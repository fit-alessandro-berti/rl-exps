from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
A = Transition(label='Farm Registration')
B = Transition(label='Lot Tagging')
C = Transition(label='Soil Testing')
D = Transition(label='Harvest Logging')
E = Transition(label='Coffee Sorting')
F = Transition(label='Sensory Profiling')
G = Transition(label='Quality Scoring')
H = Transition(label='Blockchain Entry')
I = Transition(label='Environmental Audit')
J = Transition(label='Farmer Feedback')
K = Transition(label='Dynamic Pricing')
L = Transition(label='Roast Scheduling')
M = Transition(label='Batch Testing')
N = Transition(label='Certification Review')
O = Transition(label='Distribution Prep')
P = Transition(label='Consumer Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P])

# Define the partial order structure
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

print(root)