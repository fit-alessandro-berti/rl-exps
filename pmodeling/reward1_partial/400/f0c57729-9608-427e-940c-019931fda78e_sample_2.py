import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the POWL model
xor_feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, consultation_call])
xor_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, ethics_review])
xor_progress_check = OperatorPOWL(operator=Operator.XOR, children=[progress_check, milestone_approve])
xor_quality_audit = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, copyright_transfer])
xor_packaging_plan = OperatorPOWL(operator=Operator.XOR, children=[packaging_plan, shipping_arrange])
xor_post_delivery = OperatorPOWL(operator=Operator.XOR, children=[post_delivery, client_survey])

root = StrictPartialOrder(nodes=[inquiry_intake, xor_feedback_loop, xor_material_sourcing, xor_progress_check, xor_quality_audit, xor_packaging_plan, xor_post_delivery])
root.order.add_edge(inquiry_intake, xor_feedback_loop)
root.order.add_edge(inquiry_intake, xor_material_sourcing)
root.order.add_edge(inquiry_intake, xor_progress_check)
root.order.add_edge(inquiry_intake, xor_quality_audit)
root.order.add_edge(inquiry_intake, xor_packaging_plan)
root.order.add_edge(inquiry_intake, xor_post_delivery)