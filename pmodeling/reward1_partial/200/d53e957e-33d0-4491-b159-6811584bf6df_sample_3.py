import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (for empty labels)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()
skip8 = SilentTransition()
skip9 = SilentTransition()
skip10 = SilentTransition()
skip11 = SilentTransition()
skip12 = SilentTransition()
skip13 = SilentTransition()
skip14 = SilentTransition()
skip15 = SilentTransition()

# Define loop nodes and operators
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, trend_scan])
idea_loop = OperatorPOWL(operator=Operator.LOOP, children=[idea_workshop, concept_draft, expert_review, prototype_build, regulation_check, ip_alignment, supply_sync, market_mapping, pilot_launch])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, design_iterate, impact_measure, strategy_adapt])

# Define the root node with all the nodes and their dependencies
root = StrictPartialOrder(nodes=[data_loop, idea_loop, feedback_loop])
root.order.add_edge(data_loop, idea_loop)
root.order.add_edge(idea_loop, feedback_loop)

print(root)