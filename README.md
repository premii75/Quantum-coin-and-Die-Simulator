# 🪙 Quantum Coin and 🎲 N-Sided Quantum Die Simulator

A Python-based **Quantum Coin and N-Sided Quantum Die Simulator** built using **Qiskit**. This project demonstrates the principles of **quantum superposition** and **quantum randomness** by simulating a fair quantum coin, a biased quantum coin, and an N-sided quantum die.

---

# 📌 Project Overview

This project uses the **Qiskit Aer Simulator** to simulate quantum circuits.

It includes:

- 🪙 Fair Quantum Coin using the Hadamard (H) Gate
- 🪙 Biased Quantum Coin using the Rotation-Y (Ry) Gate
- 🎲 N-Sided Quantum Die
- 📊 Histogram of Measurement Results
- 🔲 Quantum Circuit Visualization

---

# ✨ Features

- Fair Quantum Coin Simulation
- Biased Quantum Coin Simulation
- N-Sided Quantum Die Simulation
- Quantum Circuit Diagrams
- Measurement Histograms
- Configurable Number of Shots
- Modular Project Structure
- Built with Qiskit Aer Simulator

---

# 📂 Project Structure

```
Quantum-Coin-and-Die-Simulator/
│
├── main.py
├── README.md
├── requirements.txt
│
├── coin/
│   ├── fair_coin.py
│   ├── biased_coin.py
│   └── __init__.py
│
├── die/
│   ├── quantum_die.py
│   └── __init__.py
│
├── outputs/
│   ├── circuits/
│   └── plots/
│
└── images/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Quantum-Coin-and-Die-Simulator.git
```
Go to the project directory
```bash
cd Quantum-Coin-and-Die-Simulator
```

Install the required packages

```bash
python3 -m pip install -r requirements.txt
```

---

#  How to Run

## Fair Quantum Coin

```bash
python main.py --mode fair --shots 1024
```

---

## Biased Quantum Coin (Example: 70% Heads)

```bash
python main.py --mode biased --bias 70 --shots 1024
```

---

## 6-Sided Quantum Die

```bash
python main.py --mode die --sides 6 --shots 1000
```

---

## 20-Sided Quantum Die

```bash
python main.py --mode die --sides 20 --shots 5000
```

---

# 📊 Output

The simulator generates:

- Quantum Circuit Diagrams
- Measurement Histograms
- Console Output

Generated files are automatically saved inside:

```
outputs/
├── circuits/
└── plots/
```

---

# 🛠 Technologies Used

- Python
- Qiskit
- Qiskit Aer
- Matplotlib
- NumPy

# 🚀 Future Improvements
- Bloch Sphere Visualization
- IBM Quantum Hardware Support
- GUI Version (Tkinter / PyQt)
- Quantum Random Number Generator
- Export Results to CSV

# 👥 Team Members
**Project Title:** Quantum Coin and N-Sided Quantum Die Simulator
| Name | Role |
|------|------|
| **Prem Kumar** | **Team Leader** |
| Prashant Tomer | Team Member |
| Mansvi Bagoria | Team Member |
| Sameer Gupta | Team Member |
# 🎓 Institution
**JSS Academy of Technical Education, Noida**  
B.Tech – Information Technology
# 📜 License
This project is developed for educational and learning purposes.