import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
inq = Transition(label='Inquiry Review')
onboard = Transition(label='Client Onboard')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Cycle')
contract = Transition(label='Contract Setup')
payment = Transition(label='Payment Schedule')
material = Transition(label='Material Sourcing')
create = Transition(label='Artwork Create')
quality = Transition(label='Quality Check')
frame = Transition(label='Frame Selection')
pack = Transition(label='Packaging Prep')
ship = Transition(label='Shipment Arrange')
confirm = Transition(label='Delivery Confirm')
post = Transition(label='Post-Sale Support')
rev = Transition(label='Revision Manage')
delay = Transition(label='Delay Mitigate')

# Define the iterative feedback loop: do Feedback Cycle, then either exit or do Revision Manage then Feedback Cycle again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback, rev])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    inq, onboard, concept,
    feedback_loop,
    contract, payment, material, create,
    quality, frame, pack, ship, confirm,
    post, rev, delay
])

# Add the control-flow dependencies
root.order.add_edge(inq, onboard)
root.order.add_edge(onboard, concept)
root.order.add_edge(concept, feedback_loop)
root.order.add_edge(feedback_loop, contract)
root.order.add_edge(contract, payment)
root.order.add_edge(payment, material)
root.order.add_edge(material, create)
root.order.add_edge(create, quality)
root.order.add_edge(quality, frame)
root.order.add_edge(frame, pack)
root.order.add_edge(pack, ship)
root.order.add_edge(ship, confirm)
root.order.add_edge(confirm, post)
root.order.add_edge(post, rev)
root.order.add_edge(rev, delay)