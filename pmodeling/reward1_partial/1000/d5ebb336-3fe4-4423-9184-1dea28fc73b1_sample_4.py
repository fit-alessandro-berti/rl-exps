import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[conflict_check, fraud_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[reward_adjust, redemption_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[partner_sync, behavior_analyze])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[async_update, rollback_trigger])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, notification_send])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[user_feedback, report_generate])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[system_audit, user_feedback])

# Define partial order
root = StrictPartialOrder(nodes=[data_collection, point_aggregation, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(data_collection, point_aggregation)
root.order.add_edge(point_aggregation, xor1)
root.order.add_edge(point_aggregation, xor2)
root.order.add_edge(point_aggregation, xor3)
root.order.add_edge(point_aggregation, xor4)
root.order.add_edge(point_aggregation, xor5)
root.order.add_edge(point_aggregation, xor6)
root.order.add_edge(point_aggregation, xor7)