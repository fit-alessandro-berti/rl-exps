from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
DataCollection = Transition(label='Data Collection')
PointAggregation = Transition(label='Point Aggregation')
ConflictCheck = Transition(label='Conflict Check')
FraudScan = Transition(label='Fraud Scan')
RewardAdjust = Transition(label='Reward Adjust')
RedemptionVerify = Transition(label='Redemption Verify')
PartnerSync = Transition(label='Partner Sync')
BehaviorAnalyze = Transition(label='Behavior Analyze')
AsyncUpdate = Transition(label='Async Update')
RollbackTrigger = Transition(label='Rollback Trigger')
ComplianceCheck = Transition(label='Compliance Check')
NotificationSend = Transition(label='Notification Send')
UserFeedback = Transition(label='User Feedback')
ReportGenerate = Transition(label='Report Generate')
SystemAudit = Transition(label='System Audit')

# Define the POWL model
root = StrictPartialOrder(nodes=[DataCollection, PointAggregation, ConflictCheck, FraudScan, RewardAdjust, RedemptionVerify, PartnerSync, BehaviorAnalyze, AsyncUpdate, RollbackTrigger, ComplianceCheck, NotificationSend, UserFeedback, ReportGenerate, SystemAudit])

# Define the dependencies
root.order.add_edge(DataCollection, PointAggregation)
root.order.add_edge(PointAggregation, ConflictCheck)
root.order.add_edge(ConflictCheck, FraudScan)
root.order.add_edge(FraudScan, RewardAdjust)
root.order.add_edge(RewardAdjust, RedemptionVerify)
root.order.add_edge(RedemptionVerify, PartnerSync)
root.order.add_edge(PartnerSync, BehaviorAnalyze)
root.order.add_edge(BehaviorAnalyze, AsyncUpdate)
root.order.add_edge(AsyncUpdate, RollbackTrigger)
root.order.add_edge(RollbackTrigger, ComplianceCheck)
root.order.add_edge(ComplianceCheck, NotificationSend)
root.order.add_edge(NotificationSend, UserFeedback)
root.order.add_edge(UserFeedback, ReportGenerate)
root.order.add_edge(ReportGenerate, SystemAudit)

# Print the model
print(root)