import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[trend_sensing, idea_fusion])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, expert_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[field_testing, ip_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, partner_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[user_profiling, launch_prep])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, scale_planning])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, demand_scan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[agile_adjust, ])

# Define the POWL root
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)