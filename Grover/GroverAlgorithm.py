# Grover's Algorithm: Search for state |0101> (w = 5) in 4 qubits

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import ZGate
import matplotlib.pyplot as plt
from qiskit import transpile

# 1. Construction of the Oracle (U_w) for state |0101>
# Assuming the visual order of the diagram: q0 (top) = 8, q1 = 4, q2 = 2, q3 = 1
# We want to mark 0101. Therefore, q0 and q2 must be inverted (X gates)
oracle = QuantumCircuit(4, name="Oracle (U_5)")

# Apply X on qubits that are '0' in the target state
oracle.x([0, 2])

# Multi-controlled Z gate (3 controls, 1 target)
mcz = ZGate().control(3)
oracle.append(mcz, [0, 1, 2, 3])

# Uncomputing to avoid leaving quantum garbage
oracle.x([0, 2])

# 2. Construction of the diffuser (U_s) - Householder Reflection
# The diffuser amplifies the amplitude of the state marked by the oracle
diffuser = QuantumCircuit(4, name="Diffuser (U_s)")

# Apply Hadamard to all qubits
diffuser.h([0, 1, 2, 3])

# Apply X to all (inversion about the zero state)
diffuser.x([0, 1, 2, 3])

# Apply the same multi-controlled Z gate
diffuser.append(mcz, [0, 1, 2, 3])

# Undo X and H gates
diffuser.x([0, 1, 2, 3])
diffuser.h([0, 1, 2, 3])

# 3. Assembling the complete circuit
qc = QuantumCircuit(4, 4)

# Preparation: uniform superposition
qc.h([0, 1, 2, 3])

# Grover Iteration
# For n=4, the optimal number of iterations is floor(pi/4 * sqrt(16)) = 3
num_iterations = 3

for _ in range(num_iterations):
  qc.append(oracle.to_instruction(), [0, 1, 2, 3])
  qc.append(diffuser.to_instruction(), [0, 1, 2, 3])

qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

sim = AerSimulator()
# Transpiling the circuit for execution (necessary for custom gates in Aer)
qc_transpiled = transpile(qc, sim)
counts = sim.run(qc_transpiled, shots=1024).result().get_counts()

print(f"Measurement results: {counts}")
circuit_fig = qc.draw('mpl', style="iqp")
display(circuit_fig)
print("\nOracle Details:")
display(oracle.draw('mpl'))
histogram_fig = plot_histogram(counts, title="Grover's Algorithm: Search for |0101>")
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
