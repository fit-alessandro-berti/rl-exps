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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
trend_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[trend_scan])
idea_workshop_loop = OperatorPOWL(operator=Operator.LOOP, children=[idea_workshop])
concept_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_draft])
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

# Define the partial order
root = StrictPartialOrder(nodes=[data_capture, trend_scan_loop, idea_workshop_loop, concept_draft_loop, expert_review_loop, prototype_build_loop, regulation_check_loop, ip_alignment_loop, supply_sync_loop, market_mapping_loop, pilot_launch_loop, feedback_loop_loop, design_iterate_loop, impact_measure_loop, strategy_adapt_loop])

# Define dependencies between nodes
root.order.add_edge(data_capture, trend_scan)
root.order.add_edge(trend_scan, idea_workshop)
root.order.add_edge(idea_workshop, concept_draft)
root.order.add_edge(concept_draft, expert_review)
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