# Python–SCADABR Tutorial with Modbus

This repository documents how to implement **Modbus communication between Python and SCADABR**, using `pymodbus`, `pymodbusTCP`, and numerical libraries. The guide follows the original tutorial by **Lizandro de Sousa** and adapts it into a GitHub-friendly README.

---

## Author

**Lizandro de Sousa**
Email: [lizandrosousa@id.uff.br](mailto:lizandrosousa@id.uff.br)

---

## Contents

* Library installation
* Modbus implementation in Python
* SCADABR installation
* Communication between Python and SCADABR

---

## 1. Installation of Required Libraries

### Required Libraries

* `pymodbusTCP`
* `pymodbus` (version 2.5.3)
* `NumPy`
* `SciPy`

### 1.1 Installing PymodbusTCP

Run the following command in the **Anaconda Prompt**:

```bash
pip install pymodbusTCP
```

### 1.2 Installing Pymodbus (version 2.5.3)

```bash
pip install --force-reinstall -v "pymodbus==2.5.3"
```

### 1.3 Installing NumPy

```bash
conda install numpy
```

### 1.4 Installing SciPy

```bash
conda install scipy
```

---

## 2. Modbus Implementation in Python

Two Python scripts are required to test Modbus communication:

* `servidor.py`
* `teste-scada.py`

### 2.1 Development Environment

1. Open **Spyder**
2. Set the working directory to:

```text
~SCADA/tutorial/
```

3. Check the files in the **Files** tab
4. Open both scripts

---

### 2.2 Script Descriptions

<img width="267" height="405" alt="image" src="https://github.com/user-attachments/assets/be242a84-f126-4c9b-a2e3-fc84d4cfa186" />


#### servidor.py

* Acts as a Modbus server
* Receives variable values written by `teste-scada.py` or by SCADABR

#### teste-scada.py

* Communicates with `servidor.py`
* Performs read and write operations via Modbus

---

### 2.3 Script Structure

#### servidor.py

* Library imports
* Execution logic
* Server port definition

#### teste-scada.py

* Library imports
* Read/write functions
* Test execution logic

---

### 2.4 Running the Scripts

In **Spyder**, open **two consoles**.

#### First Console

Run `servidor.py`:

1. Click on the console
2. Select `servidor.py`
3. Execute the script

The server should start running.

#### Second Console

Run `teste-scada.py`:

1. Click on the console
2. Select `teste-scada.py`
3. Execute the script

---

### 2.5 Expected Behavior

* Write values **10**, **20**, and **30** to the server

  * Success: `OK`
  * Failure: `Error`

* Read the first two values

  * Success: `OK`
  * Failure: `Error`

---

## 3. SCADABR Installation

Download **SCADABR version 1.2** from:

```
https://scadabr.org/
```

> **Note:** Java 8 may be required.

After installation, a ScadaBR icon will appear on your desktop. Click it to launch the application in your web browser.

---

## 4. Communication Between Python Server and SCADABR

### 4.1 Accessing SCADABR

1. Open **ScadaBR**
2. Log in with:

   * Username: `admin`
   * Password: `admin`
   *
<img width="982" height="441" alt="image" src="https://github.com/user-attachments/assets/c16313ef-2706-4675-9880-7a99035d1ea3" />


---

### 4.2 Creating a Datasource

1. Navigate to **Datasources**
2. Select **Modbus IP**
3. Click **Add**

<img width="1004" height="467" alt="image" src="https://github.com/user-attachments/assets/9f3a9a0e-7a16-469e-b8be-7150aeaae647" />


Configure the datasource:

* **Name:** teste
* **Update period:** 5 seconds
* **Host:** localhost
* **Port:** 5028

Click **Save**, then **Enable** the datasource.

<img width="1019" height="466" alt="image" src="https://github.com/user-attachments/assets/541f861a-8af7-457e-9246-f00762f84bd7" />

---

### 4.3 Creating Datapoints

#### Datapoint 1

* Name: `var_1`
* Register type: Holding Register
* Data type: 4-byte float

Save and enable the datapoint.

<img width="991" height="469" alt="image" src="https://github.com/user-attachments/assets/e7079db9-9201-4cf3-8adf-b0be59a551ac" />


#### Datapoint 2

* Name: `var_2`
* Register type: Holding Register
* Data type: 4-byte float
* Offset: 2

Save and enable the datapoint.

<img width="1004" height="468" alt="image" src="https://github.com/user-attachments/assets/a4314ffb-3d9a-4e2d-9c2c-94b75b97e58e" />

---

## 5. Watchlist Visualization

1. Open the **Watchlist**
2. Verify that the datapoints appear
3. Click the green arrows to monitor real-time values

<img width="972" height="441" alt="image" src="https://github.com/user-attachments/assets/c7712333-4323-4bf2-9a64-caa2ab6aefa1" />

---

## Notes

* Ensure that the Python Modbus server is running before enabling the SCADABR datasource
* Port numbers and offsets must match between Python and SCADABR

---

## License / Usage

This README is a reformatted version of an educational tutorial. Use it for learning, teaching, and experimentation with Modbus, Python, and SCADABR.
