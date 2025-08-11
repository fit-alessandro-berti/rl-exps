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
forgeries_scan = Transition(label='Forgery Scan')
market_survey = Transition(label='Market Survey')
value_estimate = Transition(label='Value Estimate')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
final_storage = Transition(label='Final Storage')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
artifact_intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake])
condition_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_check])
material_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling])
radiocarbon_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test])
provenance_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_review])
imaging_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[imaging_capture])
chemical_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_analysis])
historical_match_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_match])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult])
forgeries_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgeries_scan])
market_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_survey])
value_estimate_loop = OperatorPOWL(operator=Operator.LOOP, children=[value_estimate])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification])
digital_archive_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_archive])
final_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_storage])

# Define choices
artifact_intake_xor = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake_loop, skip])
condition_check_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_check_loop, skip])
material_sampling_xor = OperatorPOWL(operator=Operator.XOR, children=[material_sampling_loop, skip])
radiocarbon_test_xor = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test_loop, skip])
provenance_review_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_review_loop, skip])
imaging_capture_xor = OperatorPOWL(operator=Operator.XOR, children=[imaging_capture_loop, skip])
chemical_analysis_xor = OperatorPOWL(operator=Operator.XOR, children=[chemical_analysis_loop, skip])
historical_match_xor = OperatorPOWL(operator=Operator.XOR, children=[historical_match_loop, skip])
expert_consult_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_consult_loop, skip])
forgeries_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[forgeries_scan_loop, skip])
market_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[market_survey_loop, skip])
value_estimate_xor = OperatorPOWL(operator=Operator.XOR, children=[value_estimate_loop, skip])
certification_xor = OperatorPOWL(operator=Operator.XOR, children=[certification_loop, skip])
digital_archive_xor = OperatorPOWL(operator=Operator.XOR, children=[digital_archive_loop, skip])
final_storage_xor = OperatorPOWL(operator=Operator.XOR, children=[final_storage_loop, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake_xor,
    condition_check_xor,
    material_sampling_xor,
    radiocarbon_test_xor,
    provenance_review_xor,
    imaging_capture_xor,
    chemical_analysis_xor,
    historical_match_xor,
    expert_consult_xor,
    forgeries_scan_xor,
    market_survey_xor,
    value_estimate_xor,
    certification_xor,
    digital_archive_xor,
    final_storage_xor
])

# Define dependencies between nodes
root.order.add_edge(artifact_intake_xor, condition_check_xor)
root.order.add_edge(condition_check_xor, material_sampling_xor)
root.order.add_edge(material_sampling_xor, radiocarbon_test_xor)
root.order.add_edge(radiocarbon_test_xor, provenance_review_xor)
root.order.add_edge(provenance_review_xor, imaging_capture_xor)
root.order.add_edge(imaging_capture_xor, chemical_analysis_xor)
root.order.add_edge(chemical_analysis_xor, historical_match_xor)
root.order.add_edge(historical_match_xor, expert_consult_xor)
root.order.add_edge(expert_consult_xor, forgeries_scan_xor)
root.order.add_edge(forgeries_scan_xor, market_survey_xor)
root.order.add_edge(market_survey_xor, value_estimate_xor)
root.order.add_edge(value_estimate_xor, certification_xor)
root.order.add_edge(certification_xor, digital_archive_xor)
root.order.add_edge(digital_archive_xor, final_storage_xor)

# Print the root
print(root)