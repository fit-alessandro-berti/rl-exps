import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

A = Transition(label='Select items')
B = Transition(label='Set payment method')
C = Transition(label='Pay')
D = Transition(label='Complete installment agreement')
E = Transition(label='Select free reward')
F = Transition(label='Deliver items')
G = Transition(label='Return items')

xor1 = OperatorPOWL(operator=Operator.XOR, children=[C, D])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[E, F])
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[G, loop])
root = StrictPartialOrder(nodes=[xor1, xor2, xor3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(loop, xor3)