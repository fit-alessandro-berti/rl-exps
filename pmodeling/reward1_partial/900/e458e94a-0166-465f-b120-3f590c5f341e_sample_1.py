import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define transitions
skip = SilentTransition()
loop_inquiry_review = OperatorPOWL(operator=Operator.LOOP, children=[inquiry_review])
xor_client_onboard = OperatorPOWL(operator=Operator.XOR, children=[client_onboard, skip])
xor_concept_draft = OperatorPOWL(operator=Operator.XOR, children=[concept_draft, skip])
xor_feedback_cycle = OperatorPOWL(operator=Operator.XOR, children=[feedback_cycle, skip])
xor_contract_setup = OperatorPOWL(operator=Operator.XOR, children=[contract_setup, skip])
xor_payment_schedule = OperatorPOWL(operator=Operator.XOR, children=[payment_schedule, skip])
xor_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
xor_artwork_create = OperatorPOWL(operator=Operator.XOR, children=[artwork_create, skip])
xor_quality_check = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
xor_frame_selection = OperatorPOWL(operator=Operator.XOR, children=[frame_selection, skip])
xor_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor_shipment_arrange = OperatorPOWL(operator=Operator.XOR, children=[shipment_arrange, skip])
xor_delivery_confirm = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, skip])
xor_post_sale_support = OperatorPOWL(operator=Operator.XOR, children=[post_sale_support, skip])
xor_revision_manage = OperatorPOWL(operator=Operator.XOR, children=[revision_manage, skip])
xor_delay_mitigate = OperatorPOWL(operator=Operator.XOR, children=[delay_mitigate, skip])

# Create root POWL model
root = StrictPartialOrder(nodes=[
    loop_inquiry_review,
    xor_client_onboard,
    xor_concept_draft,
    xor_feedback_cycle,
    xor_contract_setup,
    xor_payment_schedule,
    xor_material_sourcing,
    xor_artwork_create,
    xor_quality_check,
    xor_frame_selection,
    xor_packaging_prep,
    xor_shipment_arrange,
    xor_delivery_confirm,
    xor_post_sale_support,
    xor_revision_manage,
    xor_delay_mitigate
])

# Define order dependencies
root.order.add_edge(loop_inquiry_review, xor_client_onboard)
root.order.add_edge(xor_client_onboard, xor_concept_draft)
root.order.add_edge(xor_concept_draft, xor_feedback_cycle)
root.order.add_edge(xor_feedback_cycle, xor_contract_setup)
root.order.add_edge(xor_contract_setup, xor_payment_schedule)
root.order.add_edge(xor_payment_schedule, xor_material_sourcing)
root.order.add_edge(xor_material_sourcing, xor_artwork_create)
root.order.add_edge(xor_artwork_create, xor_quality_check)
root.order.add_edge(xor_quality_check, xor_frame_selection)
root.order.add_edge(xor_frame_selection, xor_packaging_prep)
root.order.add_edge(xor_packaging_prep, xor_shipment_arrange)
root.order.add_edge(xor_shipment_arrange, xor_delivery_confirm)
root.order.add_edge(xor_delivery_confirm, xor_post_sale_support)
root.order.add_edge(xor_post_sale_support, xor_revision_manage)
root.order.add_edge(xor_revision_manage, xor_delay_mitigate)

# Print the root POWL model
print(root)