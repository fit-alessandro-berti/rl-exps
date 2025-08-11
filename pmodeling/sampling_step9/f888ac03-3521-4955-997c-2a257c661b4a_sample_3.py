import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Order Validate')
B = Transition(label='Route Optimize')
C = Transition(label='Drone Assign')
D = Transition(label='Preflight Check')
E = Transition(label='Load Package')
F = Transition(label='Flight Launch')
G = Transition(label='Traffic Monitor')
H = Transition(label='Weather Assess')
I = Transition(label='Obstacle Avoid')
J = Transition(label='Battery Check')
K = Transition(label='Delivery Verify')
L = Transition(label='Biometric Scan')
M = Transition(label='Package Release')
N = Transition(label='Return Flight')
O = Transition(label='Post Flight')
P = Transition(label='Data Analyze')
Q = Transition(label='Feedback Collect')
R = SilentTransition()

# Define the partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R])

# Define the order
root.order.add_edge(A, B)
root.order.add_edge(B, C)
root.order.add_edge(C, D)
root.order.add_edge(D, E)
root.order.add_edge(E, F)
root.order.add_edge(F, G)
root.order.add_edge(G, H)
root.order.add_edge(H, I)
root.order.add_edge(I, J)
root.order.add_edge(J, K)
root.order.add_edge(K, L)
root.order.add_edge(L, M)
root.order.add_edge(M, N)
root.order.add_edge(N, O)
root.order.add_edge(O, P)
root.order.add_edge(P, Q)
root.order.add_edge(Q, R)

print(root)