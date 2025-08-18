from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
A = Transition(label='Provenance Check')
B = Transition(label='Material Scan')
C = Transition(label='Style Compare')
D = Transition(label='AI Imaging')
E = Transition(label='Chemical Test')
F = Transition(label='Aging Verify')
G = Transition(label='Record Match')
H = Transition(label='Database Query')
I = Transition(label='Panel Review')
J = Transition(label='Forgery Risk')
K = Transition(label='Market Value')
L = Transition(label='Report Draft')
M = Transition(label='Certification')
N = Transition(label='Approval Stage')
O = Transition(label='Secure Packing')
P = Transition(label='Transport Prep')

# Define the POWL model
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P])

# Define the dependencies between the nodes
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