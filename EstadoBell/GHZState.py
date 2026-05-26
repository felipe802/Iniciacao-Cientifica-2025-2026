# GHZ State: (|000> + |111>) / sqrt(2)
# Multipartite entanglement involving 3 qubits

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Circuit definition
# We create a register with 3 qubits and 3 classical bits for the final measurement
qc = QuantumCircuit(3, 3)

# 2. Superposition creation
# We apply the H gate to qubit 0, placing it in superposition
qc.h(0)

# 3. Cascaded Entanglement (CNOT gates)
# Qubit 0 acts as a control for target 1
qc.cx(0, 1)
# Qubit 1 (now entangled with 0) acts as a control for target 2
qc.cx(1, 2)

# 4. Measurement (wavefunction collapse)
# We measure all 3 qubits into the 3 classical bits
qc.measure([0, 1, 2], [0, 1, 2])

sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print(f"GHZ state results: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
