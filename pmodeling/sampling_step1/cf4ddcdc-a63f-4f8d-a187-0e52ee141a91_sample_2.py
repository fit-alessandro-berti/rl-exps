from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (return_request, authorization_check),
        (authorization_check, pickup_schedule),
        (pickup_schedule, transport_dispatch),
        (transport_dispatch, receiving_goods),
        (receiving_goods, quality_inspect),
        (quality_inspect, sort_items),
        (sort_items, refurbish_prep),
        (refurbish_prep, recycle_process),
        (recycle_process, inventory_update),
        (inventory_update, customer_notify),
        (customer_notify, disposal_arrange),
        (disposal_arrange, compliance_audit),
        (compliance_audit, cost_analysis),
        (cost_analysis, report_generate)
    ]
)

# Add any additional dependencies or loops as needed