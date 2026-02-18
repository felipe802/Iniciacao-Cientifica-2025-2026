# Quarto Estado de Bell $\ket{\Psi^{-}}$
# Este é conhecido como o Estado Singleto. Os qubits esão em oposição total
# (antisimétricos)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

# 1. Diferente do primeiro estado, aqui invertemos ambos para |11>
# Isso é necessário para preparar o sistema para a fase negativa posterior
qc.x(0)
qc.x(1)

# 2. Criação da superposição com fase
# Agora o sistema está em uma mistura de (|0> - |1>) carregando o qubit 1 que é |1>
qc.h(0)

# 3. Entrelaçamento
# Se o qubit 0 for |0>, o alvo fica em |1> (Estado |01>)
# Se o qubit 0 for |1>, o alvo inverte de |1> para |0> (Estado |01>)
# O sinal negativo da porta H é "herdado", resultando em |01> - |10>
qc.cx(0, 1)

# 4. Medição e colapso
# Transformamos a probabilidade quântica em dados binários clássicos
qc.measure([0, 1], [0, 1])

# 5. Simulação e visualização
counts = sim.run(qc, shots=1024).result().get_counts()
print(f"Resultados da medição: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
