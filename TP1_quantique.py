import IPython
from qiskit.quantum_info import Statevector
import numpy as np
from numpy import sqrt
from IPython.display import display

### Partie 1 : Tuto d'utilisation de Qiskit
u = Statevector([1.0 / sqrt(3) + 1 / sqrt(3) * 1j, 1 / sqrt(3)])
print(u.is_valid())

display(u.draw("latex"))
display(u.draw("text"))
print("\n")
u.seed(value=11)
a = u.measure()
print(a)
print("\n")
display(a[1].draw("text"))
sim = u.sample_counts(10000)
print(sim['1'] / 10000)
print(u.probabilities())
zero = Statevector.from_label("0")
display(zero.draw("text"))

### Partie 2 : Création d'OPerateur

from qiskit.quantum_info import Operator

print("Operator T : ")
T = Operator([[1,0], [0, (1 + 1.0j) / sqrt(2)]])
display(T.draw("text"))
print("Operator X : ")
X= Operator([[0 , 1], [1, 0]])
display(X.draw("text"))
print("Operator Y : ")
Y = Operator([[0 , -1j], [1j, 0]])
print(Y.draw("text"))
print("Operator Z : ")
Z = Operator([[1, 0], [0, -1]])
print(Z.draw("text"))
print("Operator H : ")
H = Operator([[1/sqrt(2),1/sqrt(2) ], [1/sqrt(2), -1/sqrt(2)]])

zero = zero.evolve(H)
display(zero.draw("text"))