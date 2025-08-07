import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
client_inquiry     = Transition(label='Client Inquiry')
requirement_gather = Transition(label='Requirement Gather')
concept_sketch     = Transition(label='Concept Sketch')
client_feedback    = Transition(label='Client Feedback')
revision_cycle     = Transition(label='Revision Cycle')
final_approval     = Transition(label='Final Approval')
art_creation       = Transition(label='Art Creation')
progress_update    = Transition(label='Progress Update')
quality_check      = Transition(label='Quality Check')
final_adjust       = Transition(label='Final Adjust')
invoice_issue      = Transition(label='Invoice Issue')
shipment_prep      = Transition(label='Shipment Prep')
delivery_confirm   = Transition(label='Delivery Confirm')
post_support       = Transition(label='Post Support')
license_setup      = Transition(label='License Setup')
frame_arrange      = Transition(label='Frame Arrange')

# Build the partial order
root = StrictPartialOrder(nodes=[
    client_inquiry,
    requirement_gather,
    concept_sketch,
    client_feedback,
    revision_cycle,
    final_approval,
    art_creation,
    progress_update,
    quality_check,
    final_adjust,
    invoice_issue,
    shipment_prep,
    delivery_confirm,
    post_support,
    license_setup,
    frame_arrange
])

# Define the control-flow dependencies
root.order.add_edge(client_inquiry, requirement_gather)
root.order.add_edge(requirement_gather, concept_sketch)

# Client feedback and revision cycle can happen concurrently
root.order.add_edge(concept_sketch, client_feedback)
root.order.add_edge(concept_sketch, revision_cycle)

# Feedback/revision loop: after feedback, either exit or go through revision
root.order.add_edge(client_feedback, revision_cycle)
root.order.add_edge(client_feedback, final_approval)

# Final approval either exits or starts the revision cycle again
root.order.add_edge(final_approval, revision_cycle)
root.order.add_edge(final_approval, final_approval)

# After revision, final approval is the only option
root.order.add_edge(revision_cycle, final_approval)

# After final approval, the art creation process begins
root.order.add_edge(final_approval, art_creation)

# Art creation has a parallel update‐check‐adjust loop
root.order.add_edge(art_creation, progress_update)
root.order.add_edge(art_creation, quality_check)
root.order.add_edge(art_creation, final_adjust)

# After adjustments, either exit or go back to progress update
root.order.add_edge(final_adjust, progress_update)
root.order.add_edge(final_adjust, final_adjust)

# Progress update and quality check can happen concurrently
root.order.add_edge(progress_update, quality_check)

# Quality check either exits or starts the adjustment loop again
root.order.add_edge(quality_check, final_adjust)
root.order.add_edge(quality_check, quality_check)

# After quality check, final adjustment is the only option
root.order.add_edge(quality_check, final_adjust)

# After all adjustments, invoice and shipment prep can start
root.order.add_edge(final_adjust, invoice_issue)
root.order.add_edge(final_adjust, shipment_prep)

# After invoicing, delivery confirmation can happen
root.order.add_edge(invoice_issue, delivery_confirm)

# After delivery, post-sale support can start
root.order.add_edge(delivery_confirm, post_support)

# Post-sale support can optionally include license setup or frame arrange
root.order.add_edge(post_support, license_setup)
root.order.add_edge(post_support, frame_arrange)

# License setup and frame arrange can happen concurrently
root.order.add_edge(license_setup, frame_arrange)