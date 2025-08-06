import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
inq_review = Transition(label='Inquiry Review')
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

# Define silent transitions for no-operation
skip = SilentTransition()

# Define exclusive choice for feedback cycle
xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_cycle, skip])

# Define loop for payment schedule
loop = OperatorPOWL(operator=Operator.LOOP, children=[payment_schedule, material_sourcing])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[inq_review, client_onboard, concept_draft, loop, xor, contract_setup, artwork_create, quality_check, frame_selection, packaging_prep, shipment_arrange, delivery_confirm, post_sale_support, revision_manage, delay_mitigate])

# Add dependencies between nodes
root.order.add_edge(inq_review, client_onboard)
root.order.add_edge(client_onboard, concept_draft)
root.order.add_edge(concept_draft, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, contract_setup)
root.order.add_edge(contract_setup, artwork_create)
root.order.add_edge(artwork_create, quality_check)
root.order.add_edge(quality_check, frame_selection)
root.order.add_edge(frame_selection, packaging_prep)
root.order.add_edge(packaging_prep, shipment_arrange)
root.order.add_edge(shipment_arrange, delivery_confirm)
root.order.add_edge(delivery_confirm, post_sale_support)
root.order.add_edge(post_sale_support, revision_manage)
root.order.add_edge(revision_manage, delay_mitigate)

# Print the POWL model
print(root)