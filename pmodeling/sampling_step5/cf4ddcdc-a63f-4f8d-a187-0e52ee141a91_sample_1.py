import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities (transitions) in the POWL model
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    return_request,
    authorization_check,
    pickup_schedule,
    transport_dispatch,
    receiving_goods,
    quality_inspect,
    sort_items,
    refurbish_prep,
    recycle_process,
    inventory_update,
    customer_notify,
    disposal_arrange,
    compliance_audit,
    cost_analysis,
    report_generate
])

# Define the dependencies between activities
root.order.add_edge(return_request, authorization_check)
root.order.add_edge(authorization_check, pickup_schedule)
root.order.add_edge(pickup_schedule, transport_dispatch)
root.order.add_edge(transport_dispatch, receiving_goods)
root.order.add_edge(receiving_goods, quality_inspect)
root.order.add_edge(quality_inspect, sort_items)
root.order.add_edge(sort_items, refurbish_prep)
root.order.add_edge(refurbish_prep, recycle_process)
root.order.add_edge(recycle_process, inventory_update)
root.order.add_edge(inventory_update, customer_notify)
root.order.add_edge(customer_notify, disposal_arrange)
root.order.add_edge(disposal_arrange, compliance_audit)
root.order.add_edge(compliance_audit, cost_analysis)
root.order.add_edge(cost_analysis, report_generate)