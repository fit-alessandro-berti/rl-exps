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

# Define the transitions and loops
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pickup_schedule, transport_dispatch])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, sort_items])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[refurbish_prep, recycle_process])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, customer_notify])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[disposal_arrange, compliance_audit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[cost_analysis, report_generate])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[return_request, authorization_check])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[xor3, xor4])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[xor5, xor6])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[xor7, xor8])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[xor9, xor10])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[xor11, xor12])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor13])
root.order.add_edge(xor13, xor8)
root.order.add_edge(xor8, xor1)
root.order.add_edge(xor8, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor13)