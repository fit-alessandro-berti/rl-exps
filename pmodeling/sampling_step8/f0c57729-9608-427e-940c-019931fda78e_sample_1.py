import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
inquiry = Transition(label='Inquiry Intake')
consultation = Transition(label='Consultation Call')
concept_draft = Transition(label='Concept Draft')
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
client_survey = Transition(label='Client Survey')

# Define silent transitions (if applicable)
skip = SilentTransition()

# Define loops and choices
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[feedback, skip])
contract_setup = OperatorPOWL(operator=Operator.LOOP, children=[contract, artist_match, material_sourcing, ethics, progress, milestone, quality, copyright, packaging, shipping, post_delivery, client_survey])

# Construct the POWL model
root = StrictPartialOrder(nodes=[inquiry, consultation, concept_draft, feedback_loop, contract_setup])
root.order.add_edge(inquiry, consultation)
root.order.add_edge(consultation, concept_draft)
root.order.add_edge(concept_draft, feedback_loop)
root.order.add_edge(feedback_loop, contract_setup)

# Print the POWL model
print(root)