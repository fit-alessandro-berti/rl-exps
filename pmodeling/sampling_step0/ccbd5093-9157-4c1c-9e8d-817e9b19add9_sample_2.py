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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[scan_markets, host_workshops])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[form_teams, develop_prototypes])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[simulate_tests, collect_feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[review_ethics, conduct_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[identify_partners, align_strategy])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[launch_pilots, monitor_trends])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[ai_analytics, pivot_plans])

loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

root = StrictPartialOrder(nodes=[loop, cycle_renewal])
root.order.add_edge(loop, cycle_renewal)