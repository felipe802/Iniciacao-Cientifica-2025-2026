# Fourth Bell State \ket{\Psi^{-}}
# This is known as the Singlet State. Qubits are in complete opposition (anti-symmetric)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

# 1. Unlike the first state, here we invert both qubits to |11>
# This is necessary to prepare the system for the subsequent negative phase
qc.x(0)
qc.x(1)

# 2. Creation of the superposition with phase
# Now the system is in a mixture of (|0> - |1>) carrying qubit 1 which is |1>
qc.h(0)

# 3. Entanglement
# If qubit 0 is |0>, the target remains |1> (State |01>)
# If qubit 0 is |1>, the target flips from |1> to |0> (State |10>)
# The negative sign from the H gate is "inherited", resulting in |01> - |10>
qc.cx(0, 1)

# 4. Measurement and collapse
# We transform quantum probability into classical binary data
qc.measure([0, 1], [0, 1])

# 5. Simulation and visualization
sim = AerSimulator()
counts = sim.run(qc, shots=1024).result().get_counts()
print(f"Measurement results: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
