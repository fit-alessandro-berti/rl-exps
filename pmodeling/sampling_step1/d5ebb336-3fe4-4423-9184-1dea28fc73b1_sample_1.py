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

# Define the process model using POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[partner_sync, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[system_audit, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, skip])

root = StrictPartialOrder(nodes=[data_collection, point_aggregation, conflict_check, fraud_scan, reward_adjust, redemption_verify, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(data_collection, point_aggregation)
root.order.add_edge(point_aggregation, conflict_check)
root.order.add_edge(conflict_check, fraud_scan)
root.order.add_edge(fraud_scan, reward_adjust)
root.order.add_edge(reward_adjust, redemption_verify)
root.order.add_edge(redemption_verify, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)