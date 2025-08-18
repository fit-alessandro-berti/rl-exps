from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order and its dependencies
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (initial_inspect, material_test),
        (initial_inspect, imaging_scan),
        (material_test, historical_check),
        (material_test, expert_consult),
        (imaging_scan, provenance_trace),
        (imaging_scan, forgery_detect),
        (historical_check, market_analyze),
        (historical_check, auction_review),
        (expert_consult, market_analyze),
        (expert_consult, auction_review),
        (provenance_trace, restoration_map),
        (provenance_trace, market_analyze),
        (provenance_trace, auction_review),
        (forgery_detect, restoration_map),
        (forgery_detect, market_analyze),
        (forgery_detect, auction_review),
        (restoration_map, market_analyze),
        (restoration_map, auction_review),
        (market_analyze, value_assess),
        (market_analyze, report_draft),
        (auction_review, value_assess),
        (auction_review, report_draft),
        (value_assess, board_review),
        (value_assess, certification),
        (report_draft, board_review),
        (report_draft, certification),
        (board_review, certification),
        (certification, release_artifact),
        (certification, chain_custody)
    ]
)

# Optionally, add silent transitions for clarity (e.g., skipping certain steps)
skip_step = SilentTransition()
root.order.add_edge(material_test, skip_step)
root.order.add_edge(imaging_scan, skip_step)
root.order.add_edge(historical_check, skip_step)
root.order.add_edge(expert_consult, skip_step)
root.order.add_edge(provenance_trace, skip_step)
root.order.add_edge(forgery_detect, skip_step)
root.order.add_edge(restoration_map, skip_step)
root.order.add_edge(market_analyze, skip_step)
root.order.add_edge(auction_review, skip_step)
root.order.add_edge(value_assess, skip_step)
root.order.add_edge(report_draft, skip_step)
root.order.add_edge(board_review, skip_step)
root.order.add_edge(certification, skip_step)
root.order.add_edge(release_artifact, skip_step)
root.order.add_edge(chain_custody, skip_step)

# Print the root POWL model
print(root)