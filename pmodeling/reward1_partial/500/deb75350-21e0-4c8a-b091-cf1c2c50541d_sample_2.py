from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
A = Transition(label='Intake Review')
B = Transition(label='Visual Inspect')
C = Transition(label='Material Test')
D = Transition(label='Provenance Check')
E = Transition(label='Archival Search')
F = Transition(label='Expert Consult')
G = Transition(label='Digital Scan')
H = Transition(label='Condition Report')
I = Transition(label='Forgery Assess')
J = Transition(label='Legal Review')
K = Transition(label='Risk Analysis')
L = Transition(label='Acquisition Vote')
M = Transition(label='Catalog Entry')
N = Transition(label='Storage Prep')
O = Transition(label='Final Approval')
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O
    ]
)

# Define the control flow
root.order.add_edge(A, B)
root.order.add_edge(A, C)
root.order.add_edge(B, D)
root.order.add_edge(C, D)
root.order.add_edge(D, E)
root.order.add_edge(D, F)
root.order.add_edge(E, G)
root.order.add_edge(F, G)
root.order.add_edge(G, H)
root.order.add_edge(H, I)
root.order.add_edge(I, J)
root.order.add_edge(J, K)
root.order.add_edge(K, L)
root.order.add_edge(L, M)
root.order.add_edge(M, N)
root.order.add_edge(N, O)

# Print the final result
print(root)