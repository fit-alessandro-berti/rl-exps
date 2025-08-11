import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Farm Selection')
B = Transition(label='Sample Testing')
C = Transition(label='Trade Negotiation')
D = Transition(label='Micro-Lot Sorting')
E = Transition(label='Fermentation Control')
F = Transition(label='Sensory Profiling')
G = Transition(label='Roast Calibration')
H = Transition(label='Blend Creation')
I = Transition(label='Sustainability Audit')
J = Transition(label='Packaging Design')
K = Transition(label='Quality Inspection')
L = Transition(label='Inventory Sync')
M = Transition(label='Logistics Planning')
N = Transition(label='Cafe Training')
O = Transition(label='Dynamic Pricing')
P = Transition(label='Customer Feedback')
Q = Transition(label='Traceability Logging')
R = OperatorPOWL(operator=Operator.LOOP, children=[A, B])
S = OperatorPOWL(operator=Operator.LOOP, children=[C, D, E, F, G, H, I])
T = OperatorPOWL(operator=Operator.LOOP, children=[J, K])
U = OperatorPOWL(operator=Operator.LOOP, children=[L, M, N])
V = OperatorPOWL(operator=Operator.LOOP, children=[O, P, Q])
root = StrictPartialOrder(nodes=[R, S, T, U, V])

# Add the edges between the loops
root.order.add_edge(R, S)
root.order.add_edge(R, T)
root.order.add_edge(R, U)
root.order.add_edge(R, V)
root.order.add_edge(S, T)
root.order.add_edge(S, U)
root.order.add_edge(S, V)
root.order.add_edge(T, U)
root.order.add_edge(T, V)
root.order.add_edge(U, V)

print(root)