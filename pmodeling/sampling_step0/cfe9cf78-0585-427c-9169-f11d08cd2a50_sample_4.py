import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Site Analysis')
B = Transition(label='Env Assessment')
C = Transition(label='System Design')
D = Transition(label='Equipment Order')
E = Transition(label='Seed Selection')
F = Transition(label='Install Modules')
G = Transition(label='Calibrate Systems')
H = Transition(label='Staff Training')
I = Transition(label='Plant Seeding')
J = Transition(label='IoT Monitoring')
K = Transition(label='Data Analytics')
L = Transition(label='Nutrient Adjust')
M = Transition(label='Pest Control')
N = Transition(label='Maintenance Check')
O = Transition(label='Market Launch')
P = Transition(label='Logistics Setup')

# Define the exclusive choice between A and B
X1 = OperatorPOWL(operator=Operator.XOR, children=[A, B])

# Define the loop between F and G
L1 = OperatorPOWL(operator=Operator.LOOP, children=[F, G])

# Define the exclusive choice between H and I
X2 = OperatorPOWL(operator=Operator.XOR, children=[H, I])

# Define the loop between J and K
L2 = OperatorPOWL(operator=Operator.LOOP, children=[J, K])

# Define the exclusive choice between L and M
X3 = OperatorPOWL(operator=Operator.XOR, children=[L, M])

# Define the exclusive choice between N and O
X4 = OperatorPOWL(operator=Operator.XOR, children=[N, O])

# Define the exclusive choice between P and X4
X5 = OperatorPOWL(operator=Operator.XOR, children=[P, X4])

# Define the root POWL model
root = StrictPartialOrder(nodes=[X1, L1, X2, L2, X3, X4, X5])
root.order.add_edge(X1, L1)
root.order.add_edge(L1, X2)
root.order.add_edge(X2, L2)
root.order.add_edge(L2, X3)
root.order.add_edge(X3, X4)
root.order.add_edge(X4, X5)
root.order.add_edge(X5, P)