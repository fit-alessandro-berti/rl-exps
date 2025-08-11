import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop and partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[consultation_call, feedback_loop])
partial_order = StrictPartialOrder(nodes=[loop, contract_setup, artist_match, material_sourcing, ethics_review, progress_check, milestone_approve, quality_audit, copyright_transfer, packaging_plan, shipping_arrange, post_delivery, client_survey])
partial_order.order.add_edge(loop, contract_setup)
partial_order.order.add_edge(contract_setup, artist_match)
partial_order.order.add_edge(artist_match, material_sourcing)
partial_order.order.add_edge(material_sourcing, ethics_review)
partial_order.order.add_edge(ethics_review, progress_check)
partial_order.order.add_edge(progress_check, milestone_approve)
partial_order.order.add_edge(milestone_approve, quality_audit)
partial_order.order.add_edge(quality_audit, copyright_transfer)
partial_order.order.add_edge(copyright_transfer, packaging_plan)
partial_order.order.add_edge(packaging_plan, shipping_arrange)
partial_order.order.add_edge(shipping_arrange, post_delivery)
partial_order.order.add_edge(post_delivery, client_survey)

# Set the root
root = partial_order