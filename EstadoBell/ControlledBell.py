# Sub-rotina Controlada: Estado de Bell Condicional
# Demonstração do uso de .control() e append() (análogo ao 'if' quântico)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Definição da sub-rotina (circuito base)
# Criamos o circuito do primeiro estado de Bell criado anteriormente
qc_bell = QuantumCircuit(2, name='Bell_Prep')
qc_bell.h(0)
qc_bell.cx(0, 1)

# 2. Criação da porta controlada
# Transformamos o circuito inteiro em uma única porta e adicionamos 1 pino de controle
c_bell_gate = qc_bell.to_gate().control(1)

# 3. Construção do circuito principal
# Usaremos 3 qubits: q0 (controle), q1 e q2 (alvos da subrotina)
qc = QuantumCircuit(3, 3)

# Colocamos o controle em superposição para testar os dois cenários simultaneamente
qc.h(0)

# 4. Aplicação da sub-rotina (compose/append)
# Anexamos a porta controlada. A ordem da lista [0, 1, 2] define que q0 é o controle
qc.append(c_bell_gate, [0, 1, 2])

# 5. Decomposição e Medição
# Para simular e medir, precisamos expandir a "caixa preta" da sub-rotina
qc_sim = qc.decompose()
qc_sim.measure([0, 1, 2], [0, 1, 2])

counts = AerSimulator().run(qc_sim, shots=1024).result().get_counts()
print(f"Resultados do Circuito Controlado: {counts}")
# Desenhamos o circuito original (abstrato) para visualização clara da sub-rotina
circuit_fig = qc.draw('mpl')
histogram_fig = plot_histogram(counts)
display(circuit_fig)
display(histogram_fig)
plt.close(circuit_fig)
plt.close(histogram_fig)
