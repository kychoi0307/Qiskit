from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(3,3)
qc.h(0)
qc.h(1)
qc.h(2)

qc.measure(0,0)
qc.measure(1,1)
qc.measure(2,2)

qc.draw("mpl")
plt.show()

simulator = AerSimulator()
result = simulator.run(qc, shots=10000).result()

counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()