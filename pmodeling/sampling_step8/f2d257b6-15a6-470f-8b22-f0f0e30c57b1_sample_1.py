import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_material_sampling = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling])
loop_forgery_scan = OperatorPOWL(operator=Operator.LOOP, children=[forgery_scan])

# Define exclusive choices
xor_radiocarbon_test = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, skip])
xor_historical_match = OperatorPOWL(operator=Operator.XOR, children=[historical_match, skip])
xor_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
xor_market_survey = OperatorPOWL(operator=Operator.XOR, children=[market_survey, skip])
xor_value_estimate = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop_material_sampling, loop_forgery_scan, xor_radiocarbon_test, xor_historical_match, xor_expert_consult, xor_market_survey, xor_value_estimate, certification, digital_archive, final_storage])

# Define the order of execution (dependencies)
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop_material_sampling)
root.order.add_edge(condition_check, loop_forgery_scan)
root.order.add_edge(loop_material_sampling, xor_radiocarbon_test)
root.order.add_edge(loop_forgery_scan, xor_expert_consult)
root.order.add_edge(xor_radiocarbon_test, xor_historical_match)
root.order.add_edge(xor_historical_match, xor_market_survey)
root.order.add_edge(xor_market_survey, xor_value_estimate)
root.order.add_edge(xor_value_estimate, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, final_storage)

print(root)