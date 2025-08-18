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

# Define silent transitions for each activity
skip_trend_sensing = SilentTransition()
skip_idea_fusion = SilentTransition()
skip_prototype_build = SilentTransition()
skip_expert_review = SilentTransition()
skip_field_testing = SilentTransition()
skip_ip_analysis = SilentTransition()
skip_compliance_check = SilentTransition()
skip_partner_setup = SilentTransition()
skip_user_profiling = SilentTransition()
skip_launch_prep = SilentTransition()
skip_feedback_loop = SilentTransition()
skip_scale_planning = SilentTransition()
skip_risk_assess = SilentTransition()
skip_demand_scan = SilentTransition()
skip_agile_adjust = SilentTransition()

# Define exclusive choice for trend sensing and idea fusion
xor_trend_idea = OperatorPOWL(operator=Operator.XOR, children=[trend_sensing, idea_fusion])

# Define exclusive choice for expert review and field testing
xor_expert_field = OperatorPOWL(operator=Operator.XOR, children=[expert_review, field_testing])

# Define exclusive choice for IP analysis and compliance check
xor_ip_compliance = OperatorPOWL(operator=Operator.XOR, children=[ip_analysis, compliance_check])

# Define exclusive choice for partner setup and user profiling
xor_partner_user = OperatorPOWL(operator=Operator.XOR, children=[partner_setup, user_profiling])

# Define exclusive choice for launch prep and feedback loop
xor_launch_feedback = OperatorPOWL(operator=Operator.XOR, children=[launch_prep, feedback_loop])

# Define exclusive choice for scale planning and risk assess
xor_scale_risk = OperatorPOWL(operator=Operator.XOR, children=[scale_planning, risk_assess])

# Define exclusive choice for demand scan and agile adjust
xor_demand_agile = OperatorPOWL(operator=Operator.XOR, children=[demand_scan, agile_adjust])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    xor_trend_idea,
    xor_expert_field,
    xor_ip_compliance,
    xor_partner_user,
    xor_launch_feedback,
    xor_scale_risk,
    xor_demand_agile
])

# Define the dependencies between nodes
root.order.add_edge(xor_trend_idea, xor_expert_field)
root.order.add_edge(xor_expert_field, xor_ip_compliance)
root.order.add_edge(xor_ip_compliance, xor_partner_user)
root.order.add_edge(xor_partner_user, xor_launch_feedback)
root.order.add_edge(xor_launch_feedback, xor_scale_risk)
root.order.add_edge(xor_scale_risk, xor_demand_agile)