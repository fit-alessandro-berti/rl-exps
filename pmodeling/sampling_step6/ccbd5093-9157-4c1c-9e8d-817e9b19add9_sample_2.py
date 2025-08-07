import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
scan_markets = Transition(label='Scan Markets')
host_workshops = Transition(label='Host Workshops')
form_teams = Transition(label='Form Teams')
develop_prototypes = Transition(label='Develop Prototypes')
simulate_tests = Transition(label='Simulate Tests')
collect_feedback = Transition(label='Collect Feedback')
review_ethics = Transition(label='Review Ethics')
conduct_analysis = Transition(label='Conduct Analysis')
identify_partners = Transition(label='Identify Partners')
align_strategy = Transition(label='Align Strategy')
launch_pilots = Transition(label='Launch Pilots')
monitor_trends = Transition(label='Monitor Trends')
ai_analytics = Transition(label='AI Analytics')
pivot_plans = Transition(label='Pivot Plans')
cycle_renewal = Transition(label='Cycle Renewal')

# Define the partial order
root = StrictPartialOrder(nodes=[
    scan_markets,
    host_workshops,
    form_teams,
    develop_prototypes,
    simulate_tests,
    collect_feedback,
    review_ethics,
    conduct_analysis,
    identify_partners,
    align_strategy,
    launch_pilots,
    monitor_trends,
    ai_analytics,
    pivot_plans,
    cycle_renewal
])

# Define the partial order dependencies
root.order.add_edge(scan_markets, host_workshops)
root.order.add_edge(scan_markets, form_teams)
root.order.add_edge(scan_markets, develop_prototypes)
root.order.add_edge(scan_markets, simulate_tests)
root.order.add_edge(scan_markets, collect_feedback)
root.order.add_edge(scan_markets, review_ethics)
root.order.add_edge(scan_markets, conduct_analysis)
root.order.add_edge(scan_markets, identify_partners)
root.order.add_edge(scan_markets, align_strategy)
root.order.add_edge(scan_markets, launch_pilots)
root.order.add_edge(scan_markets, monitor_trends)
root.order.add_edge(scan_markets, ai_analytics)
root.order.add_edge(scan_markets, pivot_plans)
root.order.add_edge(scan_markets, cycle_renewal)

# The final result is 'root'