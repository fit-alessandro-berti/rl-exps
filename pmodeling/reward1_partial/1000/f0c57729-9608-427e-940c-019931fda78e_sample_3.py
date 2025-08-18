import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
inquiry = Transition(label='Inquiry Intake')
consultation = Transition(label='Consultation Call')
draft = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
match = Transition(label='Artist Match')
sourcing = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
quality = Transition(label='Quality Audit')
copyright = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    inquiry, 
    consultation, 
    draft, 
    feedback, 
    contract, 
    match, 
    sourcing, 
    ethics, 
    progress, 
    milestone, 
    quality, 
    copyright, 
    packaging, 
    shipping, 
    post_delivery, 
    survey
])

# Define the partial order dependencies
root.order.add_edge(inquiry, consultation)
root.order.add_edge(consultation, draft)
root.order.add_edge(draft, feedback)
root.order.add_edge(feedback, contract)
root.order.add_edge(contract, match)
root.order.add_edge(match, sourcing)
root.order.add_edge(sourcing, ethics)
root.order.add_edge(ethics, progress)
root.order.add_edge(progress, milestone)
root.order.add_edge(milestone, quality)
root.order.add_edge(quality, copyright)
root.order.add_edge(copyright, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, post_delivery)
root.order.add_edge(post_delivery, survey)