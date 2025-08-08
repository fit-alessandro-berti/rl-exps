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

# Define silent transitions (for loops)
skip = SilentTransition()

# Define the partial order structure
root = StrictPartialOrder()

# Add transitions to the root
root.add_node(artifact_intake)
root.add_node(condition_check)
root.add_node(material_sampling)
root.add_node(radiocarbon_test)
root.add_node(provenance_review)
root.add_node(imaging_capture)
root.add_node(chemical_analysis)
root.add_node(historical_match)
root.add_node(expert_consult)
root.add_node(forgery_scan)
root.add_node(market_survey)
root.add_node(value_estimate)
root.add_node(certification)
root.add_node(digital_archive)
root.add_node(final_storage)

# Define dependencies between transitions
root.add_edge(artifact_intake, condition_check)
root.add_edge(condition_check, material_sampling)
root.add_edge(material_sampling, radiocarbon_test)
root.add_edge(radiocarbon_test, provenance_review)
root.add_edge(provenance_review, imaging_capture)
root.add_edge(imaging_capture, chemical_analysis)
root.add_edge(chemical_analysis, historical_match)
root.add_edge(historical_match, expert_consult)
root.add_edge(expert_consult, forgery_scan)
root.add_edge(forgery_scan, market_survey)
root.add_edge(market_survey, value_estimate)
root.add_edge(value_estimate, certification)
root.add_edge(certification, digital_archive)
root.add_edge(digital_archive, final_storage)

# Print the final POWL model
print(root)