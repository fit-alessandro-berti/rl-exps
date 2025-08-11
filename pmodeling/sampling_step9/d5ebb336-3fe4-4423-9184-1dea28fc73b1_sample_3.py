import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, point_aggregation, conflict_check, fraud_scan, reward_adjust, redemption_verify, partner_sync, behavior_analyze])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[async_update, rollback_trigger, compliance_check])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[notification_send, user_feedback, report_generate, system_audit])

# Define exclusive choices
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])

# Create the root model
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3])

# Define the order of execution
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_1, xor_3)
root.order.add_edge(xor_2, xor_3)

# Print the root model
print(root)