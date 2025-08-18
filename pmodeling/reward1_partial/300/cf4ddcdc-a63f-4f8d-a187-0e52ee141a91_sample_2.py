from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the process tree structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[refurbish_prep, recycle_process])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[customer_notify, disposal_arrange])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, cost_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, inventory_update])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, sort_items])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pickup_schedule, transport_dispatch])

root = StrictPartialOrder(nodes=[return_request, authorization_check, loop1, loop2, xor1, xor2, xor3, xor4])
root.order.add_edge(return_request, authorization_check)
root.order.add_edge(authorization_check, loop1)
root.order.add_edge(authorization_check, loop2)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Save the final result in the variable 'root'
print(root)