import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
A = Transition(label='Log complaint')
B = Transition(label='Assign complaint to relevant department')
C = Transition(label='Review complaint details')
D = Transition(label='Approve and notify customer')
E = Transition(label='Reject and notify customer')
F = Transition(label='Process reimbursement')
G = Transition(label='Provide feedback')
H = Transition(label='Resolve complaint')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B, C, D, E, F, G, H])
xor = OperatorPOWL(operator=Operator.XOR, children=[F, G])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)