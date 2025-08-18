import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pickup_schedule, transport_dispatch])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[receiving_goods, quality_inspect])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sort_items, refurbish_prep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[recycle_process, disposal_arrange])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, cost_analysis])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[report_generate])

# Define the partial order
root = StrictPartialOrder(nodes=[return_request, authorization_check, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(return_request, authorization_check)
root.order.add_edge(authorization_check, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)