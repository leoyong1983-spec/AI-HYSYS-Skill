# HYSYS MCP Server

[![tests](https://github.com/yuuyo-arobet/AspenHYSYS-MCP-Server/actions/workflows/tests.yml/badge.svg)](https://github.com/yuuyo-arobet/AspenHYSYS-MCP-Server/actions/workflows/tests.yml)

> **English**: An MCP (Model Context Protocol) server that lets Claude Code / Claude Desktop
> drive Aspen HYSYS in natural language. 51 tools across read / session / write / flowsheet-build,
> gated by a safe mode (`HYSYS_MCP_MODE`) that is **read-only by default**. Windows-only (HYSYS COM),
> verified on HYSYS V14. See the Japanese sections below for full docs.

Aspen HYSYS を **Claude Code / Claude Desktop から自然言語で操作**するための MCP
(Model Context Protocol) サーバーです。

> MCP とは、AI アシスタント (Claude 等) に外部ツールを安全につなぐための標準プロトコル。
> このサーバーを通すと、Claude が HYSYS のストリーム値やシミュレーション結果を読んだり、
> (許可した場合のみ) モデルを編集したりできます。

---

## これは何？

HYSYS で作業するとき、AI と相談しながら GUI を手で操作するのは非効率です。
このサーバーは Windows の COM Automation 経由で HYSYS を操作し、**AI とのチャットだけで**

- ストリーム値の確認・変更
- ケーススタディの自動化
- 収束状態のリアルタイム監視
- フローシートの構築・編集

を完結できるようにします。Aspen Plus 版
([brack101/AspenPlus-MCP-Server](https://github.com/brack101/AspenPlus-MCP-Server)) は既存ですが、
**HYSYS 版は未実装**でした (2026年5月時点の調査)。本プロジェクトはその穴を埋めるものです。

## できること

- **読み取り**: ストリーム/装置/塔プロファイル/成分/物性パッケージ/収束状態の取得、物質収支チェック
- **セッション管理**: ケースの開閉・保存・複数ケース/インスタンス切替
- **書き込み** (任意): ストリーム条件やユニット操作パラメータの変更、ソルバ実行、塔スペック調整
- **フローシート構築** (任意): ストリーム/装置の新規作成・接続・削除
- **安全モード**: 環境変数ひとつで「読み取り専用」から「書き込み解禁」まで段階的に制御

合計 **51 種類のツール**を提供します (内訳は[提供ツール](#提供ツール)を参照)。

## 現在の状態

**実装・実機検証ともに完了**しています (2026-05-30 時点)。

- registry 方式へのリファクタ + モードゲート実装済み
- オフラインテスト **67 passed / 2 skipped**
- 実機 (HYSYS V14) で読み取り・構築系の書き込み・MCP 通し・実モデルまで検証済み
  (詳細は[実機検証状況](#実機検証状況))

## 安全モードについて

> ⚠️ **まず安全に使うなら、何も設定しなくて OK です。** 既定は読み取り中心の `default` モードで起動し、
> モデルを書き換えるツールは公開されません。

環境変数 `HYSYS_MCP_MODE` で「公開するツールの副作用レベル」を切り替えます。各ツールには
`read` / `session` / `write` の tag が付き、モードに応じて一覧 (`list_tools`) から除外され、
呼ばれても HYSYS に接続する前に拒否されます。

| `HYSYS_MCP_MODE` | 公開する tag | ツール数 | 用途 |
|---|---|---|---|
| `readonly` | read | 21 | 完全な閲覧専用 |
| **`default`** (既定) | read + session | 27 | 読み取り + 保存/接続管理。**モデル値は変更しない** |
| `enhanced` | read + session + write | 51 | 書き込み/ソルバ実行/フローシート構築を解禁 |

- **既定の `default` では `set_stream` / `run` / 構築系などの書き込みツールは公開されません。**
  「閲覧と保存だけ」の安全な状態で始められます。
- 書き込みを使うときだけ `HYSYS_MCP_MODE=enhanced` を設定します
  ([書込み機能を有効にする場合](#書込み機能を有効にする場合))。
- 無効な値を設定した場合は、安全側に倒して `readonly` で起動します。

## アーキテクチャ概要

```
┌─────────────────┐         ┌──────────────────────┐         ┌─────────────┐
│  Claude Code    │  MCP    │  HYSYS MCP Server    │   COM   │   HYSYS     │
│  (WSL or Win)   │ stdio   │  (Windows Python)    │  pywin32│  (Windows)  │
└─────────────────┘  <──>   └──────────────────────┘  <──>   └─────────────┘
```

- MCP server は **Windows ネイティブ Python** で動作し、`pywin32` 経由で
  `HYSYS.Application` COM オブジェクトに接続します。
- Claude Code / Claude Desktop とは stdio で通信します
  (Claude Code 本体は WSL 上でも、サーバーは Windows Python を呼びます)。
- 実装の詳細は [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) を参照してください。

---

## セットアップ

### 必要環境

- Windows 10/11
- Aspen HYSYS V12 以降 (V14 で動作確認済み)
- Python 3.10+ (**Windows ネイティブ。WSL の Python では動きません**)
- pywin32

> ⚠️ **HYSYS は Windows 専用**です。COM Automation を使うため、Linux/macOS や WSL の
> Python からは動作しません (Claude Code 本体は WSL でも可。サーバーだけ Windows Python)。

### インストール

```powershell
# Windows PowerShell
cd path\to\hysys-mcp
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e .
```

### Claude Desktop / Claude Code の設定

`%APPDATA%\Claude\claude_desktop_config.json` に追記します:

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

- `command` は各自の clone 先の `venv\Scripts\python.exe` の絶対パスに置き換えてください。
- この設定は `HYSYS_MCP_MODE` を指定していないので、既定の **`default` (読み取り + 保存)** で起動します。

### 書込み機能を有効にする場合

ストリーム値の変更・ソルバ実行・フローシート構築を使いたい場合は、`env` で
`HYSYS_MCP_MODE=enhanced` を設定します。**サーバー側の環境変数だけで完結**するので、
利用者ごとに各自の設定ファイルで切り替えられます。

```json
{
  "mcpServers": {
    "hysys": {
      "command": "C:\\path\\to\\hysys-mcp\\venv\\Scripts\\python.exe",
      "args": ["-m", "hysys_mcp.server"],
      "env": { "HYSYS_MCP_MODE": "enhanced" }
    }
  }
}
```

> ⚠️ **書き込み系は HYSYS をフリーズさせることがあります。** 既定が安全側の `default` なのは
> このためです。まず読み取りで試し、書き込みが必要になってから `enhanced` に上げる運用を推奨します。
> Claude Code 側で個別ツールを `permissions.deny` でブロックすることもできます
> (これは利用者ローカルの設定で、配布物には含まれません)。

---

## 提供ツール

実装済み 51 種。tag によって公開モードが決まります ([安全モードについて](#安全モードについて))。

### read ツール (21)

`hysys_list_streams` `hysys_get_stream` `hysys_list_unit_ops` `hysys_get_status`
`hysys_list_column_specs` `hysys_get_column_profile` `hysys_balance_check`
`hysys_get_stream_phys` `hysys_introspect` `hysys_list_components`
`hysys_find_streams` `hysys_find_ops` `hysys_list_ports` ほか

### session ツール (6)

`hysys_open` `hysys_close` `hysys_reconnect`
`hysys_list_instances` → `hysys_switch_instance` `hysys_set_active_case` `hysys_save`

### write ツール (24)

`hysys_set_stream` `hysys_set_unit_op_param` `hysys_run` `hysys_reset`
`hysys_case_study` `hysys_set_column_spec` 系 `hysys_column_run`
`hysys_set_adjust_target` `hysys_call_method` `hysys_set_property` ほか

### フローシート構築ツール

AspenPlus-MCP の enhanced (構築) モード相当 (2026-05-30 追加)。すべて `write` tag で、
既定では `confirm=false` のドライラン (実行内容の確認のみ) になります。

| ツール | 機能 |
|---|---|
| `hysys_create_stream` | マテリアル/エネルギーストリームの新規作成 |
| `hysys_create_unit_op` | 装置の新規作成 (`type_name` は `coolerop` 等 または GUI 名) |
| `hysys_connect_stream` | ストリームを装置の Feed/Product/Energy ポートへ接続 |
| `hysys_disconnect_stream` | 接続の切断 (※下記注記。当 COM ビルドでは非対応) |
| `hysys_delete_object` | ストリーム/装置の削除 (接続中でも可) |
| `hysys_list_ports` | 装置のポート列挙 (接続前の探索用、read) |

> **使う前提**: 成分 + Fluid Package が定義済みのケースが必要です。空のケースでは
> `create_stream` 自体が失敗します (HYSYS の仕様。AspenPlus-MCP も成分/物性は既存ケース前提)。
>
> **`disconnect_stream` は当 HYSYS V14 COM ビルドでは非対応**です (接続点を空にする API が
> 存在しないため)。実行すると `supported:false` と代替手段 (繋ぎ替えは `connect_stream`、
> 除去は `delete_object`、完全な切断は GUI) を返します。
>
> 成分/反応/Fluid Package の編集は環境差が大きいため専用ツールは用意していません
> (`hysys_call_method` / `hysys_set_property` で到達可能)。型名やポート名が不明なときは
> `hysys_find_ops` / `hysys_list_ports` で確認してください。

---

## 実機検証状況

2026-05-30 に HYSYS V14 で実機検証済み (要点のみ。詳細は [docs/TODO.md](docs/TODO.md))。

- **オフライン**: 67 passed / 2 skipped (WSL の system python でも `PYTHONPATH=src pytest` で実行可。
  skip は mcp/win32 未導入による環境制約)
- **読み取り**: connect / list_cases / list_streams / list_unit_ops 等を実機確認
- **構築系 write**: create_stream / create_unit_op / connect_stream / list_ports / delete_object が
  実機で全 OK、後始末でモデル無傷 (残骸ゼロ)
- **網羅検証**: energy ストリーム、装置型 mixer / heater / separator (=`flashtank`) / valve / cooler、
  feed / product / energy ポート接続をカバー
- **MCP 通し**: `server.call_tool → モードゲート → handler → 実 HYSYS` を確認
  (enhanced=51本、default=27本で write 系は非表示かつ呼び出し拒否)
- **実モデル**: 収束済みの実プロセスモデル (ストリーム 47 / ユニット操作 30 規模) で読み取り全 OK
  ＋ 孤立オブジェクトの create→delete を実施し、モデル無傷 (47→47 / 30→30)・Save 未実行を確認

再現スクリプトは `scripts/` 配下 (`live_probe.py` / `live_build_test.py` /
`live_build_test_full.py` / `live_mcp_passthrough.py` / `live_prod_test.py`)。

---

## 開発者向け情報

### ディレクトリ構成

```
src/hysys_mcp/
  registry.py      # ToolSpec(tool+handler+tag) / モードゲート / JSON 正規化 (mcp 非依存)
  server.py        # 薄い adapter: registry → list_tools / call_tool ディスパッチ
  tools/           # ドメイン別ツール定義
    connection.py  streams.py  unit_ops.py  columns.py
    solver.py      logical.py  fluid.py     generic.py
    build.py       # フローシート構築 (create/connect/delete/ports)
  hysys_client.py  # COM 層 (HYSYS.Application 操作。registry 層からは触らない)
tests/             # オフラインテスト (registry / basic)
scripts/           # 実機検証スクリプト
docs/              # ARCHITECTURE.md / TODO.md
```

`server.py` はツール登録もディスパッチも registry に委譲する薄い層です。
`registry.py` は `mcp` パッケージに依存しないため、HYSYS が無い環境 (WSL 等) でも import でき、
レジストリ層の単体テストが回ります。設計思想は AspenPlus-MCP の構成分割を移植したものです。

### ツール追加方法

`tools/<domain>.py` に `register(...)` を 1 行足すだけです (旧来の巨大な if/elif は廃止)。
新しい COM 操作が必要なら `hysys_client.py` にメソッドを追加します。

### テスト

```bash
# WSL/Linux でも registry 層のテストは回せる
PYTHONPATH=src pytest -q
```

実機テスト (HYSYS COM が必要なもの) は Windows の venv Python で `scripts/` の各スクリプトを
実行します。

---

## 注意事項

- **HYSYS は Windows 専用** — Linux/macOS/WSL の Python では動きません。
- **書き込み系は HYSYS をフリーズさせることがある** — 既定の `default` から始め、必要時のみ
  `enhanced` に上げてください。
- **構築系は成分 + Fluid Package 定義済みのケースが前提** — 空ケースでは作成に失敗します。
- **`disconnect_stream` は当 V14 COM ビルドでは非対応** — 代替手段は上記参照。

---

## 参考資料

- [Aspen Plus MCP Server (brack101)](https://github.com/brack101/AspenPlus-MCP-Server) — Aspen Plus 版、設計の参考
- [Aspen HYSYS Customization Guide (PDF, archive.org ミラー)](https://ia801808.us.archive.org/25/items/manualzz-id-1157209/1157209.pdf) — COM Automation の公式リファレンス (AspenTech, V7.3)。原典は [AspenTech サポートポータル](https://esupport.aspentech.com) で配布
- [Model Context Protocol 仕様](https://github.com/modelcontextprotocol) — MCP 標準

---

Created: 2026-05-14
