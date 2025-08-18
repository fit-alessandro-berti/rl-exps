import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
client_inquiry = Transition(label='Client Inquiry')
req_gather = Transition(label='Requirement Gather')
concept_sketch = Transition(label='Concept Sketch')
client_feedback = Transition(label='Client Feedback')
revision_cycle = Transition(label='Revision Cycle')
final_approval = Transition(label='Final Approval')
art_creation = Transition(label='Art Creation')
progress_update = Transition(label='Progress Update')
quality_check = Transition(label='Quality Check')
final_adjust = Transition(label='Final Adjust')
invoice_issue = Transition(label='Invoice Issue')
shipment_prep = Transition(label='Shipment Prep')
delivery_confirm = Transition(label='Delivery Confirm')
post_support = Transition(label='Post Support')
license_setup = Transition(label='License Setup')
frame_arrange = Transition(label='Frame Arrange')

# Define the process structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, client_feedback])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[revision_cycle, client_inquiry])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[concept_sketch, req_gather])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[art_creation, quality_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[progress_update, final_adjust])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[invoice_issue, shipment_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, post_support])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[license_setup, frame_arrange])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor1, xor8)

# Print the POWL model
print(root)