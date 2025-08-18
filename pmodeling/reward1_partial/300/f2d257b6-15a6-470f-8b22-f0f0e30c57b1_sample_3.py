import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transition for no action
skip = SilentTransition()

# Define the loop for radiocarbon testing
radiocarbon_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test])

# Define the XOR for chemical analysis and market survey
xor_chemical_market = OperatorPOWL(operator=Operator.XOR, children=[chemical_analysis, market_survey])

# Define the XOR for historical match and expert consult
xor_historical_expert = OperatorPOWL(operator=Operator.XOR, children=[historical_match, expert_consult])

# Define the XOR for forgeries scan and market survey
xor_forgeries_market = OperatorPOWL(operator=Operator.XOR, children=[forgeries_scan, market_survey])

# Define the XOR for value estimate and digital archive
xor_value_archive = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, digital_archive])

# Define the XOR for certification and final storage
xor_certify_storage = OperatorPOWL(operator=Operator.XOR, children=[certification, final_storage])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    material_sampling,
    radiocarbon_loop,
    xor_chemical_market,
    xor_historical_expert,
    xor_forgeries_market,
    xor_value_archive,
    xor_certify_storage
])

# Define the edges in the partial order
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, material_sampling)
root.order.add_edge(material_sampling, radiocarbon_loop)
root.order.add_edge(radiocarbon_loop, xor_chemical_market)
root.order.add_edge(xor_chemical_market, xor_historical_expert)
root.order.add_edge(xor_historical_expert, xor_forgeries_market)
root.order.add_edge(xor_forgeries_market, xor_value_archive)
root.order.add_edge(xor_value_archive, xor_certify_storage)
root.order.add_edge(xor_certify_storage, certification)
root.order.add_edge(xor_certify_storage, final_storage)

# Print the root POWL model
print(root)