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
xor2 = OperatorPOWL(operator=Operator.XOR, children=[scale_planning, risk_assess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[demand_scan, agile_adjust])

root = StrictPartialOrder(nodes=[trend_sensing, idea_fusion, prototype_build, expert_review, field_testing, ip_analysis, compliance_check, xor1, xor2, xor3])
root.order.add_edge(trend_sensing, idea_fusion)
root.order.add_edge(idea_fusion, prototype_build)
root.order.add_edge(prototype_build, expert_review)
root.order.add_edge(expert_review, field_testing)
root.order.add_edge(field_testing, ip_analysis)
root.order.add_edge(ip_analysis, compliance_check)
root.order.add_edge(compliance_check, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, agile_adjust)

print(root)