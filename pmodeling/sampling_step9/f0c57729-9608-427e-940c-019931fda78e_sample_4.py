import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
inquiry_intake = Transition(label='Inquiry Intake')
consultation_call = Transition(label='Consultation Call')
concept_draft = Transition(label='Concept Draft')
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Client Feedback'), Transition(label='Artist Feedback')])
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

# Define partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[inquiry_intake, consultation_call, concept_draft, feedback_loop, contract_setup, artist_match, material_sourcing, ethics_review, progress_check, milestone_approve, quality_audit, copyright_transfer, packaging_plan, shipping_arrange, post_delivery, client_survey])
skip = SilentTransition()

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, feedback_loop)
root.order.add_edge(loop, contract_setup)
root.order.add_edge(loop, artist_match)
root.order.add_edge(loop, material_sourcing)
root.order.add_edge(loop, ethics_review)
root.order.add_edge(loop, progress_check)
root.order.add_edge(loop, milestone_approve)
root.order.add_edge(loop, quality_audit)
root.order.add_edge(loop, copyright_transfer)
root.order.add_edge(loop, packaging_plan)
root.order.add_edge(loop, shipping_arrange)
root.order.add_edge(loop, post_delivery)
root.order.add_edge(loop, client_survey)