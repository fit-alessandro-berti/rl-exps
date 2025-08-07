import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    material_sampling,
    radiocarbon_test,
    provenance_review,
    imaging_capture,
    chemical_analysis,
    historical_match,
    expert_consult,
    forgery_scan,
    market_survey,
    value_estimate,
    certification,
    digital_archive,
    final_storage
])

# Define dependencies if any (not applicable in this case as all activities are concurrent)
# root.order.add_edge(...)

print(root)