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

# Define the nodes and their relationships
data_capture_and_trend_scan = OperatorPOWL(operator=Operator.XOR, children=[data_capture, trend_scan])
idea_workshop_and_concept_draft = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, concept_draft])
prototype_build_and_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, regulation_check])
ip_alignment_and_supply_sync = OperatorPOWL(operator=Operator.XOR, children=[ip_alignment, supply_sync])
market_mapping_and_pilot_launch = OperatorPOWL(operator=Operator.XOR, children=[market_mapping, pilot_launch])
feedback_loop_and_design_iterate = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, design_iterate])
impact_measure_and_strategy_adapt = OperatorPOWL(operator=Operator.XOR, children=[impact_measure, strategy_adapt])

# Create the root POWL model
root = StrictPartialOrder(nodes=[data_capture_and_trend_scan, idea_workshop_and_concept_draft, prototype_build_and_regulation_check, ip_alignment_and_supply_sync, market_mapping_and_pilot_launch, feedback_loop_and_design_iterate, impact_measure_and_strategy_adapt])
root.order.add_edge(data_capture_and_trend_scan, idea_workshop_and_concept_draft)
root.order.add_edge(idea_workshop_and_concept_draft, prototype_build_and_regulation_check)
root.order.add_edge(prototype_build_and_regulation_check, ip_alignment_and_supply_sync)
root.order.add_edge(ip_alignment_and_supply_sync, market_mapping_and_pilot_launch)
root.order.add_edge(market_mapping_and_pilot_launch, feedback_loop_and_design_iterate)
root.order.add_edge(feedback_loop_and_design_iterate, impact_measure_and_strategy_adapt)

print(root)