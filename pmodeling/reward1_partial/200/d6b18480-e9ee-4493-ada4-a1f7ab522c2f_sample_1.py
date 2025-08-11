import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MaterialSourcing = Transition(label='Material Sourcing')
ForagerDispatch = Transition(label='Forager Dispatch')
AuthenticityCheck = Transition(label='Authenticity Check')
BatchScheduling = Transition(label='Batch Scheduling')
ArtisanAllocation = Transition(label='Artisan Allocation')
CraftAssembly = Transition(label='Craft Assembly')
QualityInspection = Transition(label='Quality Inspection')
BlockchainUpdate = Transition(label='Blockchain Update')
DemandForecast = Transition(label='Demand Forecast')
PriceAdjustment = Transition(label='Price Adjustment')
ComplianceReview = Transition(label='Compliance Review')
LogisticsPlanning = Transition(label='Logistics Planning')
DistributorSync = Transition(label='Distributor Sync')
CustomerFeedback = Transition(label='Customer Feedback')
ProductRefinement = Transition(label='Product Refinement')
ReputationAudit = Transition(label='Reputation Audit')
SeasonalReview = Transition(label='Seasonal Review')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, AuthenticityCheck])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, BatchScheduling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, ArtisanAllocation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, CraftAssembly])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip, QualityInspection])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[skip, BlockchainUpdate])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[skip, DemandForecast])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[skip, PriceAdjustment])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[skip, ComplianceReview])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[skip, LogisticsPlanning])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[skip, DistributorSync])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[skip, CustomerFeedback])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[skip, ProductRefinement])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[skip, ReputationAudit])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[skip, SeasonalReview])

root = StrictPartialOrder(nodes=[
    MaterialSourcing,
    ForagerDispatch,
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
    xor13,
    xor14,
    xor15
])
root.order.add_edge(MaterialSourcing, ForagerDispatch)
root.order.add_edge(ForagerDispatch, xor1)
root.order.add_edge(xor1, AuthenticityCheck)
root.order.add_edge(AuthenticityCheck, xor2)
root.order.add_edge(xor2, BatchScheduling)
root.order.add_edge(BatchScheduling, xor3)
root.order.add_edge(xor3, ArtisanAllocation)
root.order.add_edge(ArtisanAllocation, xor4)
root.order.add_edge(xor4, CraftAssembly)
root.order.add_edge(CraftAssembly, xor5)
root.order.add_edge(xor5, QualityInspection)
root.order.add_edge(QualityInspection, xor6)
root.order.add_edge(xor6, BlockchainUpdate)
root.order.add_edge(BlockchainUpdate, xor7)
root.order.add_edge(xor7, DemandForecast)
root.order.add_edge(DemandForecast, xor8)
root.order.add_edge(xor8, PriceAdjustment)
root.order.add_edge(PriceAdjustment, xor9)
root.order.add_edge(xor9, ComplianceReview)
root.order.add_edge(ComplianceReview, xor10)
root.order.add_edge(xor10, LogisticsPlanning)
root.order.add_edge(LogisticsPlanning, xor11)
root.order.add_edge(xor11, DistributorSync)
root.order.add_edge(DistributorSync, xor12)
root.order.add_edge(xor12, CustomerFeedback)
root.order.add_edge(CustomerFeedback, xor13)
root.order.add_edge(xor13, ProductRefinement)
root.order.add_edge(ProductRefinement, xor14)
root.order.add_edge(xor14, ReputationAudit)
root.order.add_edge(ReputationAudit, xor15)
root.order.add_edge(xor15, SeasonalReview)