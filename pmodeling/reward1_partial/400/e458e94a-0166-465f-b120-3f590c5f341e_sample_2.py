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

# Define silent transition for 'skip'
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_draft, feedback_cycle])
xor = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[artwork_create, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[frame_selection, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[shipment_arrange, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[post_sale_support, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[revision_manage, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[delay_mitigate, skip])

root = StrictPartialOrder(nodes=[inquiry_review, client_onboard, loop, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10])
root.order.add_edge(inquiry_review, client_onboard)
root.order.add_edge(client_onboard, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)

# Print the root model
print(root)