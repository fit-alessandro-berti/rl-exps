import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the POWL model
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, trend_scan])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, expert_review])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[concept_draft, prototype_build])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, ip_alignment])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, market_mapping])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, feedback_loop])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[design_iterate, impact_measure])
xor_8 = OperatorPOWL(operator=Operator.XOR, children=[strategy_adapt, None])

root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7, xor_8])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_7)
root.order.add_edge(xor_7, xor_8)
root.order.add_edge(xor_8, xor_1)