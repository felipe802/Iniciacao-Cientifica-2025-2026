# Estado GHZ: (|000> + |111>) / sqrt(2)
# Emaranhamento multipartido envolvendo 3 qubits

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Definição do circuito
# Criamos um registro com 4 qubits e 3 bits clássicos para a medição final
qc = QuantumCircuit(3, 3)

# 2. Criação de Superposição
# Aplicamos a porta H no qubit 0, colocando-o em superposição
qc.h(0)

# 3. Emaranhamento em cascata (portas CNOT)
# O qubit 0 atua como controle para o alvo 1
qc.cx(0, 1)
# O qubit 1 (agora emaranhado com o 0) atua como controle para o alvo 2
qc.cx(1, 2)

# 4. Medição (colapso da função de onda)
# Medimos os 3 qubits nos 3 bits clássicos
qc.measure([0, 1, 2], [0, 1, 2])

sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print(f"Resultados do estado GHZ: {counts}")

circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
