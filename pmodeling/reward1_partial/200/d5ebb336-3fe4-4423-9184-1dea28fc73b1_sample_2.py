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

# Define the silent transitions
skip = SilentTransition()

# Define the process tree
xor = OperatorPOWL(operator=Operator.XOR, children=[partner_sync, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[user_feedback, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[system_audit, skip])

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[behavior_analyze, async_update, rollback_trigger, compliance_check])

# Define the partial order
root = StrictPartialOrder(nodes=[data_collection, point_aggregation, conflict_check, fraud_scan, reward_adjust, redemption_verify, xor, xor2, xor3, loop])
root.order.add_edge(data_collection, point_aggregation)
root.order.add_edge(point_aggregation, conflict_check)
root.order.add_edge(conflict_check, fraud_scan)
root.order.add_edge(fraud_scan, reward_adjust)
root.order.add_edge(reward_adjust, redemption_verify)
root.order.add_edge(redemption_verify, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop)
root.order.add_edge(loop, data_collection)

# Print the POWL model
print(root)