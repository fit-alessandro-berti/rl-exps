import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Alert Trigger')
B = Transition(label='Initial Assess')
C = Transition(label='Stakeholder Notify')
D = Transition(label='Resource Check')
E = Transition(label='Risk Analyze')
F = Transition(label='Command Setup')
G = Transition(label='Deploy Teams')
H = Transition(label='Data Collect')
I = Transition(label='Situation Update')
J = Transition(label='Priority Adjust')
K = Transition(label='External Liaison')
L = Transition(label='Supply Dispatch')
M = Transition(label='Media Brief')
N = Transition(label='Impact Review')
O = Transition(label='Recovery Plan')
P = Transition(label='Process Audit')

# Define the POWL model
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P])
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