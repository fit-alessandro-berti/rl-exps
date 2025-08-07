import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
client_inq    = Transition(label='Client Inquiry')
requirement   = Transition(label='Requirement Gather')
concept       = Transition(label='Concept Sketch')
feedback      = Transition(label='Client Feedback')
revision      = Transition(label='Revision Cycle')
final_approval= Transition(label='Final Approval')
art_creation  = Transition(label='Art Creation')
progress      = Transition(label='Progress Update')
quality       = Transition(label='Quality Check')
final_adjust  = Transition(label='Final Adjust')
invoice       = Transition(label='Invoice Issue')
shipment      = Transition(label='Shipment Prep')
delivery      = Transition(label='Delivery Confirm')
post_support  = Transition(label='Post Support')
license       = Transition(label='License Setup')
frame         = Transition(label='Frame Arrange')

# Loop for iterative feedback and revision
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback, revision])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    client_inq, requirement, concept,
    feedback_loop, final_approval,
    art_creation, progress, quality,
    final_adjust, invoice, shipment,
    delivery, post_support, license, frame
])

# Define the control‐flow dependencies
root.order.add_edge(client_inq, requirement)
root.order.add_edge(requirement, concept)

# Feedback and revision cycle
root.order.add_edge(concept, feedback_loop)
root.order.add_edge(feedback_loop, concept)

# Final approval after feedback cycle
root.order.add_edge(feedback_loop, final_approval)

# Art creation and subsequent stages
root.order.add_edge(final_approval, art_creation)
root.order.add_edge(art_creation, progress)
root.order.add_edge(progress, quality)
root.order.add_edge(quality, final_adjust)

# Final stages: invoice, shipment, delivery, post‐support
root.order.add_edge(final_adjust, invoice)
root.order.add_edge(invoice, shipment)
root.order.add_edge(shipment, delivery)
root.order.add_edge(delivery, post_support)

# Optional licensing and framing after delivery
root.order.add_edge(post_support, license)
root.order.add_edge(post_support, frame)