from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Operator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1,1)

qc.h(0) #(|0> + |1>) / √2
qc.z(0) #(|0> - |1>) / √2
qc.h(0) #|1>

operator = Operator(qc) #gate의 행렬 연산
print(operator.data)

qc.measure(0,0)

qc.draw('mpl')
plt.show()

simulator = AerSimulator()
result = simulator.run(qc, shots = 1000).result()

counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()