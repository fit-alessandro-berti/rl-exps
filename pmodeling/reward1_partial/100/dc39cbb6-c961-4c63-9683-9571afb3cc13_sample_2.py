from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the silent transition (no operation)
skip = SilentTransition()

# Define the exclusive choice (xor) between final approval and license setup
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, license_setup])

# Define the loop (revision cycle) for iterative feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback, revision_cycle])

# Define the strict partial order
root = StrictPartialOrder(nodes=[client_inquiry, requirement_gather, concept_sketch, loop, art_creation, progress_update, quality_check, final_adjust, invoice_issue, shipment_prep, delivery_confirm, post_support, xor])

# Define the partial order dependencies
root.order.add_edge(client_inquiry, requirement_gather)
root.order.add_edge(requirement_gather, concept_sketch)
root.order.add_edge(concept_sketch, loop)
root.order.add_edge(loop, art_creation)
root.order.add_edge(art_creation, progress_update)
root.order.add_edge(progress_update, quality_check)
root.order.add_edge(quality_check, final_adjust)
root.order.add_edge(final_adjust, invoice_issue)
root.order.add_edge(invoice_issue, shipment_prep)
root.order.add_edge(shipment_prep, delivery_confirm)
root.order.add_edge(delivery_confirm, post_support)
root.order.add_edge(post_support, xor)

print(root)