import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Identify development needs or career aspirations')
B = Transition(label='Create personal development plan')
C = Transition(label='Receive feedback and evaluation from supervisors')
D = Transition(label='Work on skill enhancement')
E = Transition(label='Consider employee for promotion or new role')
F = Transition(label='Conducts formal performance review')
G = Transition(label='Approve promotion')
H = Transition(label='Set new responsibilities')
I = Transition(label='Adjust compensation')
J = Transition(label='Transition into new role')

# Define control flow
loop = OperatorPOWL(operator=Operator.LOOP, children=[C, D])
xor = OperatorPOWL(operator=Operator.XOR, children=[E, SilentTransition()])
root = StrictPartialOrder(nodes=[A, B, loop, xor, F, G, H, I, J])
root.order.add_edge(A, B)
root.order.add_edge(B, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, F)
root.order.add_edge(F, G)
root.order.add_edge(G, H)
root.order.add_edge(H, I)
root.order.add_edge(I, J)