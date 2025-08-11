from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
check_stock_availability = Transition(label='Check stock availability')
confirm_delivery = Transition(label='Confirm delivery')
customer_reports_issue = Transition(label='Customer reports issue')
dispatch_order = Transition(label='Dispatch order')
gift_wrap_items = Transition(label='Gift wrap items')
inform_customer_about_delay = Transition(label='Inform customer about delay')
initiate_back_order = Transition(label='Initiate back-order')
inspect_returned_items = Transition(label='Inspect returned items')
notify_about_failed_payment = Transition(label='Notify about failed payment')
package_items = Transition(label='Package items')
perform_quality_control_checks = Transition(label='Perform quality control checks')
pick_items_from_warehouse = Transition(label='Pick items from warehouse')
place_order = Transition(label='Place order')
prepare_documentation_for_international_orders = Transition(label='Prepare documentation for international orders')
prepare_shipping_documents_and_labels = Transition(label='Prepare shipping documents and labels')
process_payment = Transition(label='Process payment')
process_refund = Transition(label='Process refund')
process_replacement = Transition(label='Process replacement')
receive_back_order = Transition(label='Receive back-order')
receive_returned_items = Transition(label='Receive returned items')
record_order_details = Transition(label='Record order details')
send_follow_up_email = Transition(label='Send follow-up email')
send_return_shipping_label = Transition(label='Send return shipping label')
send_shipping_confirmation_to_customer = Transition(label='Send shipping confirmation to customer')
update_inventory_levels = Transition(label='Update inventory levels')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    check_stock_availability,
    confirm_delivery,
    customer_reports_issue,
    dispatch_order,
    gift_wrap_items,
    inform_customer_about_delay,
    initiate_back_order,
    inspect_returned_items,
    notify_about_failed_payment,
    package_items,
    perform_quality_control_checks,
    pick_items_from_warehouse,
    place_order,
    prepare_documentation_for_international_orders,
    prepare_shipping_documents_and_labels,
    process_payment,
    process_refund,
    process_replacement,
    receive_back_order,
    receive_returned_items,
    record_order_details,
    send_follow_up_email,
    send_return_shipping_label,
    send_shipping_confirmation_to_customer,
    update_inventory_levels
])

# Define the partial order dependencies
root.order.add_edge(record_order_details, place_order)
root.order.add_edge(place_order, check_stock_availability)
root.order.add_edge(check_stock_availability, initiate_back_order)
root.order.add_edge(initiate_back_order, receive_back_order)
root.order.add_edge(receive_back_order, dispatch_order)
root.order.add_edge(dispatch_order, prepare_shipping_documents_and_labels)
root.order.add_edge(prepare_shipping_documents_and_labels, send_shipping_confirmation_to_customer)
root.order.add_edge(send_shipping_confirmation_to_customer, update_inventory_levels)
root.order.add_edge(send_shipping_confirmation_to_customer, send_follow_up_email)
root.order.add_edge(send_follow_up_email, send_return_shipping_label)
root.order.add_edge(send_return_shipping_label, receive_returned_items)
root.order.add_edge(receive_returned_items, inspect_returned_items)
root.order.add_edge(inspect_returned_items, process_refund)
root.order.add_edge(inspect_returned_items, process_replacement)
root.order.add_edge(process_payment, dispatch_order)
root.order.add_edge(process_payment, send_follow_up_email)
root.order.add_edge(process_payment, send_return_shipping_label)
root.order.add_edge(process_payment, send_shipping_confirmation_to_customer)
root.order.add_edge(process_payment, update_inventory_levels)
root.order.add_edge(process_refund, send_follow_up_email)
root.order.add_edge(process_refund, send_return_shipping_label)
root.order.add_edge(process_refund, send_shipping_confirmation_to_customer)
root.order.add_edge(process_refund, update_inventory_levels)
root.order.add_edge(process_replacement, send_follow_up_email)
root.order.add_edge(process_replacement, send_return_shipping_label)
root.order.add_edge(process_replacement, send_shipping_confirmation_to_customer)
root.order.add_edge(process_replacement, update_inventory_levels)
root.order.add_edge(send_follow_up_email, send_return_shipping_label)
root.order.add_edge(send_follow_up_email, send_shipping_confirmation_to_customer)
root.order.add_edge(send_follow_up_email, update_inventory_levels)
root.order.add_edge(send_return_shipping_label, send_shipping_confirmation_to_customer)
root.order.add_edge(send_return_shipping_label, update_inventory_levels)
root.order.add_edge(send_shipping_confirmation_to_customer, update_inventory_levels)