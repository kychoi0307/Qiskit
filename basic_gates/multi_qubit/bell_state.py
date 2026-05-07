from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(2, 2) #2개의 qubit와 2개의 classical bit 생성

qc.h(0) #0번 qubit에 H-gate 적용
qc.cx(0, 1)

qc.measure(0, 0) #0번 qubit의 측정결과를 0번 classical bit에 저장
qc.measure(1, 1) #1번 qubit의 측정결과를 1번 classical bit에 저장

qc.draw("mpl")
plt.show()

simulator = AerSimulator()

result = simulator.run(qc, shots=1000).result()

counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()