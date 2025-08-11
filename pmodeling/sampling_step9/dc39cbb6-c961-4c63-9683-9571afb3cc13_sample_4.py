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

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[req_gather, concept_sketch, client_feedback, revision_cycle, final_approval])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[art_creation, progress_update, quality_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[final_adjust, invoice_issue, shipment_prep, delivery_confirm])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[post_support, license_setup, frame_arrange])

# Define the root of the workflow
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)

# Print the root of the workflow
print(root)