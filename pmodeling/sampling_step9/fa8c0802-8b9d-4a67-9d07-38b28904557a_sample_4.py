import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
DataAggregation = Transition(label='Data Aggregation')
AnomalyDetect = Transition(label='Anomaly Detect')
RiskAssess = Transition(label='Risk Assess')
DemandModel = Transition(label='Demand Model')
StakeholderSync = Transition(label='Stakeholder Sync')
AutoNegotiate = Transition(label='Auto Negotiate')
InventoryOptimize = Transition(label='Inventory Optimize')
ContingencyPlan = Transition(label='Contingency Plan')
ResourceAllocate = Transition(label='Resource Allocate')
SustainabilityCheck = Transition(label='Sustainability Check')
ComplianceVerify = Transition(label='Compliance Verify')
ImpactScore = Transition(label='Impact Score')
DistributionPlan = Transition(label='Distribution Plan')
FeedbackLoop = Transition(label='Feedback Loop')
PerformanceAudit = Transition(label='Performance Audit')
ScheduleExecute = Transition(label='Schedule Execute')

# Define the silent transitions
skip = SilentTransition()

# Define the choice nodes
xor = OperatorPOWL(operator=Operator.XOR, children=[RiskAssess, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SustainabilityCheck, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ComplianceVerify, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ImpactScore, skip])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DataAggregation, AnomalyDetect])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[StakeholderSync, AutoNegotiate])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[InventoryOptimize, ContingencyPlan])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[ResourceAllocate, FeedbackLoop])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[DistributionPlan, PerformanceAudit])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, xor, xor2, xor3, xor4])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, ScheduleExecute)

print(root)