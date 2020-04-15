###################################################################################
#  Deutsch Algorithm implimentation
#
# I got a lot of Inspiration from the following documentation.
#       - Introduction to Coding Quantum Algorithms:A Tutorial Series Using Qiskit
#
# - Author: Ghicheon Lee
#
# - History:
#   2020/04/15 initial version
###################################################################################
import math
from  qiskit import ClassicalRegister , QuantumRegister,QuantumCircuit , Aer,execute
from qiskit.tools.visualization  import circuit_drawer

M_simulator = Aer.backends(name='qasm_simulator')[0]

hidden_oracle=999

def blackbox(circuit, q):
    global hidden_oracle

    i = int(math.floor(4*sci.rand()))
    hidden_oracle=i

    if i == 0 :   #f(x) = 0
        pass
    elif i == 1: # f(x) = 1
        circuit.x(q[1])
    elif i == 2:  #f(x) = x
        circuit.cx(q[0], q[1] )
    elif i == 3:  #f(x) = ~x
        circuit.x(q[0])
        circuit.cx(q[0], q[1] )
        circuit.x(q[0])
    else:
        print("error............")

############################################################
# circuit example
#
# oracle: f(x) = x
#
#   0 ---- H  --- * --- H --- M ------          1
#                 |
#   1 ---  H  --- X --- H --- M ------          1
#
############################################################

q = QuantumRegister(2)
c = ClassicalRegister(2)
circuit = QuantumCircuit(q,c)

circuit.x(q[1]) 

circuit.h(q[0])
circuit.h(q[1])

blackbox(circuit,q)

circuit.h(q[0])
circuit.h(q[1])   # not needed

circuit.measure(q,c)

M = execute(circuit, M_simulator).result().get_counts(circuit)
print(M)

#print("oracle :", hidden_oracle )


#it works!

# > python .\deutsch.py
#    {'10': 1024}
#    oracle : 0
# > python .\deutsch.py
#    {'10': 1024}
#    oracle : 1

# > python .\deutsch.py
#    {'11': 1024}
#    oracle : 2
# > python .\deutsch.py
#    {'11': 1024}
#    oracle : 3
