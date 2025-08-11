from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
material_sourcing = Transition(label='Material Sourcing')
supplier_audit = Transition(label='Supplier Audit')
credential_verify = Transition(label='Credential Verify')
design_concept = Transition(label='Design Concept')
prototype_build = Transition(label='Prototype Build')
quality_review = Transition(label='Quality Review')
artisan_assign = Transition(label='Artisan Assign')
batch_scheduling = Transition(label='Batch Scheduling')
custom_approvals = Transition(label='Custom Approvals')
inventory_adjust = Transition(label='Inventory Adjust')
production_sync = Transition(label='Production Sync')
shipping_plan = Transition(label='Shipping Plan')
compliance_check = Transition(label='Compliance Check')
feedback_loop = Transition(label='Feedback Loop')
market_target = Transition(label='Market Target')
order_fulfill = Transition(label='Order Fulfill')
sustainability = Transition(label='Sustainability')
customer_engage = Transition(label='Customer Engage')

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
material_sourcing_node = OperatorPOWL(operator=Operator.CONC, children=[material_sourcing, supplier_audit, credential_verify])
audit_and_verify_node = OperatorPOWL(operator=Operator.CONC, children=[design_concept, prototype_build, quality_review])
assign_artisan_node = OperatorPOWL(operator=Operator.CONC, children=[artisan_assign, batch_scheduling, custom_approvals])
inventory_adjust_node = OperatorPOWL(operator=Operator.CONC, children=[inventory_adjust, production_sync, shipping_plan])
compliance_check_node = OperatorPOWL(operator=Operator.CONC, children=[compliance_check, feedback_loop, market_target])
order_fulfill_node = OperatorPOWL(operator=Operator.CONC, children=[order_fulfill, sustainability, customer_engage])

# Define the root partial order
root = StrictPartialOrder(nodes=[material_sourcing_node, audit_and_verify_node, assign_artisan_node, inventory_adjust_node, compliance_check_node, order_fulfill_node])
root.order.add_edge(material_sourcing_node, audit_and_verify_node)
root.order.add_edge(audit_and_verify_node, assign_artisan_node)
root.order.add_edge(assign_artisan_node, inventory_adjust_node)
root.order.add_edge(inventory_adjust_node, compliance_check_node)
root.order.add_edge(compliance_check_node, order_fulfill_node)

print(root)