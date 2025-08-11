import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
Skip = SilentTransition()

# Define the workflow
# Material Sourcing
material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[MaterialSourcing, Skip])
# Supplier Audit
supplier_audit = OperatorPOWL(operator=Operator.LOOP, children=[SupplierAudit, CredentialVerify])
# Design Concept
design_concept = OperatorPOWL(operator=Operator.XOR, children=[DesignConcept, Skip])
# Prototype Build
prototype_build = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, QualityReview])
# Custom Approvals
custom_approvals = OperatorPOWL(operator=Operator.XOR, children=[CustomApprovals, Skip])
# Inventory Adjust
inventory_adjust = OperatorPOWL(operator=Operator.LOOP, children=[InventoryAdjust, Skip])
# Production Sync
production_sync = OperatorPOWL(operator=Operator.XOR, children=[ProductionSync, Skip])
# Shipping Plan
shipping_plan = OperatorPOWL(operator=Operator.XOR, children=[ShippingPlan, Skip])
# Compliance Check
compliance_check = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, Skip])
# Feedback Loop
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[FeedbackLoop, Skip])
# Market Target
market_target = OperatorPOWL(operator=Operator.XOR, children=[MarketTarget, Skip])
# Order Fulfill
order_fulfill = OperatorPOWL(operator=Operator.XOR, children=[OrderFulfill, Skip])
# Sustainability
sustainability = OperatorPOWL(operator=Operator.XOR, children=[Sustainability, Skip])
# Customer Engage
customer_engage = OperatorPOWL(operator=Operator.XOR, children=[CustomerEngage, Skip])

# Define the partial order
root = StrictPartialOrder(nodes=[material_sourcing, supplier_audit, design_concept, prototype_build, custom_approvals, inventory_adjust, production_sync, shipping_plan, compliance_check, feedback_loop, market_target, order_fulfill, sustainability, customer_engage])
root.order.add_edge(material_sourcing, supplier_audit)
root.order.add_edge(supplier_audit, credential_verify)
root.order.add_edge(supplier_audit, design_concept)
root.order.add_edge(design_concept, prototype_build)
root.order.add_edge(prototype_build, quality_review)
root.order.add_edge(prototype_build, custom_approvals)
root.order.add_edge(custom_approvals, inventory_adjust)
root.order.add_edge(inventory_adjust, production_sync)
root.order.add_edge(production_sync, shipping_plan)
root.order.add_edge(shipping_plan, compliance_check)
root.order.add_edge(compliance_check, feedback_loop)
root.order.add_edge(feedback_loop, market_target)
root.order.add_edge(market_target, order_fulfill)
root.order.add_edge(order_fulfill, sustainability)
root.order.add_edge(sustainability, customer_engage)