import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[conduct_analysis, review_ethics])
loop = OperatorPOWL(operator=Operator.LOOP, children=[scan_markets, host_workshops, form_teams, develop_prototypes, simulate_tests, collect_feedback, xor])
partial_order = StrictPartialOrder(nodes=[loop, identify_partners, align_strategy, launch_pilots, monitor_trends, ai_analytics, pivot_plans, cycle_renewal])
partial_order.order.add_edge(loop, identify_partners)
partial_order.order.add_edge(loop, align_strategy)
partial_order.order.add_edge(identify_partners, launch_pilots)
partial_order.order.add_edge(launch_pilots, monitor_trends)
partial_order.order.add_edge(monitor_trends, ai_analytics)
partial_order.order.add_edge(ai_analytics, pivot_plans)
partial_order.order.add_edge(pivot_plans, cycle_renewal)

# Define the root
root = partial_order