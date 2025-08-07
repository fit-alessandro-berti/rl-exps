import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
scan_markets      = Transition(label='Scan Markets')
host_workshops    = Transition(label='Host Workshops')
form_teams        = Transition(label='Form Teams')
develop_prototypes= Transition(label='Develop Prototypes')
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

# Build the inner loop body: development, testing, feedback, ethics, analysis, partners, strategy, launch
body = StrictPartialOrder(nodes=[
    develop_prototypes, simulate_tests, collect_feedback, review_ethics,
    conduct_analysis, identify_partners, align_strategy, launch_pilots
])
body.order.add_edge(develop_prototypes, simulate_tests)
body.order.add_edge(simulate_tests, collect_feedback)
body.order.add_edge(collect_feedback, review_ethics)
body.order.add_edge(review_ethics, conduct_analysis)
body.order.add_edge(conduct_analysis, identify_partners)
body.order.add_edge(identify_partners, align_strategy)
body.order.add_edge(align_strategy, launch_pilots)

# Build the monitoring & pivoting part as a parallel set
monitoring = StrictPartialOrder(nodes=[monitor_trends, ai_analytics, pivot_plans])
monitoring.order.add_edge(monitor_trends, ai_analytics)
monitoring.order.add_edge(ai_analytics, pivot_plans)

# The complete cycle is a loop: do the inner body, then either exit or do monitoring & pivoting and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, monitoring])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    scan_markets, host_workshops, form_teams, loop, cycle_renewal
])
root.order.add_edge(scan_markets, host_workshops)
root.order.add_edge(host_workshops, form_teams)
root.order.add_edge(form_teams, loop)
root.order.add_edge(loop, cycle_renewal)