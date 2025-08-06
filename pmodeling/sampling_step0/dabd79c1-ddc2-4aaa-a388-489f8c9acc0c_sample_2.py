import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Document Review', 'Material Testing', 'Radiocarbon Date', 'Stylistic Eval', 'Database Check', 'Ownership Audit', 'Export Verify', 'Expert Arbitration', 'Conservation Plan', 'Risk Assessment', 'Approval Review', 'Insurance Setup', 'Secure Transport', 'Acquisitions Meet', 'Final Documentation']

# Create the transitions for the activities
transitions = [Transition(label=activity) for activity in activities]

# Create the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[transitions[0], transitions[1]])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transitions[2], transitions[3]])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[transitions[4], transitions[5]])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transitions[6], transitions[7]])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[transitions[8], transitions[9]])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[transitions[10], transitions[11]])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[transitions[12], transitions[13]])

# Create the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)