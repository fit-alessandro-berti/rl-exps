import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_test, imaging_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[historical_check, expert_consult])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, forgery_detect])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[restoration_map, market_analyze])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[auction_review, value_assess])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, board_review])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[certification, release_artifact])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[chain_custody, initial_inspect])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor1)