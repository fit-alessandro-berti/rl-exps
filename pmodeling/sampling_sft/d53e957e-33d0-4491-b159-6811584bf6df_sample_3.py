import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
data_capture      = Transition(label='Data Capture')
trend_scan        = Transition(label='Trend Scan')
idea_workshop     = Transition(label='Idea Workshop')
concept_draft     = Transition(label='Concept Draft')
expert_review     = Transition(label='Expert Review')
prototype_build   = Transition(label='Prototype Build')
regulation_check  = Transition(label='Regulation Check')
ip_alignment      = Transition(label='IP Alignment')
supply_sync       = Transition(label='Supply Sync')
market_mapping    = Transition(label='Market Mapping')
pilot_launch      = Transition(label='Pilot Launch')
feedback_loop     = Transition(label='Feedback Loop')
design_iterate    = Transition(label='Design Iterate')
impact_measure    = Transition(label='Impact Measure')
strategy_adapt    = Transition(label='Strategy Adapt')

# Define the loop body (one iteration of the cycle)
body = StrictPartialOrder(nodes=[
    concept_draft,
    expert_review,
    prototype_build,
    regulation_check,
    ip_alignment,
    supply_sync,
    market_mapping,
    pilot_launch,
    feedback_loop,
    design_iterate
])
# Sequence: Draft -> Review -> Build -> Check -> Align -> Sync -> Map -> Launch -> Loop -> Iterate
for prev, next in zip([concept_draft, expert_review, prototype_build, regulation_check, ip_alignment,
                       supply_sync, market_mapping, pilot_launch, feedback_loop, design_iterate]):
    body.order.add_edge(prev, next)

# Loop operator: do the body, then optionally do another iteration
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    data_capture,
    trend_scan,
    idea_workshop,
    loop,
    impact_measure,
    strategy_adapt
])
# Sequence: Capture -> Scan -> Workshop -> Cycle -> Impact -> Adapt
root.order.add_edge(data_capture, trend_scan)
root.order.add_edge(trend_scan, idea_workshop)
root.order.add_edge(idea_workshop, loop)
root.order.add_edge(loop, impact_measure)
root.order.add_edge(impact_measure, strategy_adapt)