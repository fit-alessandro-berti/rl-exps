import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
trend_scan = Transition(label='Trend Scan')
opportunity_map = Transition(label='Opportunity Map')
expert_gather = Transition(label='Expert Gather')
idea_sprint = Transition(label='Idea Sprint')
proto_build = Transition(label='Proto Build')
user_feedback = Transition(label='User Feedback')
risk_review = Transition(label='Risk Review')
ip_audit = Transition(label='IP Audit')
pilot_launch = Transition(label='Pilot Launch')
stakeholder_meet = Transition(label='Stakeholder Meet')
resource_shift = Transition(label='Resource Shift')
scale_up = Transition(label='Scale Up')
impact_assess = Transition(label='Impact Assess')
knowledge_share = Transition(label='Knowledge Share')
monitor_trends = Transition(label='Monitor Trends')

# Define the root Partial Order
root = StrictPartialOrder(nodes=[
    trend_scan,
    opportunity_map,
    expert_gather,
    idea_sprint,
    proto_build,
    user_feedback,
    risk_review,
    ip_audit,
    pilot_launch,
    stakeholder_meet,
    resource_shift,
    scale_up,
    impact_assess,
    knowledge_share,
    monitor_trends
])

# Define the dependencies in the Partial Order
root.order.add_edge(trend_scan, opportunity_map)
root.order.add_edge(trend_scan, expert_gather)
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(trend_scan, proto_build)
root.order.add_edge(trend_scan, user_feedback)
root.order.add_edge(trend_scan, risk_review)
root.order.add_edge(trend_scan, ip_audit)
root.order.add_edge(trend_scan, pilot_launch)
root.order.add_edge(trend_scan, stakeholder_meet)
root.order.add_edge(trend_scan, resource_shift)
root.order.add_edge(trend_scan, scale_up)
root.order.add_edge(trend_scan, impact_assess)
root.order.add_edge(trend_scan, knowledge_share)
root.order.add_edge(trend_scan, monitor_trends)

# The final result is stored in 'root'