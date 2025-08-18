from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
inquiry = Transition(label='Inquiry Intake')
consultation = Transition(label='Consultation Call')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
artist_match = Transition(label='Artist Match')
material_sourcing = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
quality = Transition(label='Quality Audit')
copyright = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Create the partial order model
root = StrictPartialOrder(nodes=[inquiry, consultation, concept, feedback, contract, artist_match, material_sourcing, ethics, progress, milestone, quality, copyright, packaging, shipping, post_delivery, survey])

# Define the order of execution
root.order.add_edge(inquiry, consultation)
root.order.add_edge(consultation, concept)
root.order.add_edge(concept, feedback)
root.order.add_edge(feedback, contract)
root.order.add_edge(contract, artist_match)
root.order.add_edge(artist_match, material_sourcing)
root.order.add_edge(material_sourcing, ethics)
root.order.add_edge(ethics, progress)
root.order.add_edge(progress, milestone)
root.order.add_edge(milestone, quality)
root.order.add_edge(quality, copyright)
root.order.add_edge(copyright, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, post_delivery)
root.order.add_edge(post_delivery, survey)

# Print the root to confirm
print(root)