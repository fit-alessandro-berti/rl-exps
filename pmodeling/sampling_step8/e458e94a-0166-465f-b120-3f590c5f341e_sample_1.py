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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the POWL model
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[concept_draft, feedback_cycle])
xor_payment = OperatorPOWL(operator=Operator.XOR, children=[payment_schedule, skip])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
xor_frame = OperatorPOWL(operator=Operator.XOR, children=[frame_selection, skip])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor_shipment = OperatorPOWL(operator=Operator.XOR, children=[shipment_arrange, skip])
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, skip])
xor_revision = OperatorPOWL(operator=Operator.XOR, children=[revision_manage, skip])
xor_delay = OperatorPOWL(operator=Operator.XOR, children=[delay_mitigate, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[inquiry_review, client_onboard, loop_feedback, xor_payment, xor_material, xor_frame, xor_packaging, xor_shipment, xor_delivery, xor_revision, xor_delay])
root.order.add_edge(inquiry_review, client_onboard)
root.order.add_edge(client_onboard, loop_feedback)
root.order.add_edge(loop_feedback, xor_payment)
root.order.add_edge(xor_payment, xor_material)
root.order.add_edge(xor_material, xor_frame)
root.order.add_edge(xor_frame, xor_packaging)
root.order.add_edge(xor_packaging, xor_shipment)
root.order.add_edge(xor_shipment, xor_delivery)
root.order.add_edge(xor_delivery, xor_revision)
root.order.add_edge(xor_revision, xor_delay)