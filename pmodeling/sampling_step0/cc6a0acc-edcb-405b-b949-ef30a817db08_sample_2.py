import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
A = Transition(label='Site Survey')
B = Transition(label='Load Test')
C = Transition(label='Soil Sample')
D = Transition(label='Water Check')
E = Transition(label='Design Plan')
F = Transition(label='Bed Setup')
G = Transition(label='Irrigation Install')
H = Transition(label='Climate Setup')
I = Transition(label='Seed Selection')
J = Transition(label='Planting Phase')
K = Transition(label='Pest Control')
L = Transition(label='Growth Monitor')
M = Transition(label='Harvest Prep')
N = Transition(label='Community Meet')
O = Transition(label='Waste Manage')
P = Transition(label='Yield Report')

# Define the partial order
root = StrictPartialOrder(
    nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P],
    order={
        A: [B, C, D],
        B: [E],
        C: [E],
        D: [E],
        E: [F, G, H, I, J, K, L, M, N, O, P],
        F: [J, K, L, M, N, O, P],
        G: [J, K, L, M, N, O, P],
        H: [J, K, L, M, N, O, P],
        I: [J, K, L, M, N, O, P],
        J: [L, M, N, O, P],
        K: [L, M, N, O, P],
        L: [M, N, O, P],
        M: [N, O, P],
        N: [O, P],
        O: [P],
        P: []
    }
)