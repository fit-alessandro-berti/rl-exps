from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

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

# Define the workflow steps using OperatorPOWL
# Client Inquiry -> Requirement Gather
client_inquiry_to_requirement_gather = OperatorPOWL(operator=Operator.PO, children=[client_inquiry, requirement_gather])

# Requirement Gather -> Concept Sketch
requirement_gather_to_concept_sketch = OperatorPOWL(operator=Operator.PO, children=[requirement_gather, concept_sketch])

# Concept Sketch -> Client Feedback
concept_sketch_to_client_feedback = OperatorPOWL(operator=Operator.PO, children=[concept_sketch, client_feedback])

# Client Feedback -> Revision Cycle
client_feedback_to_revision_cycle = OperatorPOWL(operator=Operator.PO, children=[client_feedback, revision_cycle])

# Revision Cycle -> Final Approval
revision_cycle_to_final_approval = OperatorPOWL(operator=Operator.PO, children=[revision_cycle, final_approval])

# Final Approval -> Art Creation
final_approval_to_art_creation = OperatorPOWL(operator=Operator.PO, children=[final_approval, art_creation])

# Art Creation -> Progress Update
art_creation_to_progress_update = OperatorPOWL(operator=Operator.PO, children=[art_creation, progress_update])

# Progress Update -> Quality Check
progress_update_to_quality_check = OperatorPOWL(operator=Operator.PO, children=[progress_update, quality_check])

# Quality Check -> Final Adjust
quality_check_to_final_adjust = OperatorPOWL(operator=Operator.PO, children=[quality_check, final_adjust])

# Final Adjust -> Invoice Issue
final_adjust_to_invoice_issue = OperatorPOWL(operator=Operator.PO, children=[final_adjust, invoice_issue])

# Invoice Issue -> Shipment Prep
invoice_issue_to_shipment_prep = OperatorPOWL(operator=Operator.PO, children=[invoice_issue, shipment_prep])

# Shipment Prep -> Delivery Confirm
shipment_prep_to_delivery_confirm = OperatorPOWL(operator=Operator.PO, children=[shipment_prep, delivery_confirm])

# Delivery Confirm -> Post Support
delivery_confirm_to_post_support = OperatorPOWL(operator=Operator.PO, children=[delivery_confirm, post_support])

# Post Support -> License Setup
post_support_to_license_setup = OperatorPOWL(operator=Operator.PO, children=[post_support, license_setup])

# License Setup -> Frame Arrange
license_setup_to_frame_arrange = OperatorPOWL(operator=Operator.PO, children=[license_setup, frame_arrange])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    client_inquiry_to_requirement_gather,
    requirement_gather_to_concept_sketch,
    concept_sketch_to_client_feedback,
    client_feedback_to_revision_cycle,
    revision_cycle_to_final_approval,
    final_approval_to_art_creation,
    art_creation_to_progress_update,
    progress_update_to_quality_check,
    quality_check_to_final_adjust,
    final_adjust_to_invoice_issue,
    invoice_issue_to_shipment_prep,
    shipment_prep_to_delivery_confirm,
    delivery_confirm_to_post_support,
    post_support_to_license_setup,
    license_setup_to_frame_arrange
])

# Establish dependencies between nodes
root.order.add_edge(client_inquiry_to_requirement_gather, requirement_gather_to_concept_sketch)
root.order.add_edge(requirement_gather_to_concept_sketch, concept_sketch_to_client_feedback)
root.order.add_edge(concept_sketch_to_client_feedback, client_feedback_to_revision_cycle)
root.order.add_edge(client_feedback_to_revision_cycle, revision_cycle_to_final_approval)
root.order.add_edge(revision_cycle_to_final_approval, final_approval_to_art_creation)
root.order.add_edge(final_approval_to_art_creation, art_creation_to_progress_update)
root.order.add_edge(art_creation_to_progress_update, progress_update_to_quality_check)
root.order.add_edge(progress_update_to_quality_check, quality_check_to_final_adjust)
root.order.add_edge(quality_check_to_final_adjust, final_adjust_to_invoice_issue)
root.order.add_edge(final_adjust_to_invoice_issue, invoice_issue_to_shipment_prep)
root.order.add_edge(invoice_issue_to_shipment_prep, shipment_prep_to_delivery_confirm)
root.order.add_edge(shipment_prep_to_delivery_confirm, delivery_confirm_to_post_support)
root.order.add_edge(delivery_confirm_to_post_support, post_support_to_license_setup)
root.order.add_edge(post_support_to_license_setup, license_setup_to_frame_arrange)