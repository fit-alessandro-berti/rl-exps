import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the process steps
return_request_to_authorization_check = OperatorPOWL(operator=Operator.XOR, children=[return_request, skip])
authorization_check_to_pickup_schedule = OperatorPOWL(operator=Operator.XOR, children=[authorization_check, skip])
pickup_schedule_to_transport_dispatch = OperatorPOWL(operator=Operator.XOR, children=[pickup_schedule, skip])
transport_dispatch_to_receiving_goods = OperatorPOWL(operator=Operator.XOR, children=[transport_dispatch, skip])
receiving_goods_to_quality_inspect = OperatorPOWL(operator=Operator.XOR, children=[receiving_goods, skip])
quality_inspect_to_sort_items = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, skip])
sort_items_to_refurbish_prep = OperatorPOWL(operator=Operator.XOR, children=[sort_items, skip])
refurbish_prep_to_recycle_process = OperatorPOWL(operator=Operator.XOR, children=[refurbish_prep, skip])
recycle_process_to_inventory_update = OperatorPOWL(operator=Operator.XOR, children=[recycle_process, skip])
inventory_update_to_customer_notify = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip])
customer_notify_to_disposal_arrange = OperatorPOWL(operator=Operator.XOR, children=[customer_notify, skip])
disposal_arrange_to_compliance_audit = OperatorPOWL(operator=Operator.XOR, children=[disposal_arrange, skip])
compliance_audit_to_cost_analysis = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])
cost_analysis_to_report_generate = OperatorPOWL(operator=Operator.XOR, children=[cost_analysis, skip])

# Define the loop for inventory update
inventory_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update_to_customer_notify])

# Define the root process
root = StrictPartialOrder(nodes=[return_request_to_authorization_check, authorization_check_to_pickup_schedule, pickup_schedule_to_transport_dispatch, transport_dispatch_to_receiving_goods, receiving_goods_to_quality_inspect, quality_inspect_to_sort_items, sort_items_to_refurbish_prep, refurbish_prep_to_recycle_process, recycle_process_to_inventory_update, inventory_update_loop, customer_notify_to_disposal_arrange, disposal_arrange_to_compliance_audit, compliance_audit_to_cost_analysis, cost_analysis_to_report_generate])
root.order.add_edge(return_request_to_authorization_check, authorization_check_to_pickup_schedule)
root.order.add_edge(authorization_check_to_pickup_schedule, pickup_schedule_to_transport_dispatch)
root.order.add_edge(pickup_schedule_to_transport_dispatch, transport_dispatch_to_receiving_goods)
root.order.add_edge(transport_dispatch_to_receiving_goods, receiving_goods_to_quality_inspect)
root.order.add_edge(receiving_goods_to_quality_inspect, quality_inspect_to_sort_items)
root.order.add_edge(quality_inspect_to_sort_items, sort_items_to_refurbish_prep)
root.order.add_edge(sort_items_to_refurbish_prep, refurbish_prep_to_recycle_process)
root.order.add_edge(refurbish_prep_to_recycle_process, recycle_process_to_inventory_update)
root.order.add_edge(recycle_process_to_inventory_update, inventory_update_to_customer_notify)
root.order.add_edge(inventory_update_to_customer_notify, customer_notify_to_disposal_arrange)
root.order.add_edge(customer_notify_to_disposal_arrange, disposal_arrange_to_compliance_audit)
root.order.add_edge(disposal_arrange_to_compliance_audit, compliance_audit_to_cost_analysis)
root.order.add_edge(compliance_audit_to_cost_analysis, cost_analysis_to_report_generate)
root.order.add_edge(cost_analysis_to_report_generate, return_request_to_authorization_check)

print(root)