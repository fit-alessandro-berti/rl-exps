from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the partial order structure
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])
xor_contracts = OperatorPOWL(operator=Operator.XOR, children=[contract_setup, skip])
xor_artist_match = OperatorPOWL(operator=Operator.XOR, children=[artist_match, skip])
xor_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
xor_ethics_review = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
xor_progress_check = OperatorPOWL(operator=Operator.XOR, children=[progress_check, skip])
xor_milestone_approve = OperatorPOWL(operator=Operator.XOR, children=[milestone_approve, skip])
xor_quality_audit = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
xor_copyright_transfer = OperatorPOWL(operator=Operator.XOR, children=[copyright_transfer, skip])
xor_packaging_plan = OperatorPOWL(operator=Operator.XOR, children=[packaging_plan, skip])
xor_shipping_arrange = OperatorPOWL(operator=Operator.XOR, children=[shipping_arrange, skip])
xor_post_delivery = OperatorPOWL(operator=Operator.XOR, children=[post_delivery, skip])
xor_client_survey = OperatorPOWL(operator=Operator.XOR, children=[client_survey, skip])

root = StrictPartialOrder(nodes=[
    inquiry_intake,
    consultation_call,
    concept_draft,
    loop_feedback,
    xor_contracts,
    xor_artist_match,
    xor_material_sourcing,
    xor_ethics_review,
    xor_progress_check,
    xor_milestone_approve,
    xor_quality_audit,
    xor_copyright_transfer,
    xor_packaging_plan,
    xor_shipping_arrange,
    xor_post_delivery,
    xor_client_survey
])

# Add dependencies to the partial order
root.order.add_edge(inquiry_intake, consultation_call)
root.order.add_edge(consultation_call, concept_draft)
root.order.add_edge(concept_draft, loop_feedback)
root.order.add_edge(loop_feedback, xor_contracts)
root.order.add_edge(xor_contracts, xor_artist_match)
root.order.add_edge(xor_artist_match, xor_material_sourcing)
root.order.add_edge(xor_material_sourcing, xor_ethics_review)
root.order.add_edge(xor_ethics_review, xor_progress_check)
root.order.add_edge(xor_progress_check, xor_milestone_approve)
root.order.add_edge(xor_milestone_approve, xor_quality_audit)
root.order.add_edge(xor_quality_audit, xor_copyright_transfer)
root.order.add_edge(xor_copyright_transfer, xor_packaging_plan)
root.order.add_edge(xor_packaging_plan, xor_shipping_arrange)
root.order.add_edge(xor_shipping_arrange, xor_post_delivery)
root.order.add_edge(xor_post_delivery, xor_client_survey)

print(root)