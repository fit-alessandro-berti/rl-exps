import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[async_update, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[rollback_trigger, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[user_feedback, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[system_audit, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[partner_sync])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2, xor3, xor4, xor5, xor6, loop])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor7])
root.order.add_edge(xor7, xor1)
root.order.add_edge(xor7, xor2)
root.order.add_edge(xor7, xor3)
root.order.add_edge(xor7, xor4)
root.order.add_edge(xor7, xor5)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor7, loop)