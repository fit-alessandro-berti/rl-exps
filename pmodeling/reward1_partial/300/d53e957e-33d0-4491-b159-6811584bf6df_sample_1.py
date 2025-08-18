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

# Define exclusive choice for regulatory landscapes and IP strategies
xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, ip_alignment])

# Define loops for supply chain adaptations and market mapping
loop_supply = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync, market_mapping])

# Define the root node with all activities and dependencies
root = StrictPartialOrder(nodes=[data_capture, trend_scan, idea_workshop, concept_draft, expert_review, prototype_build, xor, loop_supply, feedback_loop, design_iterate, impact_measure, strategy_adapt])
root.order.add_edge(data_capture, trend_scan)
root.order.add_edge(trend_scan, idea_workshop)
root.order.add_edge(idea_workshop, concept_draft)
root.order.add_edge(concept_draft, expert_review)
root.order.add_edge(expert_review, prototype_build)
root.order.add_edge(prototype_build, xor)
root.order.add_edge(xor, loop_supply)
root.order.add_edge(loop_supply, feedback_loop)
root.order.add_edge(feedback_loop, design_iterate)
root.order.add_edge(design_iterate, impact_measure)
root.order.add_edge(impact_measure, strategy_adapt)

print(root)