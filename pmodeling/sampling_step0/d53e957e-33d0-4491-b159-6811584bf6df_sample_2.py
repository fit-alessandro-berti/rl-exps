import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
data_capture = Transition(label='Data Capture')
trend_scan = Transition(label='Trend Scan')
idea_workshop = Transition(label='Idea Workshop')
concept_draft = Transition(label='Concept Draft')
expert_review = Transition(label='Expert Review')
prototype_build = Transition(label='Prototype Build')
regulation_check = Transition(label='Regulation Check')
ip_alignment = Transition(label='IP Alignment')
supply_sync = Transition(label='Supply Sync')
market_mapping = Transition(label='Market Mapping')
pilot_launch = Transition(label='Pilot Launch')
feedback_loop = Transition(label='Feedback Loop')
design_iterate = Transition(label='Design Iterate')
impact_measure = Transition(label='Impact Measure')
strategy_adapt = Transition(label='Strategy Adapt')

# Define silent transitions (e.g., for concurrency)
skip = SilentTransition()

# Define loops and choices based on the process description
# For simplicity, assume each activity has a direct successor unless specified otherwise
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, trend_scan])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[concept_draft, expert_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, skip])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, ip_alignment])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[market_mapping, pilot_launch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[design_iterate, impact_measure])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[strategy_adapt, skip])

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4, loop5, xor5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)

print(root)