import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    inquiry_review,
    client_onboard,
    concept_draft,
    feedback_cycle,
    contract_setup,
    payment_schedule,
    material_sourcing,
    artwork_create,
    quality_check,
    frame_selection,
    packaging_prep,
    shipment_arrange,
    delivery_confirm,
    post_sale_support,
    revision_manage,
    delay_mitigate
])

# Define the dependencies between transitions
root.order.add_edge(inquiry_review, client_onboard)
root.order.add_edge(client_onboard, concept_draft)
root.order.add_edge(concept_draft, feedback_cycle)
root.order.add_edge(feedback_cycle, contract_setup)
root.order.add_edge(contract_setup, payment_schedule)
root.order.add_edge(payment_schedule, material_sourcing)
root.order.add_edge(material_sourcing, artwork_create)
root.order.add_edge(artwork_create, quality_check)
root.order.add_edge(quality_check, frame_selection)
root.order.add_edge(frame_selection, packaging_prep)
root.order.add_edge(packaging_prep, shipment_arrange)
root.order.add_edge(shipment_arrange, delivery_confirm)
root.order.add_edge(delivery_confirm, post_sale_support)
root.order.add_edge(post_sale_support, revision_manage)
root.order.add_edge(revision_manage, delay_mitigate)

# Print the final result
print(root)