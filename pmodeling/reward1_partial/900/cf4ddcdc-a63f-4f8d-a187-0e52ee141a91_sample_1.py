import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[authorization_check, pickup_schedule])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transport_dispatch, receiving_goods])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, sort_items])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[refurbish_prep, recycle_process])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, customer_notify])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[disposal_arrange, compliance_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[cost_analysis, report_generate])

# Define the partial order
root = StrictPartialOrder(nodes=[return_request, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(return_request, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Print the root model
print(root)