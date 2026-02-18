# The Bell State: A Guide to Quantum Entanglement

This repository contains a practical implementation of the **Bell State** algorithm, often considered the "Hello World" of quantum computing. The goal is to demonstrate **quantum entanglement**—a phenomenon where two qubits become so deeply linked that the state of one instantly determines the state of the other.

---

## 1. Mathematical Definition
The most common Bell State is the $\lvert\Phi^+\rangle$ state, defined as:

$$\lvert\Phi^+\rangle = \frac{\lvert00\rangle + \lvert11\rangle}{\sqrt{2}}$$

In this state, there is a **50% probability** of measuring both qubits as $\lvert00\rangle$ and a **50% probability** of measuring $\lvert11\rangle$. The states $\lvert01\rangle$ and $\lvert10\rangle$ are impossible.

---

## 2. The Algorithm (Step-by-Step)

To create this state, we start with two qubits in the ground state $\lvert0\rangle$ and apply two quantum gates:

### Step 1: Hadamard Gate ($H$)
Applied to the first qubit ($q_0$), the Hadamard gate creates **superposition**:

$$H\lvert0\rangle = \frac{\lvert0\rangle + \lvert1\rangle}{\sqrt{2}}$$

At this point, the system state is: $\frac{\lvert00\rangle + \lvert10\rangle}{\sqrt{2}}$

### Step 2: Controlled-NOT Gate ($CNOT$)
We use $q_0$ as the **control** and $q_1$ as the **target**. The $CNOT$ gate flips the target qubit **if and only if** the control qubit is $\lvert1\rangle$.

Since $q_0$ is in superposition, the $CNOT$ acts on both possibilities:
1. If $q_0$ is $\lvert0\rangle \rightarrow q_1$ remains $\lvert0\rangle$.
2. If $q_0$ is $\lvert1\rangle \rightarrow q_1$ flips to $\lvert1\rangle$.

**Final Result:** The qubits are now entangled in the state $\frac{\lvert00\rangle + \lvert11\rangle}{\sqrt{2}}$.

---

## 3. Analogy: The Magic Coins
Imagine you have two "magic coins":
1. You spin the first coin on a table (**Hadamard**). While it's spinning, it’s neither heads nor tails—it’s a blur.
2. You cast a spell that links the second coin to that blur (**CNOT**).

Now, even if you take one coin to Mars and keep the other on Earth, the moment you stop the Earth coin and it lands on **Heads**, the Mars coin will **instantly** show **Heads** too.

---

## 4. How to Run
This project uses **Qiskit**. To execute the circuit, make sure you have the dependencies installed:

```bash
pip install qiskit qiskit-aer matplotlib