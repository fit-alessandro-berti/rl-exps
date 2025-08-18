from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
inquiry = Transition(label='Inquiry Intake')
consultation = Transition(label='Consultation Call')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
match = Transition(label='Artist Match')
sourcing = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
approve = Transition(label='Milestone Approve')
audit = Transition(label='Quality Audit')
transfer = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Define the partial order with the defined activities
root = StrictPartialOrder(nodes=[inquiry, consultation, concept, feedback, contract, match, sourcing, ethics, progress, approve, audit, transfer, packaging, shipping, post_delivery, survey])

# Define the order dependencies between the activities
root.order.add_edge(inquiry, consultation)
root.order.add_edge(consultation, concept)
root.order.add_edge(concept, feedback)
root.order.add_edge(feedback, contract)
root.order.add_edge(contract, match)
root.order.add_edge(match, sourcing)
root.order.add_edge(sourcing, ethics)
root.order.add_edge(ethics, progress)
root.order.add_edge(progress, approve)
root.order.add_edge(approve, audit)
root.order.add_edge(audit, transfer)
root.order.add_edge(transfer, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, post_delivery)
root.order.add_edge(post_delivery, survey)

# Print the root model
print(root)