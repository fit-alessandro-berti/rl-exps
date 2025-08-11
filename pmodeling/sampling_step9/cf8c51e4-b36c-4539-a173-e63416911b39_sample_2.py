import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Site Analysis')
B = Transition(label='Zoning Approval')
C = Transition(label='Structural Check')
D = Transition(label='Building Retrofit')
E = Transition(label='Hydroponic Setup')
F = Transition(label='Climate Control')
G = Transition(label='Nutrient Design')
H = Transition(label='Staff Hiring')
I = Transition(label='Staff Training')
J = Transition(label='Software Install')
K = Transition(label='System Testing')
L = Transition(label='Crop Planting')
M = Transition(label='Growth Monitor')
N = Transition(label='Pest Control')
O = Transition(label='Harvest Plan')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, skip)