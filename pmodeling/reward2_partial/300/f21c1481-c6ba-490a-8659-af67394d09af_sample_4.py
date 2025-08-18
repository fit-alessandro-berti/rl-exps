from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Collection Survey')
B = Transition(label='Provenance Check')
C = Transition(label='Legal Review')
D = Transition(label='Scientific Test')
E = Transition(label='Material Analysis')
F = Transition(label='Ownership Audit')
G = Transition(label='Ethical Screening')
H = Transition(label='Condition Report')
I = Transition(label='Expert Consultation')
J = Transition(label='Transport Planning')
K = Transition(label='Secure Packing')
L = Transition(label='Customs Clearance')
M = Transition(label='Insurance Setup')
N = Transition(label='Exhibit Preparation')
O = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O])

# Define the dependencies
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

# Print the result
print(root)