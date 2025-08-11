import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Intake Review')
B = Transition(label='Preliminary Inspect')
C = Transition(label='Provenance Check')
D = Transition(label='Archival Research')
E = Transition(label='Material Testing')
F = Transition(label='Radiocarbon Date')
G = Transition(label='Stylistic Assess')
H = Transition(label='Expert Consult')
I = Transition(label='Findings Compile')
J = Transition(label='Internal Review')
K = Transition(label='Client Present')
L = Transition(label='Approval Confirm')
M = Transition(label='Secure Package')
N = Transition(label='Transport Arrange')
O = Transition(label='Chain Custody')

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[D, E, F, G, H])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[I, J, K])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[L, M])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[N, O])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor2, xor3])
root = StrictPartialOrder(nodes=[xor, xor4])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)

# Print the root POWL model
print(root)