import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
A = Transition(label='Site Survey')
B = Transition(label='Design Layout')
C = Transition(label='Module Build')
D = Transition(label='System Install')
E = Transition(label='Water Prep')
F = Transition(label='Seed Selection')
G = Transition(label='Nutrient Mix')
H = Transition(label='Climate Setup')
I = Transition(label='Sensor Deploy')
J = Transition(label='Pest Scan')
K = Transition(label='Growth Monitor')
L = Transition(label='Data Sync')
M = Transition(label='Energy Manage')
N = Transition(label='Harvest Plan')
O = Transition(label='Community Link')

# Define the structure of the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[E, F, G, H, I, J, K, L, M, N, O])
xor = OperatorPOWL(operator=Operator.XOR, children=[A, B, C, D])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[xor, loop])
root.order.add_edge(xor, loop)