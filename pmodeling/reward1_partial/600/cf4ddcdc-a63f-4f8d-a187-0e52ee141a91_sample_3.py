import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
return_request = Transition(label='Return Request')
authorization_check = Transition(label='Authorization Check')
pickup_schedule = Transition(label='Pickup Schedule')
transport_dispatch = Transition(label='Transport Dispatch')
receiving_goods = Transition(label='Receiving Goods')
quality_inspect = Transition(label='Quality Inspect')
sort_items = Transition(label='Sort Items')
refurbish_prep = Transition(label='Refurbish Prep')
recycle_process = Transition(label='Recycle Process')
inventory_update = Transition(label='Inventory Update')
customer_notify = Transition(label='Customer Notify')
disposal_arrange = Transition(label='Disposal Arrange')
compliance_audit = Transition(label='Compliance Audit')
cost_analysis = Transition(label='Cost Analysis')
report_generate = Transition(label='Report Generate')

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[refurbish_prep, recycle_process])
loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, customer_notify, disposal_arrange])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, cost_analysis])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, ])

# Define the POWL root
root = StrictPartialOrder(nodes=[return_request, authorization_check, pickup_schedule, transport_dispatch, receiving_goods, quality_inspect, sort_items, xor, loop, xor2, xor3])
root.order.add_edge(return_request, authorization_check)
root.order.add_edge(authorization_check, pickup_schedule)
root.order.add_edge(pickup_schedule, transport_dispatch)
root.order.add_edge(transport_dispatch, receiving_goods)
root.order.add_edge(receiving_goods, quality_inspect)
root.order.add_edge(quality_inspect, sort_items)
root.order.add_edge(sort_items, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, report_generate)