import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    DataAggregation,
    AnomalyDetect,
    RiskAssess,
    DemandModel,
    StakeholderSync,
    AutoNegotiate,
    InventoryOptimize,
    ContingencyPlan,
    ResourceAllocate,
    SustainabilityCheck,
    ComplianceVerify,
    ImpactScore,
    DistributionPlan,
    FeedbackLoop,
    PerformanceAudit,
    ScheduleExecute
])

xor = OperatorPOWL(operator=Operator.XOR, children=[ScheduleExecute, skip])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)