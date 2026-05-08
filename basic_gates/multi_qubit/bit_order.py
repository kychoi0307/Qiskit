from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(2,2)
qc.x(0)

qc.measure(0,0)
qc.measure(1,1)

qc.draw("mpl")
plt.show()

simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()

counts = result.get_counts()
print(counts) #{'01': 1000}가 출력 --> 1번, 0번 bit 순서로 출력

plot_histogram(counts)
plt.show()