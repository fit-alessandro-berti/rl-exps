import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
inquiry = Transition(label='Inquiry Intake')
consult = Transition(label='Consultation Call')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
artist_match = Transition(label='Artist Match')
material = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
quality = Transition(label='Quality Audit')
copyright = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
client_survey = Transition(label='Client Survey')

# Build the iterative feedback loop: do Concept Draft, then Feedback Loop until exit
loop_body = StrictPartialOrder(nodes=[concept, feedback])
loop_body.order.add_edge(concept, feedback)

# Build the main partial order
main_po = StrictPartialOrder(nodes=[
    inquiry,
    consult,
    loop_body,
    contract,
    artist_match,
    material,
    ethics,
    progress,
    milestone,
    quality,
    copyright,
    packaging,
    shipping,
    post_delivery,
    client_survey
])

# Add the control-flow edges
main_po.order.add_edge(inquiry, consult)
main_po.order.add_edge(consult, loop_body)
main_po.order.add_edge(loop_body, contract)
main_po.order.add_edge(contract, artist_match)
main_po.order.add_edge(artist_match, material)
main_po.order.add_edge(material, ethics)
main_po.order.add_edge(ethics, progress)
main_po.order.add_edge(progress, milestone)
main_po.order.add_edge(milestone, quality)
main_po.order.add_edge(quality, copyright)
main_po.order.add_edge(copyright, packaging)
main_po.order.add_edge(packaging, shipping)
main_po.order.add_edge(shipping, post_delivery)
main_po.order.add_edge(post_delivery, client_survey)

# Final model: the whole partial order
root = main_po