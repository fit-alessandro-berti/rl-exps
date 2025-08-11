import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[data_capture, trend_scan])

# Define loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[idea_workshop, concept_draft])

# Define POWL model
root = StrictPartialOrder(nodes=[loop, xor, expert_review, prototype_build, regulation_check, ip_alignment, supply_sync, market_mapping, pilot_launch, feedback_loop, design_iterate, impact_measure, strategy_adapt])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, expert_review)
root.order.add_edge(expert_review, prototype_build)
root.order.add_edge(prototype_build, regulation_check)
root.order.add_edge(regulation_check, ip_alignment)
root.order.add_edge(ip_alignment, supply_sync)
root.order.add_edge(supply_sync, market_mapping)
root.order.add_edge(market_mapping, pilot_launch)
root.order.add_edge(pilot_launch, feedback_loop)
root.order.add_edge(feedback_loop, design_iterate)
root.order.add_edge(design_iterate, impact_measure)
root.order.add_edge(impact_measure, strategy_adapt)

# Print the POWL model
print(root)