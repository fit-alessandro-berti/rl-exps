import pm4py
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    inquiry_intake,
    consultation_call,
    concept_draft,
    feedback_loop,
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
    client_survey
])

# Since there are no dependencies mentioned in the problem, we assume all activities are concurrent
# Therefore, there are no edges to add in the partial order

print(root)