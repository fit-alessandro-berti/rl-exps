import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
data_collection = Transition(label='Data Collection')
point_aggregation = Transition(label='Point Aggregation')
conflict_check = Transition(label='Conflict Check')
fraud_scan = Transition(label='Fraud Scan')
reward_adjust = Transition(label='Reward Adjust')
redemption_verify = Transition(label='Redemption Verify')
partner_sync = Transition(label='Partner Sync')
behavior_analyze = Transition(label='Behavior Analyze')
async_update = Transition(label='Async Update')
rollback_trigger = Transition(label='Rollback Trigger')
compliance_check = Transition(label='Compliance Check')
notification_send = Transition(label='Notification Send')
user_feedback = Transition(label='User Feedback')
report_generate = Transition(label='Report Generate')
system_audit = Transition(label='System Audit')

# Define the partial order
root = StrictPartialOrder(nodes=[data_collection, point_aggregation, conflict_check, fraud_scan, reward_adjust, redemption_verify, partner_sync, behavior_analyze, async_update, rollback_trigger, compliance_check, notification_send, user_feedback, report_generate, system_audit])

# Define the dependencies
root.order.add_edge(data_collection, point_aggregation)
root.order.add_edge(point_aggregation, conflict_check)
root.order.add_edge(conflict_check, fraud_scan)
root.order.add_edge(fraud_scan, reward_adjust)
root.order.add_edge(reward_adjust, redemption_verify)
root.order.add_edge(redemption_verify, partner_sync)
root.order.add_edge(partner_sync, behavior_analyze)
root.order.add_edge(behavior_analyze, async_update)
root.order.add_edge(async_update, rollback_trigger)
root.order.add_edge(rollback_trigger, compliance_check)
root.order.add_edge(compliance_check, notification_send)
root.order.add_edge(notification_send, user_feedback)
root.order.add_edge(user_feedback, report_generate)
root.order.add_edge(report_generate, system_audit)

# Print the root POWL model
print(root)