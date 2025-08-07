import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
inquiry = Transition(label='Inquiry Intake')
consult = Transition(label='Consultation Call')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
artist = Transition(label='Artist Match')
source = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
quality = Transition(label='Quality Audit')
copyright = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Loop for iterative feedback
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[feedback, feedback])

# Build the partial order
root = StrictPartialOrder(nodes=[
    inquiry, consult, concept, loop_feedback,
    contract, artist, source, ethics,
    progress, milestone, quality,
    copyright, packaging, shipping, post_delivery, survey
])

# Define the control-flow dependencies
root.order.add_edge(inquiry, consult)
root.order.add_edge(consult, concept)
root.order.add_edge(concept, loop_feedback)
root.order.add_edge(loop_feedback, concept)  # loop back to concept for more feedback

root.order.add_edge(contract, artist)
root.order.add_edge(contract, source)
root.order.add_edge(contract, ethics)

root.order.add_edge(artist, progress)
root.order.add_edge(source, progress)
root.order.add_edge(ethics, progress)

root.order.add_edge(progress, milestone)
root.order.add_edge(milestone, quality)

root.order.add_edge(quality, copyright)
root.order.add_edge(copyright, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, post_delivery)
root.order.add_edge(post_delivery, survey)

print(root)