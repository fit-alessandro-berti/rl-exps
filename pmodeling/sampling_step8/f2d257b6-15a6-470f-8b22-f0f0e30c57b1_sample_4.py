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

skip = SilentTransition()

artifact_intake_to_condition_check = OperatorPOWL(operator=Operator.SEQUENCE, children=[artifact_intake, condition_check])
condition_check_to_material_sampling = OperatorPOWL(operator=Operator.SEQUENCE, children=[condition_check, material_sampling])
material_sampling_to_radiocarbon_test = OperatorPOWL(operator=Operator.SEQUENCE, children=[material_sampling, radiocarbon_test])
radiocarbon_test_to_provenance_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[radiocarbon_test, provenance_review])
provenance_review_to_imaging_capture = OperatorPOWL(operator=Operator.SEQUENCE, children=[provenance_review, imaging_capture])
imaging_capture_to_chemical_analysis = OperatorPOWL(operator=Operator.SEQUENCE, children=[imaging_capture, chemical_analysis])
chemical_analysis_to_historical_match = OperatorPOWL(operator=Operator.SEQUENCE, children=[chemical_analysis, historical_match])
historical_match_to_expert_consult = OperatorPOWL(operator=Operator.SEQUENCE, children=[historical_match, expert_consult])
expert_consult_to_forgery_scan = OperatorPOWL(operator=Operator.SEQUENCE, children=[expert_consult, forgery_scan])
forgery_scan_to_market_survey = OperatorPOWL(operator=Operator.SEQUENCE, children=[forgery_scan, market_survey])
market_survey_to_value_estimate = OperatorPOWL(operator=Operator.SEQUENCE, children=[market_survey, value_estimate])
value_estimate_to_certification = OperatorPOWL(operator=Operator.SEQUENCE, children=[value_estimate, certification])
certification_to_final_storage = OperatorPOWL(operator=Operator.SEQUENCE, children=[certification, final_storage])

root = StrictPartialOrder(nodes=[
    artifact_intake_to_condition_check,
    condition_check_to_material_sampling,
    material_sampling_to_radiocarbon_test,
    radiocarbon_test_to_provenance_review,
    provenance_review_to_imaging_capture,
    imaging_capture_to_chemical_analysis,
    chemical_analysis_to_historical_match,
    historical_match_to_expert_consult,
    expert_consult_to_forgery_scan,
    forgery_scan_to_market_survey,
    market_survey_to_value_estimate,
    value_estimate_to_certification,
    certification_to_final_storage
])

root.order.add_edge(artifact_intake_to_condition_check, condition_check_to_material_sampling)
root.order.add_edge(condition_check_to_material_sampling, material_sampling_to_radiocarbon_test)
root.order.add_edge(material_sampling_to_radiocarbon_test, radiocarbon_test_to_provenance_review)
root.order.add_edge(radiocarbon_test_to_provenance_review, provenance_review_to_imaging_capture)
root.order.add_edge(provenance_review_to_imaging_capture, imaging_capture_to_chemical_analysis)
root.order.add_edge(imaging_capture_to_chemical_analysis, chemical_analysis_to_historical_match)
root.order.add_edge(chemical_analysis_to_historical_match, historical_match_to_expert_consult)
root.order.add_edge(historical_match_to_expert_consult, expert_consult_to_forgery_scan)
root.order.add_edge(expert_consult_to_forgery_scan, forgery_scan_to_market_survey)
root.order.add_edge(forgery_scan_to_market_survey, market_survey_to_value_estimate)
root.order.add_edge(market_survey_to_value_estimate, value_estimate_to_certification)
root.order.add_edge(value_estimate_to_certification, certification_to_final_storage)