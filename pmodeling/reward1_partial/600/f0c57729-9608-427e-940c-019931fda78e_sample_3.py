from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
inquiry = Transition(label='Inquiry Intake')
consultation = Transition(label='Consultation Call')
draft = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
artist = Transition(label='Artist Match')
material = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
audit = Transition(label='Quality Audit')
transfer = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Define the partial order
root = StrictPartialOrder(nodes=[inquiry, consultation, draft, feedback, contract, artist, material, ethics, progress, milestone, audit, transfer, packaging, shipping, post_delivery, survey])

# Define the partial order edges
root.order.add_edge(inquiry, consultation)
root.order.add_edge(consultation, draft)
root.order.add_edge(draft, feedback)
root.order.add_edge(feedback, contract)
root.order.add_edge(contract, artist)
root.order.add_edge(artist, material)
root.order.add_edge(material, ethics)
root.order.add_edge(ethics, progress)
root.order.add_edge(progress, milestone)
root.order.add_edge(milestone, audit)
root.order.add_edge(audit, transfer)
root.order.add_edge(transfer, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, post_delivery)
root.order.add_edge(post_delivery, survey)

# Print the root to verify the model
print(root)