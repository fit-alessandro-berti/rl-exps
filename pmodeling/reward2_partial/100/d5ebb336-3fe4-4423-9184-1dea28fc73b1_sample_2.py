import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
Data_Collection = Transition(label='Data Collection')
Point_Aggregation = Transition(label='Point Aggregation')
Conflict_Check = Transition(label='Conflict Check')
Fraud_Scan = Transition(label='Fraud Scan')
Reward_Adjust = Transition(label='Reward Adjust')
Redemption_Verify = Transition(label='Redemption Verify')
Partner_Sync = Transition(label='Partner Sync')
Behavior_Analyze = Transition(label='Behavior Analyze')
Async_Update = Transition(label='Async Update')
Rollback_Trigger = Transition(label='Rollback Trigger')
Compliance_Check = Transition(label='Compliance Check')
Notification_Send = Transition(label='Notification Send')
User_Feedback = Transition(label='User Feedback')
Report_Generate = Transition(label='Report Generate')
System_Audit = Transition(label='System Audit')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Data_Collection, Point_Aggregation, Conflict_Check, Fraud_Scan, Reward_Adjust, Redemption_Verify,
    Partner_Sync, Behavior_Analyze, Async_Update, Rollback_Trigger, Compliance_Check, Notification_Send,
    User_Feedback, Report_Generate, System_Audit
])

# Define the order between nodes (dependencies)
root.order.add_edge(Data_Collection, Point_Aggregation)
root.order.add_edge(Point_Aggregation, Conflict_Check)
root.order.add_edge(Conflict_Check, Fraud_Scan)
root.order.add_edge(Fraud_Scan, Reward_Adjust)
root.order.add_edge(Reward_Adjust, Redemption_Verify)
root.order.add_edge(Redemption_Verify, Partner_Sync)
root.order.add_edge(Partner_Sync, Behavior_Analyze)
root.order.add_edge(Behavior_Analyze, Async_Update)
root.order.add_edge(Async_Update, Rollback_Trigger)
root.order.add_edge(Rollback_Trigger, Compliance_Check)
root.order.add_edge(Compliance_Check, Notification_Send)
root.order.add_edge(Notification_Send, User_Feedback)
root.order.add_edge(User_Feedback, Report_Generate)
root.order.add_edge(Report_Generate, System_Audit)

# Print the root POWL model
print(root)