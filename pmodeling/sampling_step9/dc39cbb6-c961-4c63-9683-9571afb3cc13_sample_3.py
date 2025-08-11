import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[concept_sketch, client_feedback, revision_cycle])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[art_creation, progress_update, quality_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[final_adjust, invoice_issue, shipment_prep])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[delivery_confirm, post_support, license_setup])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[frame_arrange, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

# Save the final result in the variable 'root'
root = root