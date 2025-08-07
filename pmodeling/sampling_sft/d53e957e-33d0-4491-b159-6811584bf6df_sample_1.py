import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
data_capture     = Transition(label='Data Capture')
trend_scan        = Transition(label='Trend Scan')
idea_workshop    = Transition(label='Idea Workshop')
concept_draft    = Transition(label='Concept Draft')
expert_review    = Transition(label='Expert Review')
prototype_build  = Transition(label='Prototype Build')
regulation_check = Transition(label='Regulation Check')
ip_alignment     = Transition(label='IP Alignment')
supply_sync      = Transition(label='Supply Sync')
market_mapping   = Transition(label='Market Mapping')
pilot_launch     = Transition(label='Pilot Launch')
feedback_loop    = Transition(label='Feedback Loop')
design_iterate   = Transition(label='Design Iterate')
impact_measure   = Transition(label='Impact Measure')
strategy_adapt   = Transition(label='Strategy Adapt')

# Build the main prototype‐to‐adapt sequence as a partial order
main_seq = StrictPartialOrder(nodes=[
    data_capture, trend_scan, idea_workshop,
    concept_draft, expert_review, prototype_build,
    regulation_check, ip_alignment, supply_sync,
    market_mapping, pilot_launch, feedback_loop,
    design_iterate, impact_measure, strategy_adapt
])

# Define the control-flow dependencies
main_seq.order.add_edge(data_capture, trend_scan)
main_seq.order.add_edge(trend_scan, idea_workshop)
main_seq.order.add_edge(idea_workshop, concept_draft)
main_seq.order.add_edge(concept_draft, expert_review)
main_seq.order.add_edge(expert_review, prototype_build)
main_seq.order.add_edge(prototype_build, regulation_check)
main_seq.order.add_edge(regulation_check, ip_alignment)
main_seq.order.add_edge(ip_alignment, supply_sync)
main_seq.order.add_edge(supply_sync, market_mapping)
main_seq.order.add_edge(market_mapping, pilot_launch)
main_seq.order.add_edge(pilot_launch, feedback_loop)
main_seq.order.add_edge(feedback_loop, design_iterate)
main_seq.order.add_edge(design_iterate, impact_measure)
main_seq.order.add_edge(impact_measure, strategy_adapt)

# Loop: after Strategy Adapt, repeat the entire sequence
loop = OperatorPOWL(operator=Operator.LOOP, children=[strategy_adapt, main_seq])

# Final root is the top-level loop
root = loop