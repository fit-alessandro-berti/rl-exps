from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
inq_review = Transition(label='Inquiry Review')
client_onboard = Transition(label='Client Onboard')
concept_draft = Transition(label='Concept Draft')
feedback_cycle = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Feedback'), Transition(label='No Feedback')])
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

# Define process
loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_draft, feedback_cycle, material_sourcing, artwork_create, quality_check, frame_selection, packaging_prep, shipment_arrange, delivery_confirm, post_sale_support, revision_manage, delay_mitigate])
root = StrictPartialOrder(nodes=[inq_review, client_onboard, loop])
root.order.add_edge(inq_review, client_onboard)
root.order.add_edge(client_onboard, loop)

print(root)