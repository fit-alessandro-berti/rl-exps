import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[revision_manage, delay_mitigate])
loop = OperatorPOWL(operator=Operator.LOOP, children=[artwork_create, quality_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[client_onboard, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[contract_setup, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[payment_schedule, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[frame_selection, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[shipment_arrange, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[post_sale_support, skip])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[
    inquiry_review, client_onboard, concept_draft, feedback_cycle, contract_setup, payment_schedule, material_sourcing,
    artwork_create, quality_check, frame_selection, packaging_prep, shipment_arrange, delivery_confirm, post_sale_support,
    revision_manage, delay_mitigate, xor, loop, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10
])

# Define dependencies
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

# Add dependencies for loop and XOR operations
root.order.add_edge(artwork_create, quality_check)
root.order.add_edge(quality_check, artwork_create)
root.order.add_edge(client_onboard, skip)
root.order.add_edge(skip, client_onboard)
root.order.add_edge(contract_setup, skip)
root.order.add_edge(skip, contract_setup)
root.order.add_edge(payment_schedule, skip)
root.order.add_edge(skip, payment_schedule)
root.order.add_edge(material_sourcing, skip)
root.order.add_edge(skip, material_sourcing)
root.order.add_edge(frame_selection, skip)
root.order.add_edge(skip, frame_selection)
root.order.add_edge(packaging_prep, skip)
root.order.add_edge(skip, packaging_prep)
root.order.add_edge(shipment_arrange, skip)
root.order.add_edge(skip, shipment_arrange)
root.order.add_edge(delivery_confirm, skip)
root.order.add_edge(skip, delivery_confirm)
root.order.add_edge(post_sale_support, skip)
root.order.add_edge(skip, post_sale_support)

print(root)