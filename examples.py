from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,execute,Aer

def quantumCoinFlip(flips):
    q = QuantumRegister(1)
    c = ClassicalRegister(1)
    perfect_coin = QuantumCircuit(q,c)
    perfect_coin.h(q[0])
    perfect_coin.measure(q,c)
    M_simulator = Aer.backends(name='qasm_simulator')[0]
    M = execute(perfect_coin,M_simulator,shots=flips).result().get_counts(perfect_coin)
    heads = M['0']
    tails = M['1']
    return heads,tails

h,t = quantumCoinFlip(1000)
print(h,t)

