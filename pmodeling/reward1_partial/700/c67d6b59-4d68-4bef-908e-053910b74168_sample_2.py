from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
A = Transition(label='Client Meet')
B = Transition(label='Design Draft')
C = Transition(label='Vendor Select')
D = Transition(label='Component Order')
E = Transition(label='Parts Inspect')
F = Transition(label='Frame Build')
G = Transition(label='Wiring Setup')
H = Transition(label='Software Load')
I = Transition(label='Flight Sim')
J = Transition(label='Quality Test')
K = Transition(label='Feedback Review')
L = Transition(label='Adjust Design')
M = Transition(label='Compliance Check')
N = Transition(label='Packaging Prep')
O = Transition(label='Final Demo')
P = Transition(label='Ship Drone')

# Create the POWL model
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P])

# Define the dependencies between activities
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

# Print the root of the POWL model
print(root)