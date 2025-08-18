from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test = Transition(label='Radiocarbon Test')
provenance_review = Transition(label='Provenance Review')
imaging_capture = Transition(label='Imaging Capture')
chemical_analysis = Transition(label='Chemical Analysis')
historical_match = Transition(label='Historical Match')
expert_consult = Transition(label='Expert Consult')
forgeries_scan = Transition(label='Forgery Scan')
market_survey = Transition(label='Market Survey')
value_estimate = Transition(label='Value Estimate')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
final_storage = Transition(label='Final Storage')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test])
loop_history = OperatorPOWL(operator=Operator.LOOP, children=[provenance_review, historical_match])
loop_consult = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, forgeries_scan])
loop_survey = OperatorPOWL(operator=Operator.LOOP, children=[market_survey, value_estimate])
loop_certify = OperatorPOWL(operator=Operator.LOOP, children=[certification, digital_archive, final_storage])

# Define root partial order
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop_material, loop_history, loop_consult, loop_survey, loop_certify])

# Define order dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop_material)
root.order.add_edge(loop_material, loop_history)
root.order.add_edge(loop_history, loop_consult)
root.order.add_edge(loop_consult, loop_survey)
root.order.add_edge(loop_survey, loop_certify)
root.order.add_edge(loop_certify, digital_archive)
root.order.add_edge(loop_certify, final_storage)

print(root)