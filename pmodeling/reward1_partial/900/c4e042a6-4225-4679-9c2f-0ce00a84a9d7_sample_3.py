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

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, supplier_audit])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[credential_verify, design_concept, prototype_build])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[quality_review, artisan_assign, batch_scheduling, custom_approvals])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_adjust, production_sync, shipping_plan, compliance_check])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, market_target, order_fulfill, sustainability])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[customer_engage])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    loop1, loop2, loop3, loop4, loop5, loop6
])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)