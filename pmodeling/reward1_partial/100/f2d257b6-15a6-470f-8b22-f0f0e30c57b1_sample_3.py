from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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
forgery_scan = Transition(label='Forgery Scan')
market_survey = Transition(label='Market Survey')
value_estimate = Transition(label='Value Estimate')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
final_storage = Transition(label='Final Storage')

# Define silent transitions
skip = SilentTransition()

# Define loops
material_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling])
radiocarbon_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test])

# Define XORs
provenance_review_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, skip])
historical_match_xor = OperatorPOWL(operator=Operator.XOR, children=[historical_match, skip])
expert_consult_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
market_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[market_survey, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, material_sampling_loop, radiocarbon_test_loop, provenance_review_xor, historical_match_xor, expert_consult_xor, market_survey_xor, value_estimate, certification, digital_archive, final_storage])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, material_sampling_loop)
root.order.add_edge(material_sampling_loop, radiocarbon_test_loop)
root.order.add_edge(radiocarbon_test_loop, provenance_review_xor)
root.order.add_edge(provenance_review_xor, historical_match_xor)
root.order.add_edge(historical_match_xor, expert_consult_xor)
root.order.add_edge(expert_consult_xor, market_survey_xor)
root.order.add_edge(market_survey_xor, value_estimate)
root.order.add_edge(value_estimate, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, final_storage)