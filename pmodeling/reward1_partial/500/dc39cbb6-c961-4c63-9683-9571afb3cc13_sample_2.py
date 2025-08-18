import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_sketch, client_feedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[revision_cycle, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[invoice_issue, shipment_prep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, post_support])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[license_setup, frame_arrange])

root = StrictPartialOrder(nodes=[client_inquiry, requirement_gather, loop, xor, final_approval, art_creation, progress_update, quality_check, final_adjust, xor2, invoice_issue, shipment_prep, delivery_confirm, xor3, post_support, xor4, license_setup, frame_arrange])
root.order.add_edge(client_inquiry, requirement_gather)
root.order.add_edge(requirement_gather, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, final_approval)
root.order.add_edge(final_approval, art_creation)
root.order.add_edge(art_creation, progress_update)
root.order.add_edge(progress_update, quality_check)
root.order.add_edge(quality_check, final_adjust)
root.order.add_edge(final_adjust, xor2)
root.order.add_edge(xor2, invoice_issue)
root.order.add_edge(invoice_issue, shipment_prep)
root.order.add_edge(shipment_prep, delivery_confirm)
root.order.add_edge(delivery_confirm, xor3)
root.order.add_edge(xor3, post_support)
root.order.add_edge(post_support, xor4)
root.order.add_edge(xor4, license_setup)
root.order.add_edge(license_setup, frame_arrange)

print(root)