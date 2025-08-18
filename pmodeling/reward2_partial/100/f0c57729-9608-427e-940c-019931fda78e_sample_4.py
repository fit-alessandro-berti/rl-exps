from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
inquiry_intake = Transition(label='Inquiry Intake')
consultation_call = Transition(label='Consultation Call')
concept_draft = Transition(label='Concept Draft')
feedback_loop = Transition(label='Feedback Loop')
contract_setup = Transition(label='Contract Setup')
artist_match = Transition(label='Artist Match')
material_sourcing = Transition(label='Material Sourcing')
ethics_review = Transition(label='Ethics Review')
progress_check = Transition(label='Progress Check')
milestone_approve = Transition(label='Milestone Approve')
quality_audit = Transition(label='Quality Audit')
copyright_transfer = Transition(label='Copyright Transfer')
packaging_plan = Transition(label='Packaging Plan')
shipping_arrange = Transition(label='Shipping Arrange')
post_delivery = Transition(label='Post Delivery')
client_survey = Transition(label='Client Survey')

# Define the partial order with the specified activities
root = StrictPartialOrder(nodes=[inquiry_intake, consultation_call, concept_draft, feedback_loop, contract_setup, artist_match, material_sourcing, ethics_review, progress_check, milestone_approve, quality_audit, copyright_transfer, packaging_plan, shipping_arrange, post_delivery, client_survey])

# Define the dependencies (edges) between the activities
root.order.add_edge(inquiry_intake, consultation_call)
root.order.add_edge(consultation_call, concept_draft)
root.order.add_edge(concept_draft, feedback_loop)
root.order.add_edge(feedback_loop, contract_setup)
root.order.add_edge(contract_setup, artist_match)
root.order.add_edge(artist_match, material_sourcing)
root.order.add_edge(material_sourcing, ethics_review)
root.order.add_edge(ethics_review, progress_check)
root.order.add_edge(progress_check, milestone_approve)
root.order.add_edge(milestone_approve, quality_audit)
root.order.add_edge(quality_audit, copyright_transfer)
root.order.add_edge(copyright_transfer, packaging_plan)
root.order.add_edge(packaging_plan, shipping_arrange)
root.order.add_edge(shipping_arrange, post_delivery)
root.order.add_edge(post_delivery, client_survey)