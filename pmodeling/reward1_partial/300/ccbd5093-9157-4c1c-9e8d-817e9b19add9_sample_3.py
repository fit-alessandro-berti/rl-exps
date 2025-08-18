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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[review_ethics, identify_partners])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conduct_analysis, align_strategy])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[launch_pilots, monitor_trends])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ai_analytics, pivot_plans])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[scan_markets, host_workshops, form_teams, develop_prototypes, simulate_tests, collect_feedback, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor3, xor4, cycle_renewal])

root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop1)

print(root)