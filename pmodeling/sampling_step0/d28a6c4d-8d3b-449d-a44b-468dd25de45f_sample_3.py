import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define exclusive choice nodes
idea_fusion_loop = OperatorPOWL(operator=Operator.XOR, children=[trend_sensing, skip])
prototype_loop = OperatorPOWL(operator=Operator.XOR, children=[idea_fusion, skip])
ip_loop = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, skip])
compliance_loop = OperatorPOWL(operator=Operator.XOR, children=[ip_analysis, skip])
partner_loop = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
user_loop = OperatorPOWL(operator=Operator.XOR, children=[partner_setup, skip])
scale_loop = OperatorPOWL(operator=Operator.XOR, children=[user_profiling, skip])
risk_loop = OperatorPOWL(operator=Operator.XOR, children=[launch_prep, skip])
demand_loop = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
agile_loop = OperatorPOWL(operator=Operator.XOR, children=[scale_planning, skip])

# Define loop nodes
idea_fusion_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[idea_fusion_loop, prototype_loop])
prototype_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[prototype_loop, ip_loop])
ip_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[ip_loop, compliance_loop])
compliance_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[compliance_loop, partner_loop])
partner_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[partner_loop, user_loop])
user_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[user_loop, scale_loop])
scale_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[scale_loop, risk_loop])
risk_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[risk_loop, demand_loop])
demand_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[demand_loop, agile_loop])
agile_loop_node = OperatorPOWL(operator=Operator.LOOP, children=[agile_loop, agile_adjust])

# Define root POWL model
root = StrictPartialOrder(nodes=[idea_fusion_loop_node, prototype_loop_node, ip_loop_node, compliance_loop_node, partner_loop_node, user_loop_node, scale_loop_node, risk_loop_node, demand_loop_node, agile_loop_node])
root.order.add_edge(idea_fusion_loop_node, prototype_loop_node)
root.order.add_edge(prototype_loop_node, ip_loop_node)
root.order.add_edge(ip_loop_node, compliance_loop_node)
root.order.add_edge(compliance_loop_node, partner_loop_node)
root.order.add_edge(partner_loop_node, user_loop_node)
root.order.add_edge(user_loop_node, scale_loop_node)
root.order.add_edge(scale_loop_node, risk_loop_node)
root.order.add_edge(risk_loop_node, demand_loop_node)
root.order.add_edge(demand_loop_node, agile_loop_node)
root.order.add_edge(agile_loop_node, agile_adjust)

print(root)