from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(1,1) #1개의 qubit와 1개의 classical bit 생성
qc.h(0) #0번 qubit에 H-gate 적용
# qc.h(0) #한 번 더 적용하면 0으로 되돌아감

qc.measure(0,0) #0번 qubit의 측정결과를 0번 classical bit에 저장

qc.draw("mpl")
plt.show()

simulator = AerSimulator() #Qiskit 시뮬레이터 생성
result = simulator.run(qc, shots=10000).result() #회로를 10000번 실행하고 측정 결과를 가져옴

counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()