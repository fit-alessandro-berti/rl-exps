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

# Define silent transitions
skip = SilentTransition()

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test, provenance_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[imaging_capture, chemical_analysis, historical_match])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, forgery_scan, market_survey])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, certification])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, final_storage])

# Create the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop1, loop2, loop3, xor1, xor2])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor1, xor2)

print(root)