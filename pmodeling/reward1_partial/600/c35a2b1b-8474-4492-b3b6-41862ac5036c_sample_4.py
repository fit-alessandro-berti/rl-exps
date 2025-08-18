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

initial_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_inspect])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test])
imaging_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[imaging_scan])
historical_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_check])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult])
provenance_trace_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_trace])
forgery_detect_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_detect])
restoration_map_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_map])
market_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analyze])
auction_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_review])
value_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[value_assess])
report_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
board_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[board_review])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification])
release_artifact_loop = OperatorPOWL(operator=Operator.LOOP, children=[release_artifact])
chain_custody_loop = OperatorPOWL(operator=Operator.LOOP, children=[chain_custody])

root = StrictPartialOrder(nodes=[
    initial_inspect_loop, material_test_loop, imaging_scan_loop, historical_check_loop, expert_consult_loop,
    provenance_trace_loop, forgery_detect_loop, restoration_map_loop, market_analyze_loop, auction_review_loop,
    value_assess_loop, report_draft_loop, board_review_loop, certification_loop, release_artifact_loop,
    chain_custody_loop
])

root.order.add_edge(initial_inspect_loop, material_test_loop)
root.order.add_edge(material_test_loop, imaging_scan_loop)
root.order.add_edge(imaging_scan_loop, historical_check_loop)
root.order.add_edge(historical_check_loop, expert_consult_loop)
root.order.add_edge(expert_consult_loop, provenance_trace_loop)
root.order.add_edge(provenance_trace_loop, forgery_detect_loop)
root.order.add_edge(forgery_detect_loop, restoration_map_loop)
root.order.add_edge(restoration_map_loop, market_analyze_loop)
root.order.add_edge(market_analyze_loop, auction_review_loop)
root.order.add_edge(auction_review_loop, value_assess_loop)
root.order.add_edge(value_assess_loop, report_draft_loop)
root.order.add_edge(report_draft_loop, board_review_loop)
root.order.add_edge(board_review_loop, certification_loop)
root.order.add_edge(certification_loop, release_artifact_loop)
root.order.add_edge(release_artifact_loop, chain_custody_loop)

print(root)