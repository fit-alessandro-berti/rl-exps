import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, trend_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, expert_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, regulation_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ip_alignment, supply_sync])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[market_mapping, pilot_launch])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, impact_measure])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[design_iterate, strategy_adapt])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor1])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])

# Define the order dependencies
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop2, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop3, xor7)
root.order.add_edge(loop4, xor1)

# Save the final result in the variable 'root'
root