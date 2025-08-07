import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions based on the given activities
initial_inspect = Transition(label='Initial Inspect')
material_test = Transition(label='Material Test')
imaging_scan = Transition(label='Imaging Scan')
historical_check = Transition(label='Historical Check')
expert_consult = Transition(label='Expert Consult')
provenance_trace = Transition(label='Provenance Trace')
forgery_detect = Transition(label='Forgery Detect')
restoration_map = Transition(label='Restoration Map')
market_analyze = Transition(label='Market Analyze')
auction_review = Transition(label='Auction Review')
value_assess = Transition(label='Value Assess')
report_draft = Transition(label='Report Draft')
board_review = Transition(label='Board Review')
certification = Transition(label='Certification')
release_artifact = Transition(label='Release Artifact')
chain_custody = Transition(label='Chain Custody')

# Define the partial order
root = StrictPartialOrder(nodes=[
    initial_inspect,
    material_test,
    imaging_scan,
    historical_check,
    expert_consult,
    provenance_trace,
    forgery_detect,
    restoration_map,
    market_analyze,
    auction_review,
    value_assess,
    report_draft,
    board_review,
    certification,
    release_artifact,
    chain_custody
])

# Since there are no dependencies between the activities, we don't need to define any edges in the partial order
# However, if there were dependencies, we would add them like this:
# root.order.add_edge(transition1, transition2) for each dependency

print(root)