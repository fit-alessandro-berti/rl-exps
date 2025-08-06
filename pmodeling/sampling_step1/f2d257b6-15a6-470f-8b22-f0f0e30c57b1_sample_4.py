import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, material_sampling, radiocarbon_test, provenance_review, imaging_capture, chemical_analysis, historical_match, expert_consult, forgeries_scan, market_survey, value_estimate, certification, digital_archive, final_storage])

# Define the dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, material_sampling)
root.order.add_edge(material_sampling, radiocarbon_test)
root.order.add_edge(radiocarbon_test, provenance_review)
root.order.add_edge(provenance_review, imaging_capture)
root.order.add_edge(imaging_capture, chemical_analysis)
root.order.add_edge(chemical_analysis, historical_match)
root.order.add_edge(historical_match, expert_consult)
root.order.add_edge(expert_consult, forgeries_scan)
root.order.add_edge(forgeries_scan, market_survey)
root.order.add_edge(market_survey, value_estimate)
root.order.add_edge(value_estimate, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, final_storage)

print(root)