from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
MaterialSourcing = Transition(label='Material Sourcing')
SupplierAudit = Transition(label='Supplier Audit')
CredentialVerify = Transition(label='Credential Verify')
DesignConcept = Transition(label='Design Concept')
PrototypeBuild = Transition(label='Prototype Build')
QualityReview = Transition(label='Quality Review')
ArtisanAssign = Transition(label='Artisan Assign')
BatchScheduling = Transition(label='Batch Scheduling')
CustomApprovals = Transition(label='Custom Approvals')
InventoryAdjust = Transition(label='Inventory Adjust')
ProductionSync = Transition(label='Production Sync')
ShippingPlan = Transition(label='Shipping Plan')
ComplianceCheck = Transition(label='Compliance Check')
FeedbackLoop = Transition(label='Feedback Loop')
MarketTarget = Transition(label='Market Target')
OrderFulfill = Transition(label='Order Fulfill')
Sustainability = Transition(label='Sustainability')
CustomerEngage = Transition(label='Customer Engage')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    MaterialSourcing, SupplierAudit, CredentialVerify, DesignConcept, PrototypeBuild, QualityReview,
    ArtisanAssign, BatchScheduling, CustomApprovals, InventoryAdjust, ProductionSync, ShippingPlan,
    ComplianceCheck, FeedbackLoop, MarketTarget, OrderFulfill, Sustainability, CustomerEngage
])

# Define the dependencies (partial order)
root.order.add_edge(MaterialSourcing, SupplierAudit)
root.order.add_edge(SupplierAudit, CredentialVerify)
root.order.add_edge(CredentialVerify, DesignConcept)
root.order.add_edge(DesignConcept, PrototypeBuild)
root.order.add_edge(PrototypeBuild, QualityReview)
root.order.add_edge(QualityReview, ArtisanAssign)
root.order.add_edge(ArtisanAssign, BatchScheduling)
root.order.add_edge(BatchScheduling, CustomApprovals)
root.order.add_edge(CustomApprovals, InventoryAdjust)
root.order.add_edge(InventoryAdjust, ProductionSync)
root.order.add_edge(ProductionSync, ShippingPlan)
root.order.add_edge(ShippingPlan, ComplianceCheck)
root.order.add_edge(ComplianceCheck, FeedbackLoop)
root.order.add_edge(FeedbackLoop, MarketTarget)
root.order.add_edge(MarketTarget, OrderFulfill)
root.order.add_edge(OrderFulfill, Sustainability)
root.order.add_edge(Sustainability, CustomerEngage)

# Print the root POWL model
print(root)