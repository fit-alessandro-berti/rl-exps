import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Customer searches for ticket')
B = Transition(label='Select route')
C = Transition(label='Select date and time')
D = Transition(label='Provide personal information')
E = Transition(label='Provide payment details')
F = Transition(label='Generate ticket')
G = Transition(label='Send ticket via email')
H = Transition(label='Send ticket via SMS')
I = Transition(label='Update seat inventory')
J = Transition(label='Customer completes journey')
K = Transition(label='Send instructions')
L = Transition(label='Send reminder')
M = Transition(label='Post-travel feedback or services')

# Define silent transitions
skip = SilentTransition()

# Define process steps
step1 = OperatorPOWL(operator=Operator.XOR, children=[A, B])
step2 = OperatorPOWL(operator=Operator.XOR, children=[C, skip])
step3 = OperatorPOWL(operator=Operator.XOR, children=[D, skip])
step4 = OperatorPOWL(operator=Operator.XOR, children=[E, skip])
step5 = OperatorPOWL(operator=Operator.XOR, children=[F, skip])
step6 = OperatorPOWL(operator=Operator.XOR, children=[G, H])
step7 = OperatorPOWL(operator=Operator.XOR, children=[I, skip])
step8 = OperatorPOWL(operator=Operator.XOR, children=[J, skip])
step9 = OperatorPOWL(operator=Operator.XOR, children=[K, L])
step10 = OperatorPOWL(operator=Operator.XOR, children=[M, skip])

# Define partial order
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5, step6, step7, step8, step9, step10])
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)
root.order.add_edge(step6, step7)
root.order.add_edge(step7, step8)
root.order.add_edge(step8, step9)
root.order.add_edge(step9, step10)

# Print the result
print(root)