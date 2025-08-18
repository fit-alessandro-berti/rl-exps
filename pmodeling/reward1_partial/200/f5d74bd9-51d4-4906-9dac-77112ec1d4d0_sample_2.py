from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) in the process
A = Transition(label='Site Review')
B = Transition(label='Impact Study')
C = Transition(label='Design Plan')
D = Transition(label='Structure Mod')
E = Transition(label='Hydroponics Setup')
F = Transition(label='Crop Select')
G = Transition(label='Nutrient Mix')
H = Transition(label='Pest Control')
I = Transition(label='Sensor Install')
J = Transition(label='Staff Train')
K = Transition(label='Compliance Audit')
L = Transition(label='Packaging Dev')
M = Transition(label='Logistics Plan')
N = Transition(label='Community Engage')
O = Transition(label='Sustainability Check')

# Define the partial order model
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O])

# Define the dependencies between the transitions
root.order.add_edge(A, B)
root.order.add_edge(A, C)
root.order.add_edge(B, D)
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

# Print the root model
print(root)