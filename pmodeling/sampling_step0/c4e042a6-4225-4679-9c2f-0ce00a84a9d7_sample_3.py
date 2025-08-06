import pm4py
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

# Define loops and choices
material_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, supplier_audit, credential_verify])
design_concept_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_concept, prototype_build, quality_review])
artisan_assign_loop = OperatorPOWL(operator=Operator.LOOP, children=[artisan_assign, batch_scheduling])
custom_approvals_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_approvals, inventory_adjust])
production_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[production_sync, shipping_plan])
compliance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, feedback_loop])
market_target_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_target, order_fulfill])
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability, customer_engage])

# Define the root of the process
root = StrictPartialOrder(nodes=[
    material_sourcing_loop,
    design_concept_loop,
    artisan_assign_loop,
    custom_approvals_loop,
    production_sync_loop,
    compliance_check_loop,
    market_target_loop,
    sustainability_loop
])
root.order.add_edge(material_sourcing_loop, design_concept_loop)
root.order.add_edge(material_sourcing_loop, artisan_assign_loop)
root.order.add_edge(material_sourcing_loop, custom_approvals_loop)
root.order.add_edge(design_concept_loop, production_sync_loop)
root.order.add_edge(artisan_assign_loop, production_sync_loop)
root.order.add_edge(custom_approvals_loop, production_sync_loop)
root.order.add_edge(production_sync_loop, compliance_check_loop)
root.order.add_edge(compliance_check_loop, market_target_loop)
root.order.add_edge(market_target_loop, sustainability_loop)
root.order.add_edge(sustainability_loop, customer_engage)