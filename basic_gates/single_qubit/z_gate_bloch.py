import sympy as sp
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)

qc.h(0)
qc.z(0)

state = Statevector(qc)
plot_bloch_multivector(state)
plt.show()

matrix = Operator(qc).data
symbolic_matrix = sp.Matrix(matrix).applyfunc(sp.nsimplify)
sp.pprint(symbolic_matrix)