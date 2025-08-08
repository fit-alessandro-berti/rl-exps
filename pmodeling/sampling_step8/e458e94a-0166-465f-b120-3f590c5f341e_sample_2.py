import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the process structure
loop_inquiries = OperatorPOWL(operator=Operator.LOOP, children=[inquiry_review, client_onboard])
xor_concept = OperatorPOWL(operator=Operator.XOR, children=[concept_draft, feedback_cycle])
xor_contract = OperatorPOWL(operator=Operator.XOR, children=[contract_setup, payment_schedule])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, artwork_create])
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_check, frame_selection])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, shipment_arrange])
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, post_sale_support])
xor_revision = OperatorPOWL(operator=Operator.XOR, children=[revision_manage, delay_mitigate])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[
    loop_inquiries, xor_concept, xor_contract, xor_material, xor_quality, xor_packaging, xor_delivery, xor_revision
])
root.order.add_edge(loop_inquiries, xor_concept)
root.order.add_edge(xor_concept, xor_contract)
root.order.add_edge(xor_contract, xor_material)
root.order.add_edge(xor_material, xor_quality)
root.order.add_edge(xor_quality, xor_packaging)
root.order.add_edge(xor_packaging, xor_delivery)
root.order.add_edge(xor_delivery, xor_revision)