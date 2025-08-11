import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[point_aggregation, conflict_check, fraud_scan, reward_adjust, redemption_verify])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[behavior_analyze, async_update, rollback_trigger, compliance_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[notification_send, user_feedback, report_generate, system_audit])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[partner_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_collection])

# Create the root model
root = StrictPartialOrder(nodes=[xor1, xor2, loop1, loop2, loop3])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop1)
root.order.add_edge(loop3, loop2)