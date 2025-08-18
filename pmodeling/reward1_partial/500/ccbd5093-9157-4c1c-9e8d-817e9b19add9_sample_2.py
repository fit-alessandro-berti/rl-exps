import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[conduct_analysis, review_ethics])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[identify_partners, pivot_plans])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[align_strategy, monitor_trends])
loop = OperatorPOWL(operator=Operator.LOOP, children=[scan_markets, host_workshops, form_teams, develop_prototypes, simulate_tests, collect_feedback, xor1])
root = StrictPartialOrder(nodes=[loop, xor2, xor3, cycle_renewal])

# Add edges to the partial order
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(xor2, cycle_renewal)
root.order.add_edge(xor3, cycle_renewal)

print(root)