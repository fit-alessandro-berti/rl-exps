from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

A = Transition(label='Milk Sourcing')
B = Transition(label='Quality Testing')
C = Transition(label='Batch Curdling')
D = Transition(label='Whey Removal')
E = Transition(label='Mold Inoculation')
F = Transition(label='Humidity Control')
G = Transition(label='Temperature Aging')
H = Transition(label='Rind Brushing')
I = Transition(label='Flavor Sampling')
J = Transition(label='Label Printing')
K = Transition(label='Packaging Prep')
L = Transition(label='Cold Storage')
M = Transition(label='Order Consolidation')
N = Transition(label='Logistics Scheduling')
O = Transition(label='Customer Feedback')
P = Transition(label='Certification Audit')
Q = Transition(label='Recipe Adjustment')

# Define nodes
nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q])
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor, P])

# Define the root
root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
print(root)