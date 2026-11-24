import IPython
from qiskit.quantum_info import Statevector
import numpy as np
from numpy import sqrt
from IPython.display import display

u =Statevector([1.0/sqrt(3)+1/sqrt(3)*1j ,1/sqrt(3)])
print(u.is_valid())

display(u.draw("latex"))
display(u.draw("text"))
