# Pressure Drop Estimation in Pipelines

## 📌 Overview
This project presents a comprehensive **pressure drop estimation model for fluid flow in straight pipelines** using the **Darcy–Weisbach equation**.  
The analytical model is implemented and validated across multiple engineering and simulation platforms, demonstrating both **theoretical understanding** and **industrial relevance**.

The work focuses on flow regime identification, friction factor modeling, minor loss estimation, and multi-software validation.

---

## 🎯 Objectives
- Develop an analytical model to estimate pressure drop in pipelines  
- Analyze the effect of flow regime, pipe roughness, and fittings  
- Implement the same engineering methodology across multiple platforms  
- Validate analytical results using industrial and open-source simulators  

---

## 🧠 Engineering Methodology
The same structured workflow is followed in all tools:

1. Define fluid properties and pipe geometry  
2. Calculate velocity and Reynolds number  
3. Identify flow regime (laminar or turbulent)  
4. Select appropriate friction factor model  
5. Compute straight-pipe frictional losses  
6. Evaluate minor losses using K-values  
7. Determine total pressure drop  
8. Validate results using simulation tools  

---

## 📐 Governing Equations
- Darcy–Weisbach equation for frictional pressure drop  
- Reynolds number for flow regime identification  
- Friction factor correlations:
  - Laminar flow: `f = 64 / Re`
  - Turbulent flow: Swamee–Jain equation
  - Turbulent flow: Colebrook equation (iterative)
- Minor losses using loss coefficient (K-value) approach  

---

## 💻 Tools & Implementations

### 🔹 MATLAB
- User-input-based numerical model  
- Automatic flow regime detection  
- Iterative solution of Colebrook equation  
- Algorithm-level verification  

### 🔹 Python
- Structured and modular implementation  
- Console-based user interaction  
- Suitable for automation and future scalability  

### 🔹 Microsoft Excel
- Transparent, hand-calculation-style engineering sheet  
- User-friendly input interface  
- Conditional logic for friction factor selection  

### 🔹 Aspen HYSYS
- Industrial-standard process simulator  
- Pipe segment modeling  
- Validation of analytical results  

### 🔹 DWSIM
- Open-source process simulation software  
- Pipeline unit operation modeling  
- Independent validation of pressure drop results  

---

## 📊 Validation
- Analytical results were validated using:
  - Moody chart behavior  
  - Aspen HYSYS pipe segment calculations  
  - DWSIM pipeline simulations  
- Results across all tools showed good agreement, with minor variations due to numerical methods and internal correlations.

---

## ⚠️ Assumptions & Limitations
- Steady-state flow  
- Incompressible, single-phase fluid  
- Constant fluid properties  
- Heat transfer and elevation effects neglected  
- Compressible gas flow not considered  

---

## 🚀 Future Scope
- Extension to pipe networks  
- Compressible gas flow modeling  
- Temperature-dependent fluid properties  
- Pump sizing and power estimation  
- GUI or web-based implementation  

---

## 👤 Author
**Kavinraja Chakravarthy**  
B.Tech Chemical Engineering  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kavinraja-chakravarthy)  

---

## 📄 License
This project is licensed under the **MIT License**.

