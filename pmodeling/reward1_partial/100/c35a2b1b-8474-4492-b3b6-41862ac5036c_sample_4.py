import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
initial_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_inspect, material_test])
historical_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_check, expert_consult, provenance_trace])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_map, forgery_detect])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analyze, auction_review, value_assess])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, board_review])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification, release_artifact])

# Define exclusive choices
market_choice = OperatorPOWL(operator=Operator.XOR, children=[market_loop, skip])
report_choice = OperatorPOWL(operator=Operator.XOR, children=[report_loop, skip])
certification_choice = OperatorPOWL(operator=Operator.XOR, children=[certification_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    initial_loop,
    historical_loop,
    restoration_loop,
    market_choice,
    report_choice,
    certification_choice,
    chain_custody
])
root.order.add_edge(initial_loop, historical_loop)
root.order.add_edge(historical_loop, restoration_loop)
root.order.add_edge(restoration_loop, market_choice)
root.order.add_edge(market_choice, report_choice)
root.order.add_edge(report_choice, certification_choice)
root.order.add_edge(certification_choice, chain_custody)

print(root)