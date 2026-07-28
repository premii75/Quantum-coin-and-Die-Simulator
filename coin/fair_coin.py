from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
def run_fair_coin(shots):
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)
    qc.draw(output="mpl",filename="outputs/circuits/fair_coin_circuit.png")
    simulator = AerSimulator()
    qc = transpile(qc, simulator)
    result = simulator.run(qc, shots=shots).result()
    counts = result.get_counts()
    heads = counts.get("1",0)
    tails = counts.get("0",0)
    print(counts)
    plt.figure(figsize=(6,4))
    plt.bar(["Heads","Tails"],[heads,tails])
    plt.title("Fair Quantum Coin")
    plt.savefig("outputs/plots/fair_coin_result.png")
    plt.show()