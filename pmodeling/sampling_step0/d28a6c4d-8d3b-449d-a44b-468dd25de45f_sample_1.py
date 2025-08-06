import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

trend_sensing = Transition(label='Trend Sensing')
idea_fusion = Transition(label='Idea Fusion')
prototype_build = Transition(label='Prototype Build')
expert_review = Transition(label='Expert Review')
field_testing = Transition(label='Field Testing')
ip_analysis = Transition(label='IP Analysis')
compliance_check = Transition(label='Compliance Check')
partner_setup = Transition(label='Partner Setup')
user_profiling = Transition(label='User Profiling')
launch_prep = Transition(label='Launch Prep')
feedback_loop = Transition(label='Feedback Loop')
scale_planning = Transition(label='Scale Planning')
risk_assess = Transition(label='Risk Assess')
demand_scan = Transition(label='Demand Scan')
agile_adjust = Transition(label='Agile Adjust')

xor1 = OperatorPOWL(operator=Operator.XOR, children=[partner_setup, user_profiling])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[agile_adjust, demand_scan])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ip_analysis, compliance_check])

loop2 = OperatorPOWL(operator=Operator.LOOP, children=[field_testing, expert_review])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[launch_prep, feedback_loop])

root = StrictPartialOrder(nodes=[trend_sensing, idea_fusion, prototype_build, xor1, xor2, loop1, loop2, xor3])
root.order.add_edge(trend_sensing, idea_fusion)
root.order.add_edge(idea_fusion, prototype_build)
root.order.add_edge(prototype_build, xor1)
root.order.add_edge(prototype_build, xor2)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop2, xor3)