import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Data Collection', 'Point Aggregation', 'Conflict Check', 'Fraud Scan', 'Reward Adjust', 'Redemption Verify', 'Partner Sync', 'Behavior Analyze', 'Async Update', 'Rollback Trigger', 'Compliance Check', 'Notification Send', 'User Feedback', 'Report Generate', 'System Audit']
transitions = [Transition(label=activity) for activity in activities]

# Define the process
data_collection = transitions[0]
point_aggregation = transitions[1]
conflict_check = transitions[2]
fraud_scan = transitions[3]
reward_adjust = transitions[4]
redemption_verify = transitions[5]
partner_sync = transitions[6]
behavior_analyze = transitions[7]
async_update = transitions[8]
rollback_trigger = transitions[9]
compliance_check = transitions[10]
notification_send = transitions[11]
user_feedback = transitions[12]
report_generate = transitions[13]
system_audit = transitions[14]

# Define the partial order
root = StrictPartialOrder(nodes=[data_collection, point_aggregation, conflict_check, fraud_scan, reward_adjust, redemption_verify, partner_sync, behavior_analyze, async_update, rollback_trigger, compliance_check, notification_send, user_feedback, report_generate, system_audit])
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

print(root)