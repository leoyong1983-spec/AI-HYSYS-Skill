# Architecture

## 環境とランタイム

### なぜ Windows ネイティブ Python か

HYSYS は Windows 専用ソフトで、COM (Component Object Model) Automation 経由でしか外部制御できない。COM を Python から扱う `pywin32` パッケージは **Windows ネイティブ Python でのみ動作**(WSL 内の Python では COM 呼び出し不可)。

したがって本 MCP サーバーは **Windows 上の Python プロセスとして起動**する。

### Claude Code が WSL の場合の通信

ユーザーは WSL2 で Claude Code を使う可能性が高い。MCP は stdio ベースなので、

```
[WSL Claude Code] ─┐
                   ├──> stdio ──> [Windows Python MCP Server] ─COM─> [HYSYS]
[Win Claude Desktop] ─┘
```

WSL から Windows プロセスを起動するには `claude_desktop_config.json` に Windows パスで python.exe を指定する必要がある。

```json
{
  "mcpServers": {
    "hysys": {
      "command": "C:\\path\\to\\hysys-mcp\\venv\\Scripts\\python.exe",
      "args": ["-m", "hysys_mcp.server"]
    }
  }
}
```

WSL からの起動は Windows パス指定でも問題なく動く(`/mnt/c/` 経由)。

---

## HYSYS COM API の使い方

### 接続

```python
import win32com.client

# HYSYS が既に起動していれば既存インスタンスを取得
hysys = win32com.client.Dispatch("HYSYS.Application")
hysys.Visible = True  # GUI 表示
```

### ケース(.hsc / .tpl)を開く

```python
case = hysys.SimulationCases.Open(r"C:\path\to\file.hsc")
# または
case = hysys.ActiveDocument  # 既に開いているもの
```

### Flowsheet ナビゲーション

```python
fs = case.Flowsheet  # メインフローシート
sfs = fs.Flowsheets  # サブフローシート一覧

# マテリアルストリーム
streams = fs.MaterialStreams
for s in streams:
    print(s.name)

# 装置
ops = fs.Operations
for op in ops:
    print(op.name, op.TypeName)
```

### ストリームの値読み書き

```python
stream = fs.MaterialStreams.Item("Feed")

# 温度
T = stream.Temperature.GetValue("C")  # 摂氏で取得
stream.Temperature.SetValue(182.0, "C")

# 圧力
P = stream.Pressure.GetValue("kPa")
stream.Pressure.SetValue(2500.0, "kPa")

# モル流量
F = stream.MolarFlow.GetValue("kgmole/h")
stream.MolarFlow.SetValue(9549.0, "kgmole/h")

# 組成(モル分率)
fractions = stream.ComponentMolarFractionValue
# 例: (0.2459, 0.0534, 0.0238, ...) ← タプル
```

### ソルバー操作

```python
solver = case.Solver
solver.CanSolve  # True なら計算可能
solver.Reset()   # 初期化
solver.RunBoth() # 計算実行
```

### 収束確認

```python
# ストリームの計算ステータス
stream.IsKnown  # True なら計算済み

# 装置の状態
op.SolveComplete  # True なら収束
```

---

## MCP Server 設計方針

### Phase 1 (MVP) のスコープ

**読み取り専用ツール**だけで、まず動作確認:

1. `hysys_open` — ファイルを開く / 既存接続
2. `hysys_close`
3. `hysys_list_streams` — 全ストリーム名と所属サブフロー
4. `hysys_get_stream` — 1ストリームの詳細
5. `hysys_list_unit_ops` — 全装置名と種類
6. `hysys_get_status` — グローバル収束状態

### Phase 2 (書き込み・実行)

7. `hysys_set_stream` — T/P/流量/組成のいずれかを設定
8. `hysys_set_unit_op_param` — 装置パラメータ
9. `hysys_run` — ソルバー実行
10. `hysys_reset` — リセット
11. `hysys_save` — 別名保存

### Phase 3 (高度)

12. `hysys_get_column_profile` — 蒸留塔/吸収塔の段別プロファイル
13. `hysys_case_study` — 変数振って計算ループ
14. `hysys_place_unit` — 装置追加
15. `hysys_connect_stream` — 配線

---

## エラーハンドリング

### COM 例外

`pywin32` の COM エラーは `pywintypes.com_error` で発生。MCP ツールでキャッチして JSON-RPC error として返す。

```python
try:
    stream.Temperature.SetValue(value, "C")
except pywintypes.com_error as e:
    return {"error": f"COM error: {e.excepinfo[2]}", "code": e.hresult}
```

### HYSYS がインストールされていない/起動できない

`Dispatch("HYSYS.Application")` が `ClassFactoryError` を投げる。明確なエラーメッセージで返す。

### ストリーム/装置が見つからない

`Item("名前")` が `KeyError` 相当を投げる。一覧を取得してくれるツールで補助。

---

## 安全性の考慮

### 書き込み系のガード

`hysys_set_*` 系は破壊的な操作なので、

1. **デフォルトはドライラン**(値を表示するだけ、実際には書き込まない)
2. `confirm: true` パラメータが明示されたときだけ実行
3. ログに全操作を記録

### ファイル保存

`hysys_save` は必ず**別名保存**(上書き保存禁止)。元ファイルを破壊するリスク回避。

```python
def save(path: str):
    if os.path.exists(path):
        raise ValueError(f"File exists: {path}. Use a different name.")
    case.SaveAs(path)
```

---

## 既知の制約

1. **HYSYS が起動していないと使えない**(本サーバーは起動済みインスタンスに接続するだけ、自動起動はしない)
2. **サブフローシート(カラム内部など)へのアクセスは別途実装が必要**
3. **電解質パッケージ(Acid Gas)の電解質種は組成読み取り時に表示が複雑**
4. **HYSYS V12 と V14 で API 差分がある可能性**(V14 で動作確認予定)
