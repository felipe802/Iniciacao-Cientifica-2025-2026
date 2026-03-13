# Desigualdade CHSH: Quebrando o limite clássico de S <= 2

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def circuito_chsh(theta_a, theta_b):
  # Cria um circuito CHSH para ângulos de medição específicos
  qc = QuantumCircuit(2, 2)

  # 1. Prepara o Estado de Bell |Phi+>
  qc.h(0)
  qc.cx(0, 1)

  # 2. Rotação das bases de medição (simula Alice e Bob girando seus detectores)
  qc.ry(theta_a, 0)
  qc.ry(theta_b, 1)

  qc.measure([0, 1], [0, 1])
  return qc

# Ângulos que maximizam a violação quântica
theta_A = 0               # Alice mede o eixo Z
theta_A_linha = np.pi/2   # Alice mede no eixo X
theta_B = np.pi/4         # Bob mede na diagonal W
theta_B_linha = -np.pi/4  # Bob mede na diagonal V

# Precisamos testar 4 combinações de ângulos: (A, B), (A, B'), (A', B), (A', B')
circuitos = [
    circuito_chsh(theta_A, theta_B),
    circuito_chsh(theta_A, theta_B_linha),
    circuito_chsh(theta_A_linha, theta_B),
    circuito_chsh(theta_A_linha, theta_B_linha)
]

sim = AerSimulator()
valores_E = []

# Executa os 4 circuitos e calcula o valor esperado para cada um
for qc in circuitos:
  counts = sim.run(qc, shots=8192).result().get_counts()

  # Probabilidade de resultados iguais (00 ou 11) vs diferentes (01 ou 10)
  iguais = counts.get('00', 0) + counts.get('11', 0)
  diferentes = counts.get('01', 0) + counts.get('10', 0)
  total = iguais + diferentes

  # E = P(iguais) - P(diferentes)
  E = (iguais - diferentes) / total
  valores_E.append(E)

# Calcula o parâmetro S da CHSH: S = E(A,B) - E(A,B') + E(A',B) + E(A',B')
S = valores_E[0] - valores_E[1] + valores_E[2] + valores_E[3]

print(f"Parâmetro S calculado: {S:.4f}")
print("Limite máximo clássico: 2.0000")
print(f"Limite máximo quântico: {2*np.sqrt(2):.4f}")

if S > 2:
  print("Sucesso! A desigualdade CHSH foi violada (Emaranhamento comprovado).")
