from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(1,1) #1개의 qubit와 1개의 classical bit 생성
qc.x(0) #0번 qubit에 X-gate 적용

qc.measure(0,0) #0번 qubit의 측정결과를 0번 classical bit에 저장

circuit_figure = qc.draw("mpl")
circuit_figure.savefig("results/x_gate_circuit.png")
plt.show()

simulator = AerSimulator() #Qiskit 시뮬레이터 생성
result = simulator.run(qc, shots=1000).result() #회로를 1000번 실행하고 측정 결과를 가져옴

counts = result.get_counts()
print(counts)

histogram_figure = plot_histogram(counts)
histogram_figure.savefig("results/x_gate_result.png")
plt.show()