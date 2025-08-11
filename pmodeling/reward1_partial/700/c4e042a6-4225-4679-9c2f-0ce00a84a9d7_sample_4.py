import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, supplier_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[credential_verify, design_concept])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, quality_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[artisan_assign, batch_scheduling])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[custom_approvals, inventory_adjust])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[production_sync, shipping_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, feedback_loop])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[market_target, order_fulfill])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[sustainability, customer_engage])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)