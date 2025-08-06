from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Site Analysis')
B = Transition(label='Climate Setup')
C = Transition(label='Nutrient Mix')
D = Transition(label='Seed Germinate')
E = Transition(label='Auto Planting')
F = Transition(label='Irrigation Setup')
G = Transition(label='IoT Monitoring')
H = Transition(label='Pest Detection')
I = Transition(label='Drone Pollinate')
J = Transition(label='Pesticide Spray')
K = Transition(label='Robotic Harvest')
L = Transition(label='Quality Check')
M = Transition(label='Package Product')
N = Transition(label='Waste Recycle')
O = Transition(label='Energy Optimize')
P = Transition(label='Data Logging')

# Define silent transitions
skip = SilentTransition()

# Define partial order
root = StrictPartialOrder(
    nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P],
    order={
        (A, B): None,
        (B, C): None,
        (C, D): None,
        (D, E): None,
        (E, F): None,
        (F, G): None,
        (G, H): None,
        (H, I): None,
        (I, J): None,
        (J, K): None,
        (K, L): None,
        (L, M): None,
        (M, N): None,
        (N, O): None,
        (O, P): None
    }
)

# Define control-flow operators
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