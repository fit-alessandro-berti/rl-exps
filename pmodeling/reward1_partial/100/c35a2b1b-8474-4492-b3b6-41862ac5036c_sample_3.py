import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
initial_inspect = Transition(label='Initial Inspect')
material_test = Transition(label='Material Test')
imaging_scan = Transition(label='Imaging Scan')
historical_check = Transition(label='Historical Check')
expert_consult = Transition(label='Expert Consult')
provenance_trace = Transition(label='Provenance Trace')
forgeries_detect = Transition(label='Forgery Detect')
restoration_map = Transition(label='Restoration Map')
market_analyze = Transition(label='Market Analyze')
auction_review = Transition(label='Auction Review')
value_assess = Transition(label='Value Assess')
report_draft = Transition(label='Report Draft')
board_review = Transition(label='Board Review')
certification = Transition(label='Certification')
release_artifact = Transition(label='Release Artifact')
chain_custody = Transition(label='Chain Custody')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
initial_inspect_process = StrictPartialOrder(nodes=[initial_inspect])
material_test_process = StrictPartialOrder(nodes=[material_test])
imaging_scan_process = StrictPartialOrder(nodes=[imaging_scan])
historical_check_process = StrictPartialOrder(nodes=[historical_check])
expert_consult_process = StrictPartialOrder(nodes=[expert_consult])
provenance_trace_process = StrictPartialOrder(nodes=[provenance_trace])
forgeries_detect_process = StrictPartialOrder(nodes=[forgeries_detect])
restoration_map_process = StrictPartialOrder(nodes=[restoration_map])
market_analyze_process = StrictPartialOrder(nodes=[market_analyze])
auction_review_process = StrictPartialOrder(nodes=[auction_review])
value_assess_process = StrictPartialOrder(nodes=[value_assess])
report_draft_process = StrictPartialOrder(nodes=[report_draft])
board_review_process = StrictPartialOrder(nodes=[board_review])
certification_process = StrictPartialOrder(nodes=[certification])
release_artifact_process = StrictPartialOrder(nodes=[release_artifact])
chain_custody_process = StrictPartialOrder(nodes=[chain_custody])

# Define process flow
xor = OperatorPOWL(operator=Operator.XOR, children=[
    initial_inspect_process,
    material_test_process,
    imaging_scan_process,
    historical_check_process,
    expert_consult_process,
    provenance_trace_process,
    forgeries_detect_process,
    restoration_map_process,
    market_analyze_process,
    auction_review_process,
    value_assess_process,
    report_draft_process,
    board_review_process,
    certification_process,
    release_artifact_process,
    chain_custody_process
])

# Define loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor])

# Define root process
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)