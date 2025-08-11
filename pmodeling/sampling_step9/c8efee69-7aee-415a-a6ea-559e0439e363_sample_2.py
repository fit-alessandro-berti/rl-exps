import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Milk Sourcing')
B = Transition(label='Quality Testing')
C = Transition(label='Starter Prep')
D = Transition(label='Curd Cutting')
E = Transition(label='Molding Cheese')
F = Transition(label='Salting Process')
G = Transition(label='Aging Control')
H = Transition(label='Humidity Check')
I = Transition(label='Packaging Design')
J = Transition(label='Label Printing')
K = Transition(label='Inventory Audit')
L = Transition(label='Cold Storage')
M = Transition(label='Order Processing')
N = Transition(label='Logistics Planning')
O = Transition(label='Retail Delivery')
P = Transition(label='Consumer Feedback')
Q = Transition(label='Batch Adjustment')
R = Transition(label='Event Coordination')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R])
xor = OperatorPOWL(operator=Operator.XOR, children=[R, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)