import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop and choice nodes
artifact_intake_to_condition_check = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, condition_check])
material_sampling_to_radiocarbon_test = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test])
provenance_review_to_imaging_capture = OperatorPOWL(operator=Operator.LOOP, children=[provenance_review, imaging_capture])
chemical_analysis_to_historical_match = OperatorPOWL(operator=Operator.LOOP, children=[chemical_analysis, historical_match])
expert_consult_to_forgeries_scan = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, forgeries_scan])
market_survey_to_value_estimate = OperatorPOWL(operator=Operator.LOOP, children=[market_survey, value_estimate])
certification_to_final_storage = OperatorPOWL(operator=Operator.LOOP, children=[certification, final_storage])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake_to_condition_check, material_sampling_to_radiocarbon_test, provenance_review_to_imaging_capture, chemical_analysis_to_historical_match, expert_consult_to_forgeries_scan, market_survey_to_value_estimate, certification_to_final_storage])

# Define the partial order
root.order.add_edge(artifact_intake_to_condition_check, material_sampling_to_radiocarbon_test)
root.order.add_edge(artifact_intake_to_condition_check, provenance_review_to_imaging_capture)
root.order.add_edge(artifact_intake_to_condition_check, chemical_analysis_to_historical_match)
root.order.add_edge(artifact_intake_to_condition_check, expert_consult_to_forgeries_scan)
root.order.add_edge(artifact_intake_to_condition_check, market_survey_to_value_estimate)
root.order.add_edge(artifact_intake_to_condition_check, certification_to_final_storage)

# Print the root POWL model
print(root)