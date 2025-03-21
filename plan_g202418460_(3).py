# -*- coding: utf-8 -*-
"""plan_g202418460 (3).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q76pw6TAf6rzpDuQiaggXIESeLMA_pM6

# ***Install Pennylane***
"""

pip install pennylane

"""# ***import***"""

import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

"""# ***word = "ABC" (WORK, ONLY 9 QUBITS)***
shorter code

"""

word = "ABC"

SSL = []
for L in word:
    letASCII = ord(L) -64
    SS = np.binary_repr(letASCII,width=2)
    SSL.append(SS)
print(SSL)

numQubits = (2+1)*3

numQubits = (2 + 1) * 3

qc = qml.device("default.qubit", wires=9, shots=1)  # shots=1 for single measurement outcome

@qml.qnode(qc)
def prepare_state():
    N_W = 9

    for i in range(N_W):
        if i % 3 == 2:
            qml.H(wires=i)
            qml.Z(wires=i)
        else:
            qml.H(wires=i)

    A = 0
    for s in SSL:
        s = s[::-1]
        for q in range(2):
            if s[q] == '1':
                qml.CNOT(wires=[A * 3 + q, A * 3 + 2])
        A = A + 1

    for j in range(N_W):
        if j % 3 != 2:
            qml.H(wires=j)

    return [qml.sample(wires=j) for j in range(N_W) if j % 3 != 2]


results = prepare_state()
print(results)

circuit = qml.draw(prepare_state)
print(circuit())

binary_word = "".join(str(i) for i in results)
binary = binary_word[::-1]
print("binary_word:", binary)
let_index = 0
ll = []
for i in range(3):
    letter = binary[i*2:i*2+2]
    let_index=let_index+1
    wlet = int(letter,2)
    ll.append(chr(wlet+64))
ll.reverse()
print('The word is ', ll)

"""# word = "FILE" (WORK, ONLY 20 QUBITS)

"""

word = "FILE"

SSL = []
for L in word:
    letASCII = ord(L) -64
    SS = np.binary_repr(letASCII,width=4)
    SSL.append(SS)
print(SSL)

numQubits = (4+1)*4

numQubits = (4+1)*4

qc = qml.device("default.qubit", wires=20, shots=1)  # shots=1 for single measurement outcome

@qml.qnode(qc)
def prepare_state():
    N_W = 20

    for i in range(N_W):
        if i % 5 == 4:
            qml.H(wires=i)
            qml.Z(wires=i)
        else:
            qml.H(wires=i)

    A = 0
    for s in SSL:
        s = s[::-1]
        for q in range(4):
            if s[q] == '1':
                qml.CNOT(wires=[A * 5 + q, A * 5 + 4])
        A = A + 1

    for j in range(N_W):
        if j % 5 != 4:
            qml.H(wires=j)

    return [qml.sample(wires=j) for j in range(N_W) if j % 5 != 4]


results = prepare_state()
print(results)

circuit = qml.draw(prepare_state)
print(circuit())

binary_word = "".join(str(i) for i in results)
binary = binary_word[::-1]
print("binary_word:", binary)
let_index = 0
ll = []
for i in range(4):
    letter = binary[i*4:i*4+4]
    let_index=let_index+1
    wlet = int(letter,2)
    ll.append(chr(wlet+64))
ll.reverse()
print('The word is ', ll)

"""# word = "APPLE" (DID NOT WORK, 30 QUBITS, SESSION CRASHING)"""

word = "APPLE"

SSL = []
for L in word:
    letASCII = ord(L) -64
    SS = np.binary_repr(letASCII,width=5)
    SSL.append(SS)
print(SSL)

numQubits = (5+1)*5

numQubits = (5+1)*5

qc = qml.device("default.qubit", wires=30, shots=1)  # shots=1 for single measurement outcome

@qml.qnode(qc)
def prepare_state():
    N_W = 30

    for i in range(N_W):
        if i % 6 == 5:
            qml.H(wires=i)
            qml.Z(wires=i)
        else:
            qml.H(wires=i)

    A = 0
    for s in SSL:
        s = s[::-1]
        for q in range(5):
            if s[q] == '1':
                qml.CNOT(wires=[A * 5 + q, A * 6 + 5])
        A = A + 1

    for j in range(N_W):
        if j % 6 != 5:
            qml.H(wires=j)

    return [qml.sample(wires=j) for j in range(N_W) if j % 6 != 5]


results = prepare_state()
print(results)

circuit = qml.draw(prepare_state)
print(circuit())

binary_word = "".join(str(i) for i in results)
binary = binary_word[::-1]
print("binary_word:", binary)
let_index = 0
ll = []
for i in range(5):
    letter = binary[i*5:i*5+5]
    let_index=let_index+1
    wlet = int(letter,2)
    ll.append(chr(wlet+64))
ll.reverse()
print('The word is ', ll)