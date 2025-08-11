import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names as provided
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

# Define silent transitions (e.g., no action required)
Skip = SilentTransition()

# Define control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ConflictCheck, Skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[FraudScan, Skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[RewardAdjust, Skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[RedemptionVerify, Skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[PartnerSync, Skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[BehaviorAnalyze, Skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[AsyncUpdate, Skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[RollbackTrigger, Skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, Skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[NotificationSend, Skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[UserFeedback, Skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[ReportGenerate, Skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[SystemAudit, Skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    DataCollection,
    PointAggregation,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7,
    xor8,
    xor9,
    xor10,
    xor11,
    xor12,
    xor13
])

# Define dependencies (edges) between nodes
root.order.add_edge(DataCollection, PointAggregation)
root.order.add_edge(PointAggregation, xor1)
root.order.add_edge(PointAggregation, xor2)
root.order.add_edge(PointAggregation, xor3)
root.order.add_edge(PointAggregation, xor4)
root.order.add_edge(PointAggregation, xor5)
root.order.add_edge(PointAggregation, xor6)
root.order.add_edge(PointAggregation, xor7)
root.order.add_edge(PointAggregation, xor8)
root.order.add_edge(PointAggregation, xor9)
root.order.add_edge(PointAggregation, xor10)
root.order.add_edge(PointAggregation, xor11)
root.order.add_edge(PointAggregation, xor12)
root.order.add_edge(PointAggregation, xor13)

print(root)