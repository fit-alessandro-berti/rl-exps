import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity transition
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
root = StrictPartialOrder(nodes=[
    data_collection, point_aggregation, conflict_check, fraud_scan,
    reward_adjust, redemption_verify, partner_sync, behavior_analyze,
    async_update, rollback_trigger, compliance_check, notification_send,
    user_feedback, report_generate, system_audit
])

# Define the dependencies (if any)
# In this case, there are no explicit dependencies mentioned, so we assume all activities are concurrent.

# Save the final result in the variable 'root'
print(root)