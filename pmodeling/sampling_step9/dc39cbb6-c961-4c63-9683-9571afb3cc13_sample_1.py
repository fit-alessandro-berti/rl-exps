import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for art creation and quality check
loop_art_creation_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[art_creation, quality_check])

# Define the exclusive choice for final approval and revision cycle
exclusive_choice_final_approval_revision_cycle = OperatorPOWL(operator=Operator.XOR, children=[final_approval, revision_cycle])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_art_creation_quality_check, exclusive_choice_final_approval_revision_cycle])

# Define the dependencies between nodes
root.order.add_edge(loop_art_creation_quality_check, exclusive_choice_final_approval_revision_cycle)

# Print the result
print(root)