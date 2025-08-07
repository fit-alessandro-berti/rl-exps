import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
scan_markets      = Transition(label='Scan Markets')
host_workshops    = Transition(label='Host Workshops')
form_teams        = Transition(label='Form Teams')
develop_protos    = Transition(label='Develop Prototypes')
simulate_tests    = Transition(label='Simulate Tests')
collect_feedback  = Transition(label='Collect Feedback')
review_ethics     = Transition(label='Review Ethics')
conduct_analysis  = Transition(label='Conduct Analysis')
identify_partners = Transition(label='Identify Partners')
align_strategy    = Transition(label='Align Strategy')
launch_pilots     = Transition(label='Launch Pilots')
monitor_trends    = Transition(label='Monitor Trends')
ai_analytics      = Transition(label='AI Analytics')
pivot_plans       = Transition(label='Pivot Plans')
cycle_renewal     = Transition(label='Cycle Renewal')

# Define the loop body: Monitor Trends -> AI Analytics -> Pivot Plans
loop_body = StrictPartialOrder(nodes=[monitor_trends, ai_analytics, pivot_plans])
loop_body.order.add_edge(monitor_trends, ai_analytics)
loop_body.order.add_edge(ai_analytics, pivot_plans)

# Define the loop: do Align Strategy, then either exit or execute the loop body and Align Strategy again
loop = OperatorPOWL(operator=Operator.LOOP, children=[align_strategy, loop_body])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    scan_markets, host_workshops, form_teams,
    develop_protos, simulate_tests, collect_feedback,
    review_ethics, conduct_analysis, identify_partners,
    align_strategy, launch_pilots,
    loop
])

# Define the control-flow dependencies
root.order.add_edge(scan_markets, host_workshops)
root.order.add_edge(host_workshops, form_teams)
root.order.add_edge(form_teams, develop_protos)
root.order.add_edge(develop_protos, simulate_tests)
root.order.add_edge(simulate_tests, collect_feedback)
root.order.add_edge(collect_feedback, review_ethics)
root.order.add_edge(review_ethics, conduct_analysis)
root.order.add_edge(conduct_analysis, identify_partners)
root.order.add_edge(identify_partners, align_strategy)
root.order.add_edge(align_strategy, launch_pilots)
root.order.add_edge(align_strategy, loop)
root.order.add_edge(launch_pilots, loop)
root.order.add_edge(loop, align_strategy)

print(root)