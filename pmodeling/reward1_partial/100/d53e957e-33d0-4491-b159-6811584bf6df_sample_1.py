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

# Define loops and XORs
trend_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[trend_scan])
idea_workshop_loop = OperatorPOWL(operator=Operator.LOOP, children=[idea_workshop])
expert_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review])
prototype_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build])
regulation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check])
ip_alignment_loop = OperatorPOWL(operator=Operator.LOOP, children=[ip_alignment])
supply_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync])
market_mapping_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_mapping])
pilot_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_launch])
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])
design_iterate_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_iterate])
impact_measure_loop = OperatorPOWL(operator=Operator.LOOP, children=[impact_measure])
strategy_adapt_loop = OperatorPOWL(operator=Operator.LOOP, children=[strategy_adapt])

# Define XORs
trend_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[trend_scan, skip])
idea_workshop_xor = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, skip])
expert_review_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
prototype_build_xor = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, skip])
regulation_check_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, skip])
ip_alignment_xor = OperatorPOWL(operator=Operator.XOR, children=[ip_alignment, skip])
supply_sync_xor = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, skip])
market_mapping_xor = OperatorPOWL(operator=Operator.XOR, children=[market_mapping, skip])
pilot_launch_xor = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, skip])
feedback_loop_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
design_iterate_xor = OperatorPOWL(operator=Operator.XOR, children=[design_iterate, skip])
impact_measure_xor = OperatorPOWL(operator=Operator.XOR, children=[impact_measure, skip])
strategy_adapt_xor = OperatorPOWL(operator=Operator.XOR, children=[strategy_adapt, skip])

# Define the root
root = StrictPartialOrder(nodes=[data_capture, trend_scan_loop, idea_workshop_loop, concept_draft, expert_review_loop, prototype_build_loop, regulation_check_loop, ip_alignment_loop, supply_sync_loop, market_mapping_loop, pilot_launch_loop, feedback_loop_loop, design_iterate_loop, impact_measure_loop, strategy_adapt_loop, trend_scan_xor, idea_workshop_xor, expert_review_xor, prototype_build_xor, regulation_check_xor, ip_alignment_xor, supply_sync_xor, market_mapping_xor, pilot_launch_xor, feedback_loop_xor, design_iterate_xor, impact_measure_xor, strategy_adapt_xor])
root.order.add_edge(trend_scan_loop, trend_scan_xor)
root.order.add_edge(idea_workshop_loop, idea_workshop_xor)
root.order.add_edge(expert_review_loop, expert_review_xor)
root.order.add_edge(prototype_build_loop, prototype_build_xor)
root.order.add_edge(regulation_check_loop, regulation_check_xor)
root.order.add_edge(ip_alignment_loop, ip_alignment_xor)
root.order.add_edge(supply_sync_loop, supply_sync_xor)
root.order.add_edge(market_mapping_loop, market_mapping_xor)
root.order.add_edge(pilot_launch_loop, pilot_launch_xor)
root.order.add_edge(feedback_loop_loop, feedback_loop_xor)
root.order.add_edge(design_iterate_loop, design_iterate_xor)
root.order.add_edge(impact_measure_loop, impact_measure_xor)
root.order.add_edge(strategy_adapt_loop, strategy_adapt_xor)

print(root)