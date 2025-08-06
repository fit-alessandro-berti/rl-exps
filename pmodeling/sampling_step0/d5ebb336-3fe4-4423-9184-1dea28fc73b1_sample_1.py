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

# Define silent transitions
skip = SilentTransition()

# Define loops
async_loop = OperatorPOWL(operator=Operator.LOOP, children=[async_update, rollback_trigger])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, notification_send])

# Define choices
conflict_choice = OperatorPOWL(operator=Operator.XOR, children=[conflict_check, skip])
fraud_choice = OperatorPOWL(operator=Operator.XOR, children=[fraud_scan, skip])
reward_choice = OperatorPOWL(operator=Operator.XOR, children=[reward_adjust, skip])
redemption_choice = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    data_collection, point_aggregation, behavior_analyze, partner_sync, async_loop, conflict_choice, fraud_choice,
    reward_choice, redemption_choice, compliance_loop, notification_send, system_audit, report_generate
])

# Define the partial order
root.order.add_edge(data_collection, point_aggregation)
root.order.add_edge(point_aggregation, behavior_analyze)
root.order.add_edge(behavior_analyze, partner_sync)
root.order.add_edge(partner_sync, async_loop)
root.order.add_edge(async_loop, compliance_loop)
root.order.add_edge(conflict_choice, async_loop)
root.order.add_edge(fraud_choice, async_loop)
root.order.add_edge(reward_choice, async_loop)
root.order.add_edge(redemption_choice, async_loop)
root.order.add_edge(compliance_loop, notification_send)
root.order.add_edge(notification_send, system_audit)
root.order.add_edge(system_audit, report_generate)

# Print the root
print(root)