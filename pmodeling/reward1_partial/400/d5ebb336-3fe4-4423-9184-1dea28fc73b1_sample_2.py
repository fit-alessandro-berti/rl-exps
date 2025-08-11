import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[fraud_scan, partner_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[rollback_trigger, compliance_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

root = StrictPartialOrder(nodes=[data_collection, point_aggregation, conflict_check, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(data_collection, point_aggregation)
root.order.add_edge(point_aggregation, conflict_check)
root.order.add_edge(conflict_check, xor1)
root.order.add_edge(conflict_check, xor2)
root.order.add_edge(xor1, fraud_scan)
root.order.add_edge(xor1, partner_sync)
root.order.add_edge(xor2, behavior_analyze)
root.order.add_edge(xor2, async_update)
root.order.add_edge(xor3, rollback_trigger)
root.order.add_edge(xor3, compliance_check)
root.order.add_edge(xor4, notification_send)
root.order.add_edge(xor4, user_feedback)
root.order.add_edge(xor5, report_generate)
root.order.add_edge(xor5, system_audit)