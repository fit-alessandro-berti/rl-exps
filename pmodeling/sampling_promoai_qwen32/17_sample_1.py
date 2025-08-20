import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Place_order = Transition(label='Place order')
Record_order_details = Transition(label='Record order details')
Process_payment = Transition(label='Process payment')
Notify_about_failed_payment = Transition(label='Notify about failed payment')
Check_stock_availability = Transition(label='Check stock availability')
Initiate_back_order = Transition(label='Initiate back-order')
Inform_customer_about_delay = Transition(label='Inform customer about delay')
Pick_items_from_warehouse = Transition(label='Pick items from warehouse')
Perform_quality_control_checks = Transition(label='Perform quality control checks')
Gift_wrap_items = Transition(label='Gift wrap items')
Package_items = Transition(label='Package items')
Prepare_shipping_documents_and_labels = Transition(label='Prepare shipping documents and labels')
Prepare_documentation_for_international_orders = Transition(label='Prepare documentation for international orders')
Dispatch_order = Transition(label='Dispatch order')
Send_shipping_confirmation_to_customer = Transition(label='Send shipping confirmation to customer')
Update_inventory_levels = Transition(label='Update inventory levels')
Send_follow_up_email = Transition(label='Send follow-up email')
Customer_reports_issue = Transition(label='Customer reports issue')
Send_return_shipping_label = Transition(label='Send return shipping label')
Receive_returned_items = Transition(label='Receive returned items')
Inspect_returned_items = Transition(label='Inspect returned items')
Process_refund = Transition(label='Process refund')
Process_replacement = Transition(label='Process replacement')
Receive_back_order = Transition(label='Receive back-order')
Confirm_delivery = Transition(label='Confirm delivery')

# Define the process
payment_loop = OperatorPOWL(operator=Operator.LOOP, children=[Process_payment, Notify_about_failed_payment])
back_order_loop = OperatorPOWL(operator=Operator.LOOP, children=[Initiate_back_order, Inform_customer_about_delay, Receive_back_order])
pick_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pick_items_from_warehouse, Perform_quality_control_checks, Gift_wrap_items, Package_items])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[Prepare_shipping_documents_and_labels, Prepare_documentation_for_international_orders, Dispatch_order, Send_shipping_confirmation_to_customer, Update_inventory_levels, Send_follow_up_email])

# Define the root node
root = StrictPartialOrder(nodes=[Place_order, Record_order_details, payment_loop, back_order_loop, pick_loop, shipping_loop, Customer_reports_issue, Send_return_shipping_label, Receive_returned_items, Inspect_returned_items, Process_refund, Process_replacement, Confirm_delivery])

# Define the order
root.order.add_edge(Place_order, Record_order_details)
root.order.add_edge(Record_order_details, payment_loop)
root.order.add_edge(payment_loop, back_order_loop)
root.order.add_edge(back_order_loop, pick_loop)
root.order.add_edge(pick_loop, shipping_loop)
root.order.add_edge(shipping_loop, Customer_reports_issue)
root.order.add_edge(Customer_reports_issue, Send_return_shipping_label)
root.order.add_edge(Send_return_shipping_label, Receive_returned_items)
root.order.add_edge(Receive_returned_items, Inspect_returned_items)
root.order.add_edge(Inspect_returned_items, Process_refund)
root.order.add_edge(Process_refund, Process_replacement)
root.order.add_edge(Process_replacement, Confirm_delivery)

# Define the final result
root