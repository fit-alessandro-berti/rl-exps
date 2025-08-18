import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Assess Structure')
B = Transition(label='Analyze Environment')
C = Transition(label='Design Modules')
D = Transition(label='Procure Materials')
E = Transition(label='Install Irrigation')
F = Transition(label='Set Sensors')
G = Transition(label='Select Seeds')
H = Transition(label='Schedule Planting')
I = Transition(label='Monitor Growth')
J = Transition(label='Collect Data')
K = Transition(label='Manage Pests')
L = Transition(label='Harvest Crops')
M = Transition(label='Coordinate Sales')
N = Transition(label='Compost Waste')
O = Transition(label='Review Feedback')

# Define POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[N, O])
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, xor])
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
root.order.add_edge(M, xor)