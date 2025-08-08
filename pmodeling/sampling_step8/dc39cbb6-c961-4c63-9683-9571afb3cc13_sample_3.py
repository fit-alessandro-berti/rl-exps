import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
# Define the activities
client_inquiry = Transition(label='Client Inquiry')
requirement_gather = Transition(label='Requirement Gather')
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[revision_cycle, final_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, concept_sketch])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[concept_sketch, client_inquiry])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[license_setup, frame_arrange])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[frame_arrange, client_inquiry])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, art_creation, progress_update, quality_check, final_adjust, invoice_issue, shipment_prep, delivery_confirm, post_support, xor4, xor5])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(art_creation, progress_update)
root.order.add_edge(progress_update, quality_check)
root.order.add_edge(quality_check, final_adjust)
root.order.add_edge(final_adjust, invoice_issue)
root.order.add_edge(invoice_issue, shipment_prep)
root.order.add_edge(shipment_prep, delivery_confirm)
root.order.add_edge(delivery_confirm, post_support)
root.order.add_edge(post_support, xor4)
root.order.add_edge(xor4, xor5)

# Print the root of the POWL model
print(root)