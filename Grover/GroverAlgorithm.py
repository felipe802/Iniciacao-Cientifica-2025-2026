# Algoritmo de Grover: Busca pelo estado |0101> (w = 5) em 4 qubits

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import ZGate
import matplotlib.pyplot as plt
from qiskit import transpile

# 1. Construção do Oráculo (U_w) para o estado |0101>
# Assumindo a ordem visual do diagrama: q0(topo)=8, q1=4, q2=2, q3=1
# Queremos marcar 0101. Logo, q0 e q2 devem ser invertidos (portas X)
oraculo = QuantumCircuit(4, name="Oraculo (U_5)")

# Aplica X nos qubits que são '0' no estado alvo
oraculo.x([0, 2])

# Porta Z multi-controlada (3 controles, 1 alvo)
mcz = ZGate().control(3)
oraculo.append(mcz, [0, 1, 2, 3])

# Descomputação para não deixar lixo quântico
oraculo.x([0, 2])

# 2. Construção do difusor (U_s) - Reflexão de Householder
# O difusor amplifica a amplitude do estado marcado pelo oráculo
difusor = QuantumCircuit(4, name="Difusor (U_s)")

# Aplica Hadamard a todos os qubits
difusor.h([0, 1, 2, 3])

# Aplica X a todos (inversão sobre o estado zero)
difusor.x([0, 1, 2, 3])

# Aplica a mesma porta Z multi-controlada
difusor.append(mcz, [0, 1, 2, 3])

# Desfaz as portas X e H
difusor.x([0, 1, 2, 3])
difusor.h([0, 1, 2, 3])

# 3. Montagem do circuito completo
qc = QuantumCircuit(4, 4)

# Preparação: superposição uniforme
qc.h([0, 1, 2, 3])

# Iteração Grover
# Para n=4, o número ótimo de iterações é floor(pi/4 * sqrt(16)) = 3
num_iteracoes = 3

for _ in range(num_iteracoes):
  qc.append(oraculo.to_instruction(), [0, 1, 2, 3])
  qc.append(difusor.to_instruction(), [0, 1, 2, 3])

qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

sim = AerSimulator()
# Convertendo o circuito para ser executado (necessário para custom gates no Aer)
qc_transpilado = transpile(qc, sim)
counts = sim.run(qc_transpilado, shots=1024).result().get_counts()

print(f"Resultados da medição: {counts}")
circuit_fig = qc.draw('mpl', style="iqp")
display(circuit_fig)
print("\nDetalhes do Oráculo:")
display(oraculo.draw('mpl'))
histogram_fig = plot_histogram(counts, title="Algoritmo de Grover: Busca por |0101>")
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
