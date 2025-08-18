from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

client_feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[revision_cycle, skip])
concept_sketch_xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

art_creation_loop = OperatorPOWL(operator=Operator.LOOP, children=[progress_update, quality_check, final_adjust])

root = StrictPartialOrder(nodes=[client_inquiry, requirement_gather, concept_sketch, client_feedback_xor, art_creation_loop, final_approval, invoice_issue, shipment_prep, delivery_confirm, post_support, license_setup, frame_arrange])
root.order.add_edge(client_inquiry, requirement_gather)
root.order.add_edge(requirement_gather, concept_sketch)
root.order.add_edge(concept_sketch, client_feedback_xor)
root.order.add_edge(client_feedback_xor, art_creation_loop)
root.order.add_edge(art_creation_loop, final_approval)
root.order.add_edge(final_approval, invoice_issue)
root.order.add_edge(invoice_issue, shipment_prep)
root.order.add_edge(shipment_prep, delivery_confirm)
root.order.add_edge(delivery_confirm, post_support)
root.order.add_edge(post_support, license_setup)
root.order.add_edge(license_setup, frame_arrange)