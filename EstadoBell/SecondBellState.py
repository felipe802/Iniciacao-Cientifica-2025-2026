# Second Bell State \ket{\Phi^{-}}
# The difference from the first state is a phase inversion when the system is in |11>

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

# 1. Preparation: We start by inverting qubit 0 to |1>
# This ensures that, after Hadamard, we will have a negative phase
qc.x(0)

# 2. Creation of Superposition with phase
# The state |1> transformed by H becomes |-> = (|0> - |1>) / sqrt(2)
qc.h(0)

# 3. Entanglement (CNOT)
# The control (0) spreads the phase and correlation to the target (1)
qc.cx(0, 1)

# 4. Measurement
qc.measure([0, 1], [0, 1])

# 5. Simulation and visualization
sim = AerSimulator()
counts = sim.run(qc, shots=1024).result().get_counts()
print(f"Results |Phi->: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)