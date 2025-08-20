import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Assign report to appropriate team')
B = Transition(label='Change policy')
C = Transition(label='Close incident report')
D = Transition(label='Conduct follow-up')
E = Transition(label='Conduct training')
F = Transition(label='Gather necessary information')
G = Transition(label='Identify cause of incident')
H = Transition(label='Implement fix')
I = Transition(label='Log report into tracking system')
J = Transition(label='Notify all stakeholders')
K = Transition(label='Propose corrective actions')
L = Transition(label='Report incident')

# Define the process model
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])
xor = OperatorPOWL(operator=Operator.XOR, children=[C, J])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[H, K])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[D, E])
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, C)

# Print the root
print(root)