import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the activities
A = Transition(label='Site Survey')
B = Transition(label='Structural Audit')
C = Transition(label='Climate Design')
D = Transition(label='Lighting Setup')
E = Transition(label='Irrigation Plan')
F = Transition(label='Nutrient Mix')
G = Transition(label='Sensor Install')
H = Transition(label='AI Calibration')
I = Transition(label='Pest Scan')
J = Transition(label='Energy Audit')
K = Transition(label='Renewable Sync')
L = Transition(label='Data Modeling')
M = Transition(label='Staff Briefing')
N = Transition(label='Compliance Check')
O = Transition(label='Community Meet')
P = Transition(label='Yield Review')
Q = Transition(label='Feedback Loop')

# Define the partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q])

# Define the edges
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

# Print the root
print(root)