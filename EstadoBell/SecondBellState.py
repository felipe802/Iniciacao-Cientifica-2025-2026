# Segundo Estado de Bell $\ket{\Phi^{-}}$
# A diferença para o primeiro estado é uma inversão de fase quando o sistema
# está em |11>

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

# 1. Preparação: Começamos invertendo o qubit 0 para |1>
# Isso garante que, após a Hadamard, teremos a fase negativa
qc.x(0)

# 2. Criação de Superposição com fase
# O estado |1> transformado pelo H vira |-> = (|0> - |1>) / sqrt(2)
qc.h(0)

# 3. Emaranhamento (CNOT)
# O controle (0) espalha a fase e a correlação para o alvo (1)
qc.cx(0, 1)

# 4. Medição
qc.measure([0, 1], [0, 1])

# 5. Simulalção e visualização
counts = sim.run(qc, shots=1024).result().get_counts()
print(f"Resultados |Phi->: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)