# First Bell State \ket{\Phi^{+}}

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Circuit definition
# We create a register with 2 qubits and 2 classical bits (to store the measurements)
# In the Hilbert space, this represents a system of dimension 4
qc = QuantumCircuit(2, 2)

# 2. Superposition creation (Hadamard gate)
# We apply the H gate to qubit 0 (control)
# This transforms |0> into |+> = (|0> + |1>) / sqrt(2)
qc.h(0)

# 3. Entanglement (CNOT gate)
# qubit 0 is the control and qubit 1 is the target
# If qubit 0 is |1>, qubit 1 inverts. This creates the correlation described above
qc.cx(0, 1)

# 4. Measurement (wavefunction collapse)
# Both qubits are measured into their respective classical bits.
# This step "forces" the system to choose a basis state (Born rule)
qc.measure([0, 1], [0, 1])

# 5. Execution and simulation
# Use AerSimulator to run the experiment 1024 times
sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()

# Obtain the counts of how many times each state was measured
counts = result.get_counts()
print(f"Measurement results (State: Frequency): {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)