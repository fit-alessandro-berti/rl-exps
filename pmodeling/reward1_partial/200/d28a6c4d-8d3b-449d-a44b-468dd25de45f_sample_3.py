import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[trend_sensing, idea_fusion])
xor = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, expert_review])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[field_testing, ip_analysis])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, partner_setup])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[user_profiling, launch_prep])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, scale_planning])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, demand_scan])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[agile_adjust, skip])

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[loop, xor, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_7)