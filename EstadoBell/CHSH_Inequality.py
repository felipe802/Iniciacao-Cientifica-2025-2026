# CHSH Inequality: Breaking the classical limit of S <= 2

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def chsh_circuit(theta_a, theta_b):
  # Creates a CHSH circuit for specific measurement angles
  qc = QuantumCircuit(2, 2)

  # 1. Prepares the Bell State |Phi+>
  qc.h(0)
  qc.cx(0, 1)

  # 2. Rotation of measurement bases (simulates Alice and Bob rotating their detectors)
  qc.ry(theta_a, 0)
  qc.ry(theta_b, 1)

  qc.measure([0, 1], [0, 1])
  return qc

# Angles that maximize the quantum violation
theta_A = 0               # Alice measures the Z axis
theta_A_prime = np.pi/2   # Alice measures the X axis
theta_B = np.pi/4         # Bob measures on diagonal W
theta_B_prime = -np.pi/4  # Bob measures on diagonal V

# We need to test 4 angle combinations: (A, B), (A, B'), (A', B), (A', B')
circuits = [
    chsh_circuit(theta_A, theta_B),
    chsh_circuit(theta_A, theta_B_prime),
    chsh_circuit(theta_A_prime, theta_B),
    chsh_circuit(theta_A_prime, theta_B_prime)
]

sim = AerSimulator()
E_values = []

# Executes the 4 circuits and calculates the expected value for each
for qc in circuits:
  counts = sim.run(qc, shots=8192).result().get_counts()

  # Probability of equal results (00 or 11) vs different (01 or 10)
  equal = counts.get('00', 0) + counts.get('11', 0)
  different = counts.get('01', 0) + counts.get('10', 0)
  total = equal + different

  # E = P(equal) - P(different)
  E = (equal - different) / total
  E_values.append(E)

# Calculates the CHSH S-parameter: S = E(A,B) - E(A,B') + E(A',B) + E(A',B')
S = E_values[0] - E_values[1] + E_values[2] + E_values[3]

print(f"Calculated S-parameter: {S:.4f}")
print("Maximum classical limit: 2.0000")
print(f"Maximum quantum limit: {2*np.sqrt(2):.4f}")

if S > 2:
  print("Success! The CHSH inequality was violated (Entanglement proven).")
