import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
A = Transition(label='Customer searches for ticket')
B = Transition(label='Select route')
C = Transition(label='Select date and time')
D = Transition(label='Provide personal information')
E = Transition(label='Provide payment details')
F = Transition(label='Generate ticket')
G = Transition(label='Send ticket via email')
H = Transition(label='Send ticket via SMS')
I = Transition(label='Update seat inventory')
J = Transition(label='Customer completes journey')
K = Transition(label='Post-travel feedback or services')
L = Transition(label='Send reminder')
M = Transition(label='Send instructions')

# Define the process structure
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M])

# Define the process order
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
root.order.add_edge(J, K)
root.order.add_edge(J, L)
root.order.add_edge(L, M)
root.order.add_edge(M, J)

# Print the final result
print(root)