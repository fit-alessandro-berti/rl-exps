import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
place_order = Transition(label='Place order')
process_payment = Transition(label='Process payment')
notify_failed_payment = Transition(label='Notify about failed payment')
check_stock_availability = Transition(label='Check stock availability')
initiate_back_order = Transition(label='Initiate back-order')
inform_customer_about_delay = Transition(label='Inform customer about delay')
receive_back_order = Transition(label='Receive back-order')
pick_items_from_warehouse = Transition(label='Pick items from warehouse')
perform_quality_control_checks = Transition(label='Perform quality control checks')
package_items = Transition(label='Package items')
gift_wrap_items = Transition(label='Gift wrap items')
prepare_shipping_documents_and_labels = Transition(label='Prepare shipping documents and labels')
prepare_documentation_for_international_orders = Transition(label='Prepare documentation for international orders')
dispatch_order = Transition(label='Dispatch order')
send_shipping_confirmation_to_customer = Transition(label='Send shipping confirmation to customer')
update_inventory_levels = Transition(label='Update inventory levels')
send_follow_up_email = Transition(label='Send follow-up email')
customer_reports_issue = Transition(label='Customer reports issue')
send_return_shipping_label = Transition(label='Send return shipping label')
receive_returned_items = Transition(label='Receive returned items')
inspect_returned_items = Transition(label='Inspect returned items')
process_refund = Transition(label='Process refund')
process_replacement = Transition(label='Process replacement')
confirm_delivery = Transition(label='Confirm delivery')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop_check_stock = OperatorPOWL(operator=Operator.LOOP, children=[check_stock_availability, initiate_back_order])
loop_receive_back_order = OperatorPOWL(operator=Operator.LOOP, children=[inform_customer_about_delay, receive_back_order])
loop_receive_returned_items = OperatorPOWL(operator=Operator.LOOP, children=[send_return_shipping_label, receive_returned_items])
loop_inspect_returned_items = OperatorPOWL(operator=Operator.LOOP, children=[inspect_returned_items, process_refund])
loop_process_replacement = OperatorPOWL(operator=Operator.LOOP, children=[process_replacement, skip])
choice_payment = OperatorPOWL(operator=Operator.XOR, children=[notify_failed_payment, skip])
choice_stock_availability = OperatorPOWL(operator=Operator.XOR, children=[loop_check_stock, skip])
choice_dispatch_order = OperatorPOWL(operator=Operator.XOR, children=[dispatch_order, loop_receive_back_order])
choice_customer_issue = OperatorPOWL(operator=Operator.XOR, children=[customer_reports_issue, confirm_delivery])
choice_return_items = OperatorPOWL(operator=Operator.XOR, children=[loop_receive_returned_items, skip])
choice_inspect_returned_items = OperatorPOWL(operator=Operator.XOR, children=[loop_inspect_returned_items, skip])
choice_process_refund = OperatorPOWL(operator=Operator.XOR, children=[process_refund, loop_process_replacement])
choice_process_replacement = OperatorPOWL(operator=Operator.XOR, children=[process_replacement, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    place_order,
    process_payment,
    check_stock_availability,
    initiate_back_order,
    inform_customer_about_delay,
    receive_back_order,
    pick_items_from_warehouse,
    perform_quality_control_checks,
    package_items,
    gift_wrap_items,
    prepare_shipping_documents_and_labels,
    prepare_documentation_for_international_orders,
    dispatch_order,
    send_shipping_confirmation_to_customer,
    update_inventory_levels,
    send_follow_up_email,
    customer_reports_issue,
    send_return_shipping_label,
    receive_returned_items,
    inspect_returned_items,
    process_refund,
    process_replacement,
    confirm_delivery,
    loop_check_stock,
    loop_receive_back_order,
    loop_receive_returned_items,
    loop_inspect_returned_items,
    loop_process_replacement,
    choice_payment,
    choice_stock_availability,
    choice_dispatch_order,
    choice_customer_issue,
    choice_return_items,
    choice_inspect_returned_items,
    choice_process_refund,
    choice_process_replacement,
    skip
])

# Define the order of the nodes
root.order.add_edge(place_order, process_payment)
root.order.add_edge(process_payment, choice_payment)
root.order.add_edge(choice_payment, skip)
root.order.add_edge(choice_payment, check_stock_availability)
root.order.add_edge(check_stock_availability, choice_stock_availability)
root.order.add_edge(choice_stock_availability, skip)
root.order.add_edge(choice_stock_availability, loop_check_stock)
root.order.add_edge(loop_check_stock, pick_items_from_warehouse)
root.order.add_edge(pick_items_from_warehouse, perform_quality_control_checks)
root.order.add_edge(perform_quality_control_checks, package_items)
root.order.add_edge(package_items, gift_wrap_items)
root.order.add_edge(gift_wrap_items, prepare_shipping_documents_and_labels)
root.order.add_edge(prepare_shipping_documents_and_labels, prepare_documentation_for_international_orders)
root.order.add_edge(prepare_documentation_for_international_orders, dispatch_order)
root.order.add_edge(dispatch_order, choice_dispatch_order)
root.order.add_edge(choice_dispatch_order, skip)
root.order.add_edge(choice_dispatch_order, loop_receive_back_order)
root.order.add_edge(loop_receive_back_order, send_shipping_confirmation_to_customer)
root.order.add_edge(send_shipping_confirmation_to_customer, update_inventory_levels)
root.order.add_edge(update_inventory_levels, send_follow_up_email)
root.order.add_edge(send_follow_up_email, customer_reports_issue)
root.order.add_edge(customer_reports_issue, choice_customer_issue)
root.order.add_edge(choice_customer_issue, confirm_delivery)
root.order.add_edge(choice_customer_issue, send_return_shipping_label)
root.order.add_edge(send_return_shipping_label, loop_receive_returned_items)
root.order.add_edge(loop_receive_returned_items, inspect_returned_items)
root.order.add_edge(inspect_returned_items, choice_inspect_returned_items)
root.order.add_edge(choice_inspect_returned_items, loop_inspect_returned_items)
root.order.add_edge(choice_inspect_returned_items, skip)
root.order.add_edge(loop_inspect_returned_items, process_refund)
root.order.add_edge(process_refund, choice_process_refund)
root.order.add_edge(choice_process_refund, loop_process_replacement)
root.order.add_edge(choice_process_refund, skip)
root.order.add_edge(loop_process_replacement, process_replacement)
root.order.add_edge(process_replacement, choice_process_replacement)
root.order.add_edge(choice_process_replacement, skip)
root.order.add_edge(choice_process_replacement, loop_process_replacement)

print(root)