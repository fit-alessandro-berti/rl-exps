import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
init_inspect   = Transition(label='Initial Inspect')
material_test  = Transition(label='Material Test')
img_scan       = Transition(label='Imaging Scan')
historical_chk = Transition(label='Historical Check')
expert_consult = Transition(label='Expert Consult')
prov_trace     = Transition(label='Provenance Trace')
forgery_detect = Transition(label='Forgery Detect')
restoration_map= Transition(label='Restoration Map')
market_analyze = Transition(label='Market Analyze')
auction_review = Transition(label='Auction Review')
value_assess   = Transition(label='Value Assess')
report_draft   = Transition(label='Report Draft')
board_review   = Transition(label='Board Review')
certification  = Transition(label='Certification')
release_art    = Transition(label='Release Artifact')
chain_custody  = Transition(label='Chain Custody')

# Loop for iterative imaging and historical checks
loop_img_his = OperatorPOWL(
    operator=Operator.LOOP,
    children=[img_scan, historical_chk]
)

# Exclusive choice for forgery or restoration detection
xor_forgery_rest = OperatorPOWL(
    operator=Operator.XOR,
    children=[forgery_detect, restoration_map]
)

# Sequence for market analysis and auction review
seq_market_auction = StrictPartialOrder(nodes=[market_analyze, auction_review])
seq_market_auction.order.add_edge(market_analyze, auction_review)

# Build the partial order
root = StrictPartialOrder(nodes=[
    init_inspect,
    material_test,
    loop_img_his,
    expert_consult,
    prov_trace,
    xor_forgery_rest,
    value_assess,
    report_draft,
    board_review,
    certification,
    release_art,
    chain_custody
])

# Add edges
root.order.add_edge(init_inspect, material_test)
root.order.add_edge(material_test, loop_img_his)
root.order.add_edge(material_test, expert_consult)
root.order.add_edge(loop_img_his, prov_trace)
root.order.add_edge(prov_trace, xor_forgery_rest)
root.order.add_edge(xor_forgery_rest, value_assess)
root.order.add_edge(value_assess, report_draft)
root.order.add_edge(report_draft, board_review)
root.order.add_edge(board_review, certification)
root.order.add_edge(certification, release_art)
root.order.add_edge(release_art, chain_custody)