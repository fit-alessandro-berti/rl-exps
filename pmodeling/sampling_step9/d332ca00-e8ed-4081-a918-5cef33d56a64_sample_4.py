import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Intake Document')
B = Transition(label='Visual Inspect')
C = Transition(label='Imaging Scan')
D = Transition(label='Material Test')
E = Transition(label='Database Cross')
F = Transition(label='Provenance Check')
G = Transition(label='Expert Consult')
H = Transition(label='Carbon Dating')
I = Transition(label='Forensic Analyze')
J = Transition(label='Anomaly Review')
K = Transition(label='Risk Assess')
L = Transition(label='Report Draft')
M = Transition(label='Insurance Quote')
N = Transition(label='Storage Plan')
O = Transition(label='Final Approval')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O])
xor = OperatorPOWL(operator=Operator.XOR, children=[O, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)