import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initial_inspect    = Transition(label='Initial Inspect')
material_test      = Transition(label='Material Test')
imaging_scan       = Transition(label='Imaging Scan')
historical_check   = Transition(label='Historical Check')
expert_consult     = Transition(label='Expert Consult')
provenance_trace   = Transition(label='Provenance Trace')
forgery_detect     = Transition(label='Forgery Detect')
restoration_map    = Transition(label='Restoration Map')
market_analyze     = Transition(label='Market Analyze')
auction_review     = Transition(label='Auction Review')
value_assess       = Transition(label='Value Assess')
report_draft       = Transition(label='Report Draft')
board_review       = Transition(label='Board Review')
certification      = Transition(label='Certification')
release_artifact   = Transition(label='Release Artifact')
chain_custody      = Transition(label='Chain Custody')

# Build the loop body: Market Analyze -> Auction Review -> Value Assess
body = StrictPartialOrder(nodes=[market_analyze, auction_review, value_assess])
body.order.add_edge(market_analyze, auction_review)
body.order.add_edge(auction_review, value_assess)

# Build the loop: do Historical Check, then either exit or do the loop body and repeat
historical_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[historical_check, body]
)

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    initial_inspect,
    material_test,
    imaging_scan,
    historical_loop,
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

# Define the control-flow dependencies
root.order.add_edge(initial_inspect, material_test)
root.order.add_edge(material_test, imaging_scan)
root.order.add_edge(imaging_scan, historical_loop)
root.order.add_edge(historical_loop, provenance_trace)
root.order.add_edge(provenance_trace, forgery_detect)
root.order.add_edge(forgery_detect, restoration_map)
root.order.add_edge(restoration_map, market_analyze)
root.order.add_edge(market_analyze, auction_review)
root.order.add_edge(auction_review, value_assess)
root.order.add_edge(value_assess, report_draft)
root.order.add_edge(report_draft, board_review)
root.order.add_edge(board_review, certification)
root.order.add_edge(certification, release_artifact)
root.order.add_edge(release_artifact, chain_custody)