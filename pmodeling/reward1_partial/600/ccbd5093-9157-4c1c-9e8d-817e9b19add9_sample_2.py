import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

xor = OperatorPOWL(operator=Operator.XOR, children=[develop_prototypes, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[scan_markets, host_workshops, form_teams, xor])

root = StrictPartialOrder(nodes=[loop, align_strategy, launch_pilots, monitor_trends, ai_analytics, pivot_plans, cycle_renewal])
root.order.add_edge(loop, align_strategy)
root.order.add_edge(align_strategy, launch_pilots)
root.order.add_edge(launch_pilots, monitor_trends)
root.order.add_edge(monitor_trends, ai_analytics)
root.order.add_edge(ai_analytics, pivot_plans)
root.order.add_edge(pivot_plans, cycle_renewal)
root.order.add_edge(cycle_renewal, align_strategy)