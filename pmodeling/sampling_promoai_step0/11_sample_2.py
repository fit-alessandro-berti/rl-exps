import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the activities
A = Transition(label='Assign access')
B = Transition(label='Customer signs up')
C = Transition(label='Customer submits cancellation request')
D = Transition(label='Deactivate subscription')
E = Transition(label='Generate account')
F = Transition(label='Send product enhancements')
G = Transition(label='Send regular updates')
H = Transition(label='Send renewal notifications')
I = Transition(label='Set automatic triggers for billing cycles')
J = Transition(label='Settle final account balance')
K = Transition(label='apply charges')
L = Transition(label='apply refund')

# Define the transitions
T1 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[B, I])
T2 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[D, K])
T3 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[L, J])
T4 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[G])
T5 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[H])
T6 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[F, T4])
T7 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[T5, T6])
T8 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[T3, T7])
T9 = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[T2, T8])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[T1, T2, T3, T4, T5, T6, T7, T8, T9])
root.order.add_edge(T1, T2)
root.order.add_edge(T1, T3)
root.order.add_edge(T2, T4)
root.order.add_edge(T2, T5)
root.order.add_edge(T3, T6)
root.order.add_edge(T3, T7)
root.order.add_edge(T4, T8)
root.order.add_edge(T5, T8)
root.order.add_edge(T6, T8)
root.order.add_edge(T7, T8)

# Print the root to verify
print(root)