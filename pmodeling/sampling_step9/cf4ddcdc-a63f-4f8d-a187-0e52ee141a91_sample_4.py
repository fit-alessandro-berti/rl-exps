import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the POWL model
loop_pickup_schedule = OperatorPOWL(operator=Operator.LOOP, children=[pickup_schedule, transport_dispatch])
loop_quality_inspect = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, sort_items, refurbish_prep])
loop_recycle_process = OperatorPOWL(operator=Operator.LOOP, children=[recycle_process, inventory_update, customer_notify])
loop_disposal_arrange = OperatorPOWL(operator=Operator.LOOP, children=[disposal_arrange, compliance_audit, cost_analysis, report_generate])

xor = OperatorPOWL(operator=Operator.XOR, children=[return_request, authorization_check])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor, loop_pickup_schedule, loop_quality_inspect, loop_recycle_process, loop_disposal_arrange])
root.order.add_edge(xor, loop_pickup_schedule)
root.order.add_edge(xor, loop_quality_inspect)
root.order.add_edge(xor, loop_recycle_process)
root.order.add_edge(xor, loop_disposal_arrange)