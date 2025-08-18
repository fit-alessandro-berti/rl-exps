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

# Define the workflow model
xor = OperatorPOWL(operator=Operator.XOR, children=[scan_markets, host_workshops, form_teams, develop_prototypes, simulate_tests, collect_feedback, review_ethics, conduct_analysis, identify_partners, align_strategy, launch_pilots, monitor_trends, ai_analytics, pivot_plans])
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, cycle_renewal])

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor)