import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake   = Transition(label='Artifact Intake')
condition_check   = Transition(label='Condition Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test  = Transition(label='Radiocarbon Test')
provenance_review = Transition(label='Provenance Review')
historical_match  = Transition(label='Historical Match')
expert_consult    = Transition(label='Expert Consult')
forgery_scan      = Transition(label='Forgery Scan')
chemical_analysis = Transition(label='Chemical Analysis')
imaging_capture   = Transition(label='Imaging Capture')
market_survey     = Transition(label='Market Survey')
value_estimate    = Transition(label='Value Estimate')
certification     = Transition(label='Certification')
digital_archive   = Transition(label='Digital Archive')
final_storage     = Transition(label='Final Storage')

# Loop for iterative expert consultation and forgery scan
skip = SilentTransition()
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_consult, forgery_scan]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    material_sampling,
    radiocarbon_test,
    provenance_review,
    historical_match,
    expert_loop,
    imaging_capture,
    chemical_analysis,
    market_survey,
    value_estimate,
    certification,
    digital_archive,
    final_storage
])

# Define the control-flow dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, material_sampling)
root.order.add_edge(material_sampling, radiocarbon_test)
root.order.add_edge(material_sampling, provenance_review)
root.order.add_edge(provenance_review, historical_match)
root.order.add_edge(historical_match, expert_loop)
root.order.add_edge(expert_loop, imaging_capture)
root.order.add_edge(expert_loop, chemical_analysis)
root.order.add_edge(imaging_capture, market_survey)
root.order.add_edge(chemical_analysis, market_survey)
root.order.add_edge(market_survey, value_estimate)
root.order.add_edge(value_estimate, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, final_storage)