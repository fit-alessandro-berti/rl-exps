import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
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

# Define the partial order
root = StrictPartialOrder(nodes=[Data_Collection, Point_Aggregation, Conflict_Check, Fraud_Scan, Reward_Adjust, Redemption_Verify, Partner_Sync, Behavior_Analyze, Async_Update, Rollback_Trigger, Compliance_Check, Notification_Send, User_Feedback, Report_Generate, System_Audit])