from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the relationships between activities
root = StrictPartialOrder(nodes=[
    material_sourcing,
    supplier_audit,
    credential_verify,
    design_concept,
    prototype_build,
    quality_review,
    artisan_assign,
    batch_scheduling,
    custom_approvals,
    inventory_adjust,
    production_sync,
    shipping_plan,
    compliance_check,
    feedback_loop,
    market_target,
    order_fulfill,
    sustainability,
    customer_engage
])

# Define the dependencies
root.order.add_edge(material_sourcing, supplier_audit)
root.order.add_edge(material_sourcing, credential_verify)
root.order.add_edge(supplier_audit, credential_verify)
root.order.add_edge(credential_verify, design_concept)
root.order.add_edge(design_concept, prototype_build)
root.order.add_edge(prototype_build, quality_review)
root.order.add_edge(quality_review, artisan_assign)
root.order.add_edge(artisan_assign, batch_scheduling)
root.order.add_edge(batch_scheduling, custom_approvals)
root.order.add_edge(custom_approvals, inventory_adjust)
root.order.add_edge(inventory_adjust, production_sync)
root.order.add_edge(production_sync, shipping_plan)
root.order.add_edge(shipping_plan, compliance_check)
root.order.add_edge(compliance_check, feedback_loop)
root.order.add_edge(feedback_loop, market_target)
root.order.add_edge(market_target, order_fulfill)
root.order.add_edge(order_fulfill, sustainability)
root.order.add_edge(sustainability, customer_engage)

# Return the root of the POWL model
root