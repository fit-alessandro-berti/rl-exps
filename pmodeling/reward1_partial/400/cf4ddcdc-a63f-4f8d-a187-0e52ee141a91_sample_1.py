import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop and choice nodes
pickup_and_dispatch = OperatorPOWL(operator=Operator.LOOP, children=[pickup_schedule, transport_dispatch])
receive_and_inspect = OperatorPOWL(operator=Operator.LOOP, children=[receiving_goods, quality_inspect])
refurbish_and_update = OperatorPOWL(operator=Operator.LOOP, children=[refurbish_prep, inventory_update])
recycle_and_update = OperatorPOWL(operator=Operator.LOOP, children=[recycle_process, inventory_update])
notify_and_audit = OperatorPOWL(operator=Operator.LOOP, children=[customer_notify, compliance_audit])
cost_and_report = OperatorPOWL(operator=Operator.LOOP, children=[cost_analysis, report_generate])

# Define the root node with the defined nodes and order
root = StrictPartialOrder(nodes=[
    return_request,
    authorization_check,
    pickup_and_dispatch,
    receive_and_inspect,
    refurbish_and_update,
    recycle_and_update,
    notify_and_audit,
    cost_and_report
])

# Define the order of execution
root.order.add_edge(return_request, authorization_check)
root.order.add_edge(authorization_check, pickup_and_dispatch)
root.order.add_edge(pickup_and_dispatch, receive_and_inspect)
root.order.add_edge(receive_and_inspect, refurbish_and_update)
root.order.add_edge(refurbish_and_update, recycle_and_update)
root.order.add_edge(recycle_and_update, notify_and_audit)
root.order.add_edge(notify_and_audit, cost_and_report)

# Print the root node
print(root)