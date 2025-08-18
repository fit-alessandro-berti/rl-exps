from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
A = Transition(label='Provenance Check')
B = Transition(label='Material Test')
C = Transition(label='Archive Search')
D = Transition(label='Expert Review')
E = Transition(label='3D Scanning')
F = Transition(label='Wear Analysis')
G = Transition(label='Database Cross')
H = Transition(label='Law Consult')
I = Transition(label='Forgery Detect')
J = Transition(label='Certification')
K = Transition(label='Document Prep')
L = Transition(label='Client Brief')
M = Transition(label='Secure Storage')
N = Transition(label='Risk Assessment')
O = Transition(label='Final Approval')

# Define the POWL model structure
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O])
root.order.add_edge(A, B)
root.order.add_edge(A, C)
root.order.add_edge(B, D)
root.order.add_edge(B, E)
root.order.add_edge(C, G)
root.order.add_edge(D, H)
root.order.add_edge(E, F)
root.order.add_edge(F, I)
root.order.add_edge(G, J)
root.order.add_edge(H, K)
root.order.add_edge(I, K)
root.order.add_edge(J, L)
root.order.add_edge(K, M)
root.order.add_edge(L, N)
root.order.add_edge(M, O)

# Print the final POWL model
print(root)