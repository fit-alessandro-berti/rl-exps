import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
check_stock = Transition(label='Check stock availability')
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[inform_customer_about_delay, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[process_refund, process_replacement])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[process_refund, process_replacement])

# Define the POWL loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[process_payment, process_refund, process_replacement])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[place_order, check_stock, confirm_delivery, gift_wrap_items, package_items, perform_quality_control_checks, pick_items_from_warehouse, prepare_documentation_for_international_orders, prepare_shipping_documents_and_labels, dispatch_order, send_shipping_confirmation_to_customer, update_inventory_levels, record_order_details, send_follow_up_email, customer_reports_issue, initiate_back_order, receive_back_order, inform_customer_about_delay, notify_about_failed_payment, receive_returned_items, inspect_returned_items, send_return_shipping_label, xor, xor2, xor3, loop])
root.order.add_edge(place_order, check_stock)
root.order.add_edge(check_stock, confirm_delivery)
root.order.add_edge(confirm_delivery, gift_wrap_items)
root.order.add_edge(gift_wrap_items, package_items)
root.order.add_edge(package_items, perform_quality_control_checks)
root.order.add_edge(perform_quality_control_checks, pick_items_from_warehouse)
root.order.add_edge(pick_items_from_warehouse, prepare_documentation_for_international_orders)
root.order.add_edge(prepare_documentation_for_international_orders, prepare_shipping_documents_and_labels)
root.order.add_edge(prepare_shipping_documents_and_labels, dispatch_order)
root.order.add_edge(dispatch_order, send_shipping_confirmation_to_customer)
root.order.add_edge(send_shipping_confirmation_to_customer, update_inventory_levels)
root.order.add_edge(update_inventory_levels, record_order_details)
root.order.add_edge(record_order_details, send_follow_up_email)
root.order.add_edge(send_follow_up_email, customer_reports_issue)
root.order.add_edge(customer_reports_issue, initiate_back_order)
root.order.add_edge(initiate_back_order, receive_back_order)
root.order.add_edge(receive_back_order, inform_customer_about_delay)
root.order.add_edge(inform_customer_about_delay, notify_about_failed_payment)
root.order.add_edge(notify_about_failed_payment, receive_returned_items)
root.order.add_edge(receive_returned_items, inspect_returned_items)
root.order.add_edge(inspect_returned_items, send_return_shipping_label)
root.order.add_edge(send_return_shipping_label, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop)