import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for the material sampling process
loop_sampling = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test, historical_match, expert_consult, forgery_scan, market_survey, value_estimate])

# Define the exclusive choice for the imaging and chemical analysis process
xor_imaging_chemical = OperatorPOWL(operator=Operator.XOR, children=[imaging_capture, chemical_analysis])

# Define the root of the process
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop_sampling, xor_imaging_chemical, certification, digital_archive, final_storage])

# Define the dependencies between the nodes
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, material_sampling)
root.order.add_edge(material_sampling, loop_sampling)
root.order.add_edge(loop_sampling, xor_imaging_chemical)
root.order.add_edge(xor_imaging_chemical, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, final_storage)

print(root)