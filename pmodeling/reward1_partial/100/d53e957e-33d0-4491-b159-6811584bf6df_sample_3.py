import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[trend_scan, data_capture])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, concept_draft])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, prototype_build])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, ip_alignment])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, market_mapping])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, feedback_loop])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[design_iterate, impact_measure])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[strategy_adapt, exclusive_choice_7])

# Define the partial order
root = StrictPartialOrder(nodes=[exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8])
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)