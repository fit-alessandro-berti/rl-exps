import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
inquiry_intake = Transition(label='Inquiry Intake')
consultation_call = Transition(label='Consultation Call')
concept_draft = Transition(label='Concept Draft')
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[concept_draft, SilentTransition()])
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

# Define the loop for the feedback loop
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])

# Define the process tree
process_tree = StrictPartialOrder(nodes=[
    inquiry_intake,
    consultation_call,
    contract_setup,
    artist_match,
    material_sourcing,
    ethics_review,
    progress_check,
    milestone_approve,
    quality_audit,
    copyright_transfer,
    packaging_plan,
    shipping_arrange,
    post_delivery,
    client_survey,
    feedback_loop_loop
])

# Add the dependencies between the nodes
process_tree.order.add_edge(inquiry_intake, consultation_call)
process_tree.order.add_edge(consultation_call, contract_setup)
process_tree.order.add_edge(contract_setup, artist_match)
process_tree.order.add_edge(artist_match, material_sourcing)
process_tree.order.add_edge(material_sourcing, ethics_review)
process_tree.order.add_edge(ethics_review, progress_check)
process_tree.order.add_edge(progress_check, milestone_approve)
process_tree.order.add_edge(milestone_approve, quality_audit)
process_tree.order.add_edge(quality_audit, copyright_transfer)
process_tree.order.add_edge(copyright_transfer, packaging_plan)
process_tree.order.add_edge(packaging_plan, shipping_arrange)
process_tree.order.add_edge(shipping_arrange, post_delivery)
process_tree.order.add_edge(post_delivery, client_survey)
process_tree.order.add_edge(client_survey, feedback_loop_loop)
process_tree.order.add_edge(feedback_loop_loop, concept_draft)

# Save the root of the POWL model
root = process_tree