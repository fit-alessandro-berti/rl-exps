import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
A = Transition(label='Approve prototype for further development')
B = Transition(label='Build prototype')
C = Transition(label='Collect feedback from testing phase')
D = Transition(label='Conduct feasibility studies')
E = Transition(label='Conduct initial research')
F = Transition(label='Discard prototype')
G = Transition(label='Draft design concepts')
H = Transition(label='Identify idea for new product or improvement')
I = Transition(label='Refine prototype')
J = Transition(label='Select promising design')
K = Transition(label='Test functionality')
L = Transition(label='Test market potential')
M = Transition(label='Test safety')

# Define the silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[K, M])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[B, D, E, H, J, K, M])
choice = OperatorPOWL(operator=Operator.XOR, children=[G, skip1])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[F, skip2])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[I, skip1])

# Define the root
root = StrictPartialOrder(nodes=[H, choice, E, D, choice2, G, choice3, A, loop1, loop2])
root.order.add_edge(H, E)
root.order.add_edge(E, D)
root.order.add_edge(D, choice2)
root.order.add_edge(choice2, G)
root.order.add_edge(G, choice3)
root.order.add_edge(choice3, A)
root.order.add_edge(A, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, choice3)

# Print the root
print(root)