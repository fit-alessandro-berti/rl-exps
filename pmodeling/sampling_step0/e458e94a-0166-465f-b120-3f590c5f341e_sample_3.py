import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
inquiry_review = Transition(label='Inquiry Review')
client_onboard = Transition(label='Client Onboard')
concept_draft = Transition(label='Concept Draft')
feedback_cycle = Transition(label='Feedback Cycle')
contract_setup = Transition(label='Contract Setup')
payment_schedule = Transition(label='Payment Schedule')
material_sourcing = Transition(label='Material Sourcing')
artwork_create = Transition(label='Artwork Create')
quality_check = Transition(label='Quality Check')
frame_selection = Transition(label='Frame Selection')
packaging_prep = Transition(label='Packaging Prep')
shipment_arrange = Transition(label='Shipment Arrange')
delivery_confirm = Transition(label='Delivery Confirm')
post_sale_support = Transition(label='Post-Sale Support')
revision_manage = Transition(label='Revision Manage')
delay_mitigate = Transition(label='Delay Mitigate')

# Define the silent transition (skip)
skip = SilentTransition()

# Define the loop for feedback cycle
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_cycle])

# Define the exclusive choice for contract setup
contract_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_setup, skip])

# Define the exclusive choice for material sourcing
material_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])

# Define the exclusive choice for artwork creation
artwork_create_choice = OperatorPOWL(operator=Operator.XOR, children=[artwork_create, skip])

# Define the exclusive choice for quality check
quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])

# Define the exclusive choice for frame selection
frame_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[frame_selection, skip])

# Define the exclusive choice for packaging preparation
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])

# Define the exclusive choice for shipment arrangement
shipment_arrange_choice = OperatorPOWL(operator=Operator.XOR, children=[shipment_arrange, skip])

# Define the exclusive choice for delivery confirmation
delivery_confirm_choice = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, skip])

# Define the exclusive choice for post-sale support
post_sale_support_choice = OperatorPOWL(operator=Operator.XOR, children=[post_sale_support, skip])

# Define the exclusive choice for revision management
revision_manage_choice = OperatorPOWL(operator=Operator.XOR, children=[revision_manage, skip])

# Define the exclusive choice for delay mitigation
delay_mitigate_choice = OperatorPOWL(operator=Operator.XOR, children=[delay_mitigate, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    inquiry_review,
    client_onboard,
    concept_draft,
    feedback_loop,
    contract_choice,
    material_sourcing_choice,
    artwork_create_choice,
    quality_check_choice,
    frame_selection_choice,
    packaging_prep_choice,
    shipment_arrange_choice,
    delivery_confirm_choice,
    post_sale_support_choice,
    revision_manage_choice,
    delay_mitigate_choice
])

# Add edges to define the partial order
root.order.add_edge(inquiry_review, client_onboard)
root.order.add_edge(client_onboard, concept_draft)
root.order.add_edge(concept_draft, feedback_loop)
root.order.add_edge(feedback_loop, contract_choice)
root.order.add_edge(contract_choice, material_sourcing_choice)
root.order.add_edge(material_sourcing_choice, artwork_create_choice)
root.order.add_edge(artwork_create_choice, quality_check_choice)
root.order.add_edge(quality_check_choice, frame_selection_choice)
root.order.add_edge(frame_selection_choice, packaging_prep_choice)
root.order.add_edge(packaging_prep_choice, shipment_arrange_choice)
root.order.add_edge(shipment_arrange_choice, delivery_confirm_choice)
root.order.add_edge(delivery_confirm_choice, post_sale_support_choice)
root.order.add_edge(post_sale_support_choice, revision_manage_choice)
root.order.add_edge(revision_manage_choice, delay_mitigate_choice)

# Print the root POWL model
print(root)