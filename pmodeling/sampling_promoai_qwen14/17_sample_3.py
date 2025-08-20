import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
place_order = Transition(label='Place order')
record_order_details = Transition(label='Record order details')
process_payment = Transition(label='Process payment')
notify_about_failed_payment = Transition(label='Notify about failed payment')
check_stock_availability = Transition(label='Check stock availability')
initiate_back_order = Transition(label='Initiate back-order')
inform_customer_about_delay = Transition(label='Inform customer about delay')
receive_back_order = Transition(label='Receive back-order')
pick_items_from_warehouse = Transition(label='Pick items from warehouse')
perform_quality_control_checks = Transition(label='Perform quality control checks')
gift_wrap_items = Transition(label='Gift wrap items')
package_items = Transition(label='Package items')
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

# Define silent transitions
skip = SilentTransition()

# Define loops
order_loop = OperatorPOWL(operator=Operator.LOOP, children=[process_payment, check_stock_availability])

# Define choices
payment_choice = OperatorPOWL(operator=Operator.XOR, children=[notify_about_failed_payment, order_loop])
stock_availability_choice = OperatorPOWL(operator=Operator.XOR, children=[initiate_back_order, skip])
back_order_choice = OperatorPOWL(operator=Operator.XOR, children=[inform_customer_about_delay, receive_back_order])
delivery_issue_choice = OperatorPOWL(operator=Operator.XOR, children=[send_return_shipping_label, skip])
refund_or_replacement_choice = OperatorPOWL(operator=Operator.XOR, children=[process_refund, process_replacement])

# Define partial orders
order_process = StrictPartialOrder(nodes=[place_order, record_order_details, payment_choice, stock_availability_choice, pick_items_from_warehouse, perform_quality_control_checks, package_items, prepare_shipping_documents_and_labels, prepare_documentation_for_international_orders, dispatch_order, send_shipping_confirmation_to_customer, update_inventory_levels, send_follow_up_email, customer_reports_issue, delivery_issue_choice, inspect_returned_items, refund_or_replacement_choice])
order_process.order.add_edge(place_order, record_order_details)
order_process.order.add_edge(record_order_details, payment_choice)
order_process.order.add_edge(payment_choice, stock_availability_choice)
order_process.order.add_edge(stock_availability_choice, pick_items_from_warehouse)
order_process.order.add_edge(pick_items_from_warehouse, perform_quality_control_checks)
order_process.order.add_edge(perform_quality_control_checks, package_items)
order_process.order.add_edge(package_items, prepare_shipping_documents_and_labels)
order_process.order.add_edge(prepare_shipping_documents_and_labels, prepare_documentation_for_international_orders)
order_process.order.add_edge(prepare_documentation_for_international_orders, dispatch_order)
order_process.order.add_edge(dispatch_order, send_shipping_confirmation_to_customer)
order_process.order.add_edge(send_shipping_confirmation_to_customer, update_inventory_levels)
order_process.order.add_edge(update_inventory_levels, send_follow_up_email)
order_process.order.add_edge(send_follow_up_email, customer_reports_issue)
order_process.order.add_edge(customer_reports_issue, delivery_issue_choice)
order_process.order.add_edge(delivery_issue_choice, inspect_returned_items)
order_process.order.add_edge(inspect_returned_items, refund_or_replacement_choice)

# Define final root
root = order_process