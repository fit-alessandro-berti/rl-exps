import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[initial_inspect, material_test])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[imaging_scan, historical_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, provenance_trace])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, restoration_map])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[market_analyze, auction_review])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[value_assess, report_draft])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[board_review, certification])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[release_artifact, chain_custody])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)