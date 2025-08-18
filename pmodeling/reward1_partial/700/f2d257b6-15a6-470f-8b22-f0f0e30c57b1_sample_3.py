import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the process model
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, condition_check, material_sampling, radiocarbon_test, provenance_review, imaging_capture, chemical_analysis, historical_match, expert_consult, forgeries_scan, market_survey])
xor = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)