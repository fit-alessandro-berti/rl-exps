from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order model
root = StrictPartialOrder(nodes=[trend_sensing, idea_fusion, prototype_build, expert_review, field_testing, ip_analysis, compliance_check, partner_setup, user_profiling, launch_prep, feedback_loop, scale_planning, risk_assess, demand_scan, agile_adjust])

# Define the partial order dependencies
root.order.add_edge(trend_sensing, idea_fusion)
root.order.add_edge(idea_fusion, prototype_build)
root.order.add_edge(prototype_build, expert_review)
root.order.add_edge(expert_review, field_testing)
root.order.add_edge(field_testing, ip_analysis)
root.order.add_edge(ip_analysis, compliance_check)
root.order.add_edge(compliance_check, partner_setup)
root.order.add_edge(partner_setup, user_profiling)
root.order.add_edge(user_profiling, launch_prep)
root.order.add_edge(launch_prep, feedback_loop)
root.order.add_edge(feedback_loop, scale_planning)
root.order.add_edge(scale_planning, risk_assess)
root.order.add_edge(risk_assess, demand_scan)
root.order.add_edge(demand_scan, agile_adjust)

# The final result is stored in the variable 'root'