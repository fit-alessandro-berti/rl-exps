from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

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

# Define the workflow
# Material Sourcing -> Supplier Audit -> Credential Verify -> Design Concept
root.add_transition(material_sourcing)
root.add_transition(supplier_audit)
root.add_transition(credential_verify)
root.add_transition(design_concept)
root.add_edge(material_sourcing, supplier_audit)
root.add_edge(supplier_audit, credential_verify)
root.add_edge(credential_verify, design_concept)

# Design Concept -> Prototype Build -> Quality Review -> Artisan Assign
root.add_transition(prototype_build)
root.add_transition(quality_review)
root.add_transition(artisan_assign)
root.add_edge(design_concept, prototype_build)
root.add_edge(prototype_build, quality_review)
root.add_edge(quality_review, artisan_assign)

# Artisan Assign -> Batch Scheduling -> Custom Approvals
root.add_transition(batch_scheduling)
root.add_transition(custom_approvals)
root.add_edge(artisan_assign, batch_scheduling)
root.add_edge(batch_scheduling, custom_approvals)

# Custom Approvals -> Inventory Adjust -> Production Sync -> Shipping Plan
root.add_transition(inventory_adjust)
root.add_transition(production_sync)
root.add_transition(shipping_plan)
root.add_edge(custom_approvals, inventory_adjust)
root.add_edge(inventory_adjust, production_sync)
root.add_edge(production_sync, shipping_plan)

# Shipping Plan -> Compliance Check -> Feedback Loop
root.add_transition(compliance_check)
root.add_transition(feedback_loop)
root.add_edge(shipping_plan, compliance_check)
root.add_edge(compliance_check, feedback_loop)

# Feedback Loop -> Market Target -> Order Fulfill -> Sustainability
root.add_transition(market_target)
root.add_transition(order_fulfill)
root.add_transition(sustainability)
root.add_edge(feedback_loop, market_target)
root.add_edge(market_target, order_fulfill)
root.add_edge(order_fulfill, sustainability)

# Order Fulfill -> Customer Engage
root.add_transition(customer_engage)
root.add_edge(order_fulfill, customer_engage)

# Print the final POWL model
print(root)