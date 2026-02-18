# Terceiro Estado de Bell $\ket{\Psi^{+}}$
# Aqui, os qubits são correlacionados de forma oposta

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

# 1. Invertemos o qubit alvo (1) para |1>
# Isso mudará o resultado da CNOT de (00, 11) para (01, 00)
qc.x(1)

# 2. Criação e Superposição
qc.h(0)

# 3. Emaranhamento (CNOT)
# Como o qubit 1 já é |1>, a CNOT alterna os estados base para opostos
qc.cx(0, 1)

# 4. Medição
qc.measure([0, 1], [0, 1])

# 5. Simulação e visualização
counts = sim.run(qc, shots=1024).result().get_counts()
print(f"Resultados |Psi+>: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)