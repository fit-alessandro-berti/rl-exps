import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Sourcing, verification, and artisan assignment
source_verify_artisan = OperatorPOWL(operator=Operator.XOR, children=[MaterialSourcing, SupplierAudit, CredentialVerify, ArtisanAssign])

# Prototype build and quality review
prototype_quality = OperatorPOWL(operator=Operator.XOR, children=[PrototypeBuild, QualityReview])

# Custom approvals and inventory adjustment
custom_approval_inventory = OperatorPOWL(operator=Operator.XOR, children=[CustomApprovals, InventoryAdjust])

# Production synchronization and shipping plan
production_sync_shipping = OperatorPOWL(operator=Operator.XOR, children=[ProductionSync, ShippingPlan])

# Compliance check and feedback loop
compliance_feedback = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, FeedbackLoop])

# Market target and order fulfillment
market_target_order = OperatorPOWL(operator=Operator.XOR, children=[MarketTarget, OrderFulfill])

# Sustainability and customer engagement
sustainability_customer = OperatorPOWL(operator=Operator.XOR, children=[Sustainability, CustomerEngage])

# Loops and concurrent activities
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[source_verify_artisan])
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_quality])
custom_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_approval_inventory])
production_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[production_sync_shipping])
compliance_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_feedback])
market_target_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_target_order])
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_customer])

root = StrictPartialOrder(nodes=[sourcing_loop, prototype_loop, custom_approval_loop, production_sync_loop, compliance_feedback_loop, market_target_loop, sustainability_loop])
root.order.add_edge(sourcing_loop, prototype_loop)
root.order.add_edge(prototype_loop, custom_approval_loop)
root.order.add_edge(custom_approval_loop, production_sync_loop)
root.order.add_edge(production_sync_loop, compliance_feedback_loop)
root.order.add_edge(compliance_feedback_loop, market_target_loop)
root.order.add_edge(market_target_loop, sustainability_loop)