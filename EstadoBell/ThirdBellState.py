# Third Bell State \ket{\Psi^{+}}
# Here, the qubits are correlated in opposite ways

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

# 1. We invert the target qubit (1) to |1>
# This will change the CNOT result from (00, 11) to (01, 10)
qc.x(1)

# 2. Creation and Superposition
qc.h(0)

# 3. Entanglement (CNOT)
# Since qubit 1 is already |1>, the CNOT toggles the basis states to opposite ones
qc.cx(0, 1)

# 4. Measurement
qc.measure([0, 1], [0, 1])

# 5. Simulation and visualization
sim = AerSimulator()
counts = sim.run(qc, shots=1024).result().get_counts()
print(f"Results |Psi+>: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)