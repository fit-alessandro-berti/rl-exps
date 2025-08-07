import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
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

# Add dependencies (if any)
# For example, if there's a dependency between material sourcing and supplier audit:
# root.order.add_edge(material_sourcing, supplier_audit)

# You can add more dependencies as needed based on the actual process flow.