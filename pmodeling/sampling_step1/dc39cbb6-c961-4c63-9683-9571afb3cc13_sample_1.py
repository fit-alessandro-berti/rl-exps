import pm4py
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

client_inquiry_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_inquiry, requirement_gather])
concept_sketch_loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_sketch, client_feedback, revision_cycle])
quality_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, final_approval])
invoice_issue_loop = OperatorPOWL(operator=Operator.LOOP, children=[invoice_issue, shipment_prep, delivery_confirm])
post_support_loop = OperatorPOWL(operator=Operator.LOOP, children=[post_support, license_setup, frame_arrange])

root = StrictPartialOrder(nodes=[client_inquiry_loop, concept_sketch_loop, quality_check_loop, invoice_issue_loop, post_support_loop])
root.order.add_edge(client_inquiry_loop, concept_sketch_loop)
root.order.add_edge(concept_sketch_loop, quality_check_loop)
root.order.add_edge(quality_check_loop, invoice_issue_loop)
root.order.add_edge(invoice_issue_loop, post_support_loop)