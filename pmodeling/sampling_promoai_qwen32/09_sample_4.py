import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Identify idea for new product or improvement')
B = Transition(label='Conduct initial research')
C = Transition(label='Conduct feasibility studies')
D = Transition(label='Draft design concepts')
E = Transition(label='Select promising design')
F = Transition(label='Build prototype')
G = Transition(label='Test functionality')
H = Transition(label='Test safety')
I = Transition(label='Test market potential')
J = Transition(label='Collect feedback from testing phase')
K = Transition(label='Refine prototype')
L = Transition(label='Approve prototype for further development')
M = Transition(label='Discard prototype')

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[L, M])
loop = OperatorPOWL(operator=Operator.LOOP, children=[J, K])

# Define partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, loop, xor])
root.order.add_edge(A, B)
root.order.add_edge(B, C)
root.order.add_edge(C, D)
root.order.add_edge(D, E)
root.order.add_edge(E, F)
root.order.add_edge(F, G)
root.order.add_edge(F, H)
root.order.add_edge(F, I)
root.order.add_edge(G, J)
root.order.add_edge(H, J)
root.order.add_edge(I, J)
root.order.add_edge(loop, xor)