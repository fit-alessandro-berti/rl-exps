import pm4py
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
forgery_scan = Transition(label='Forgery Scan')
market_survey = Transition(label='Market Survey')
value_estimate = Transition(label='Value Estimate')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
final_storage = Transition(label='Final Storage')

# Define a loop node for the material sampling and radiocarbon test activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test])

# Define a choice node for the historical match, expert consult, and forgery scan activities
xor = OperatorPOWL(operator=Operator.XOR, children=[historical_match, expert_consult, forgery_scan])

# Define a choice node for the market survey and value estimate activities
xor2 = OperatorPOWL(operator=Operator.XOR, children=[market_survey, value_estimate])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop, xor, xor2, certification, digital_archive, final_storage])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, final_storage)