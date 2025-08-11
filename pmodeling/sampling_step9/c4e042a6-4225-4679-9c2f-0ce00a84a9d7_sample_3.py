import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define activities
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
# Define exclusive choice (XOR) for feedback loop and market target
xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, market_target])
# Define loop for production sync, feedback loop, and market target
loop = OperatorPOWL(operator=Operator.LOOP, children=[production_sync, xor])
# Define root POWL model
root = StrictPartialOrder(nodes=[loop, batch_scheduling, prototype_build, quality_review, artisan_assign, custom_approvals, inventory_adjust, shipping_plan, compliance_check, order_fulfill, sustainability, customer_engage])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, production_sync)
root.order.add_edge(batch_scheduling, prototype_build)
root.order.add_edge(prototype_build, quality_review)
root.order.add_edge(quality_review, artisan_assign)
root.order.add_edge(artisan_assign, custom_approvals)
root.order.add_edge(custom_approvals, inventory_adjust)
root.order.add_edge(inventory_adjust, production_sync)
root.order.add_edge(production_sync, shipping_plan)
root.order.add_edge(shipping_plan, compliance_check)
root.order.add_edge(compliance_check, order_fulfill)
root.order.add_edge(order_fulfill, sustainability)
root.order.add_edge(sustainability, customer_engage)