import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_inspect, material_test])
choice = OperatorPOWL(operator=Operator.XOR, children=[historical_check, skip])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, skip])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, skip])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[restoration_map, skip])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[market_analyze, skip])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[auction_review, skip])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[value_assess, skip])
choice9 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
choice10 = OperatorPOWL(operator=Operator.XOR, children=[board_review, skip])
choice11 = OperatorPOWL(operator=Operator.XOR, children=[certification, skip])
choice12 = OperatorPOWL(operator=Operator.XOR, children=[release_artifact, skip])
choice13 = OperatorPOWL(operator=Operator.XOR, children=[chain_custody, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop, choice, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10, choice11, choice12, choice13])
root.order.add_edge(loop, choice)
root.order.add_edge(choice, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)
root.order.add_edge(choice8, choice9)
root.order.add_edge(choice9, choice10)
root.order.add_edge(choice10, choice11)
root.order.add_edge(choice11, choice12)
root.order.add_edge(choice12, choice13)
root.order.add_edge(choice13, loop)