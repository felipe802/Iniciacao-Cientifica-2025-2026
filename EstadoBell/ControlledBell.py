# Controlled Sub-routine: Conditional Bell State
# Demonstration of .control() and append() usage (analogous to a quantum 'if')

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Definition of the sub-routine (base circuit)
# We create the circuit of the first Bell State created previously
qc_bell = QuantumCircuit(2, name='Bell_Prep')
qc_bell.h(0)
qc_bell.cx(0, 1)

# 2. Creation of the controlled gate
# We transform the entire circuit into a single gate and add 1 control pin
c_bell_gate = qc_bell.to_gate().control(1)

# 3. Assembling the main circuit
# We will use 3 qubits: q0 (control), q1 and q2 (targets of the sub-routine)
qc = QuantumCircuit(3, 3)

# We place the control qubit in superposition to test both scenarios simultaneously
qc.h(0)

# 4. Application of the sub-routine (compose/append)
# We append the controlled gate. The list order [0, 1, 2] defines that q0 is the control
qc.append(c_bell_gate, [0, 1, 2])

# 5. Decomposition and Measurement
# To simulate and measure, we need to expand the "black box" of the sub-routine
qc_sim = qc.decompose()
qc_sim.measure([0, 1, 2], [0, 1, 2])

counts = AerSimulator().run(qc_sim, shots=1024).result().get_counts()
print(f"Controlled Circuit Results: {counts}")
# We draw the original (abstract) circuit for a clear visualization of the sub-routine
circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
