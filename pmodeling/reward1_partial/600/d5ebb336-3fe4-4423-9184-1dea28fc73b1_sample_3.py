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

# Define transitions and loop
xor1 = OperatorPOWL(operator=Operator.XOR, children=[fraud_scan, data_collection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conflict_check, point_aggregation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[reward_adjust, redemption_verify])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[partner_sync, behavior_analyze])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[async_update, rollback_trigger])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, notification_send])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[user_feedback, report_generate])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[system_audit, user_feedback])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)