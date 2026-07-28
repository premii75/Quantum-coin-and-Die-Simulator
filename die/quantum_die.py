import math
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import os
def run_quantum_die(sides, rolls):
    print(f"Running {sides}-sided die simulation for {rolls} rolls...")
    
    num_qubits = math.ceil(math.log2(sides))
    qc = QuantumCircuit(num_qubits, num_qubits)
    for i in range(num_qubits):
        qc.h(i)
    qc.measure(range(num_qubits), range(num_qubits))
    
    os.makedirs("outputs/circuits", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)
    # Save circuit visually
    qc.draw(output='mpl', filename='outputs/circuits/quantum_die_circuit.png')
    print("Saved circuit diagram to outputs/circuits/quantum_die_circuit.png")
    
    backend = AerSimulator()
    qc_transpiled = transpile(qc, backend)
    
    valid_rolls = []
    
    while len(valid_rolls) < rolls:
        remaining = rolls - len(valid_rolls)
        # Expected acceptance rate is sides / (2^num_qubits)
        acceptance_rate = sides / (2**num_qubits)
        shots_needed = max(int(remaining / acceptance_rate * 1.2), remaining + 10)
        shots_needed = min(shots_needed, 100000) # Ensure we don't exceed simulator limits
        
        job = backend.run(qc_transpiled, shots=shots_needed, memory=True)
        result = job.result()
        outcomes = result.get_memory()
        
        for out in outcomes:
            val = int(out, 2) + 1
            if val <= sides:
                valid_rolls.append(val)
                if len(valid_rolls) == rolls:
                    break
                    
    # Count frequencies
    counts = {i: 0 for i in range(1, sides + 1)}
    for val in valid_rolls:
        counts[val] += 1
        
    print(f"Results:")
    for i in range(1, sides + 1):
        obs_prob = counts[i] / rolls * 100
        exp_prob = 100.0 / sides
        print(f"Face {i}: {counts[i]} ({obs_prob:.1f}%) [Expected: {exp_prob:.1f}%]")
        
    # Plotting
    labels = list(range(1, sides + 1))
    values = [counts[i] for i in labels]
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='orange')
    plt.title(f"{sides}-Sided Die Roll Results (Rolls: {rolls})")
    plt.xlabel('Face')
    plt.ylabel('Frequency')
    plt.xticks(labels)
    plt.savefig('outputs/plots/quantum_die_result.png')
    plt.close()
    print("Saved plot to outputs/plots/quantum_die_result.png")