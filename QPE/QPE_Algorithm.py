# Quantum Phase Estimation (QPE) Algorithm
# Extraction of the secret geometric phase (theta = 1/8) of the P(lambda) gate

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt
import numpy as np

# 1. Problem Definition
secret_theta = 1/8  
angle = 2 * np.pi * secret_theta
t = 3  # Readout qubits (N=8)
n_target = 1

qc = QuantumCircuit(t + n_target, t)

# 2. Preparation
for qubit in range(t):
    qc.h(qubit)
qc.x(t) # Eigenvector |1>
qc.barrier()

# 3. Phase Kickback with powers of U
repetitions = 1
for counting_qubit in range(t):
    for i in range(repetitions):
        qc.cp(angle, counting_qubit, t)
    repetitions *= 2
qc.barrier()

# 4. Decoder: Inverse QFT
qft_inverse = QFT(num_qubits=t, inverse=True, do_swaps=True).to_gate()
qft_inverse.name = "Inverse QFT"
qc.append(qft_inverse, range(t))

# 5. Measurement
for i in range(t):
    qc.measure(i, i)

sim = AerSimulator()
qc_transpiled = transpile(qc, sim)
counts = sim.run(qc_transpiled, shots=1024).result().get_counts()

print(f"Raw results: {counts}")

circuit_fig = qc.draw('mpl', style="iqp")
histogram_fig = plot_histogram(counts, title="QPE: Estimated Phase")
display(circuit_fig)
display(histogram_fig)