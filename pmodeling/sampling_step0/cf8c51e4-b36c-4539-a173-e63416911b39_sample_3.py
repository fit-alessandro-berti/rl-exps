import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[A, B, C, D])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[E, F, G])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[H, I, J, K, xor1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[L, M, N, O])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor2)

# Return the root
return root