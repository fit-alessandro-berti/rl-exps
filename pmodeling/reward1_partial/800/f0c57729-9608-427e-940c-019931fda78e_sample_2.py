import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[consultation_call, concept_draft, feedback_loop])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[contract_setup, artist_match, material_sourcing, ethics_review])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[progress_check, milestone_approve, quality_audit, copyright_transfer])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_plan, shipping_arrange])
xor = OperatorPOWL(operator=Operator.XOR, children=[post_delivery, client_survey])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, xor)