import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

# Create the POWL model
initial_inspect_choice = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
historical_check_choice = OperatorPOWL(operator=Operator.XOR, children=[imaging_scan, skip])
market_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[historical_check, skip])
auction_review_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analyze, skip])
value_assess_choice = OperatorPOWL(operator=Operator.XOR, children=[auction_review, skip])
report_draft_choice = OperatorPOWL(operator=Operator.XOR, children=[value_assess, skip])
board_review_choice = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
certification_choice = OperatorPOWL(operator=Operator.XOR, children=[board_review, skip])
release_artifact_choice = OperatorPOWL(operator=Operator.XOR, children=[certification, skip])

# Loop for expert consultations and provenance trace
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, provenance_trace])

# Loop for imaging scans and restoration maps
imaging_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[imaging_scan, restoration_map])

# Create the root node
root = StrictPartialOrder(nodes=[
    initial_inspect_choice,
    expert_consult_loop,
    imaging_scan_loop,
    market_analyze_choice,
    auction_review_choice,
    value_assess_choice,
    report_draft_choice,
    board_review_choice,
    certification_choice,
    release_artifact_choice
])

# Add dependencies between nodes
root.order.add_edge(initial_inspect_choice, expert_consult_loop)
root.order.add_edge(expert_consult_loop, imaging_scan_loop)
root.order.add_edge(imaging_scan_loop, market_analyze_choice)
root.order.add_edge(market_analyze_choice, auction_review_choice)
root.order.add_edge(auction_review_choice, value_assess_choice)
root.order.add_edge(value_assess_choice, report_draft_choice)
root.order.add_edge(report_draft_choice, board_review_choice)
root.order.add_edge(board_review_choice, certification_choice)
root.order.add_edge(certification_choice, release_artifact_choice)

print(root)