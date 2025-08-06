import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define loops and XORs
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collection])
conflict_loop = OperatorPOWL(operator=Operator.LOOP, children=[conflict_check])
fraud_loop = OperatorPOWL(operator=Operator.LOOP, children=[fraud_scan])
reward_loop = OperatorPOWL(operator=Operator.LOOP, children=[reward_adjust])
redemption_loop = OperatorPOWL(operator=Operator.LOOP, children=[redemption_verify])
partner_loop = OperatorPOWL(operator=Operator.LOOP, children=[partner_sync])
behavior_loop = OperatorPOWL(operator=Operator.LOOP, children=[behavior_analyze])
async_loop = OperatorPOWL(operator=Operator.LOOP, children=[async_update])
rollback_loop = OperatorPOWL(operator=Operator.LOOP, children=[rollback_trigger])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check])
notification_loop = OperatorPOWL(operator=Operator.LOOP, children=[notification_send])
user_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[user_feedback])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_generate])
system_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_audit])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[partner_loop, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[behavior_loop, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[async_loop, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[rollback_loop, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_loop, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[notification_loop, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[user_feedback_loop, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[report_loop, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[system_audit_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[data_loop, conflict_loop, fraud_loop, reward_loop, redemption_loop, partner_loop, behavior_loop, async_loop, rollback_loop, compliance_loop, notification_loop, user_feedback_loop, report_loop, system_audit_loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(data_loop, conflict_loop)
root.order.add_edge(conflict_loop, fraud_loop)
root.order.add_edge(fraud_loop, reward_loop)
root.order.add_edge(reward_loop, redemption_loop)
root.order.add_edge(partner_loop, behavior_loop)
root.order.add_edge(behavior_loop, async_loop)
root.order.add_edge(async_loop, rollback_loop)
root.order.add_edge(rollback_loop, compliance_loop)
root.order.add_edge(compliance_loop, notification_loop)
root.order.add_edge(notification_loop, user_feedback_loop)
root.order.add_edge(user_feedback_loop, report_loop)
root.order.add_edge(report_loop, system_audit_loop)
root.order.add_edge(data_loop, xor1)
root.order.add_edge(conflict_loop, xor2)
root.order.add_edge(fraud_loop, xor3)
root.order.add_edge(reward_loop, xor4)
root.order.add_edge(redemption_loop, xor5)
root.order.add_edge(partner_loop, xor6)
root.order.add_edge(behavior_loop, xor7)
root.order.add_edge(async_loop, xor8)
root.order.add_edge(rollback_loop, xor9)

# Print the root POWL model
print(root)