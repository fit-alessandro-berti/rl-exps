import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loop node for material sampling and radiocarbon test
material_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test])

# Define the XOR node for imaging capture and chemical analysis
imaging_capture_xor = OperatorPOWL(operator=Operator.XOR, children=[imaging_capture, chemical_analysis])

# Define the XOR node for historical match and expert consult
historical_match_xor = OperatorPOWL(operator=Operator.XOR, children=[historical_match, expert_consult])

# Define the XOR node for forgery scan and market survey
forgery_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, market_survey])

# Define the XOR node for value estimate and certification
value_estimate_xor = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, certification])

# Define the XOR node for digital archive and final storage
digital_archive_xor = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, final_storage])

# Define the root node
root = StrictPartialOrder(nodes=[material_sampling_loop, imaging_capture_xor, historical_match_xor, forgery_scan_xor, value_estimate_xor, digital_archive_xor])
root.order.add_edge(material_sampling_loop, imaging_capture_xor)
root.order.add_edge(imaging_capture_xor, historical_match_xor)
root.order.add_edge(historical_match_xor, forgery_scan_xor)
root.order.add_edge(forgery_scan_xor, value_estimate_xor)
root.order.add_edge(value_estimate_xor, digital_archive_xor)
root.order.add_edge(digital_archive_xor, final_storage)