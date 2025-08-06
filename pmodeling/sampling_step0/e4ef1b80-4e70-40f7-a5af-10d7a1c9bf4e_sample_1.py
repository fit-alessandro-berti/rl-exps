import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Opportunity Scan')
B = Transition(label='Idea Workshop')
C = Transition(label='Concept Merge')
D = Transition(label='Resource Align')
E = Transition(label='Prototype Build')
F = Transition(label='Feasibility Test')
G = Transition(label='Pilot Launch')
H = Transition(label='Feedback Gather')
I = Transition(label='Design Adapt')
J = Transition(label='Compliance Check')
K = Transition(label='Scaling Plan')
L = Transition(label='IP Management')
M = Transition(label='Market Sync')
N = Transition(label='Partner Review')
O = Transition(label='Exit Strategy')

# Define the choice and loop nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[A, B])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[C, D])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[E, F])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[G, H])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[I, J])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[K, L])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[M, N])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, O])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(loop4, xor7)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor7, O)

# Print the POWL model
print(root)