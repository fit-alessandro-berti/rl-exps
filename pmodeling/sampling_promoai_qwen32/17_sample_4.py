import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Place_order = Transition(label='Place order')
Record_order_details = Transition(label='Record order details')
Process_payment = Transition(label='Process payment')
Notify_about_failed_payment = Transition(label='Notify about failed payment')
Check_stock_availability = Transition(label='Check stock availability')
Initiate_back_order = Transition(label='Initiate back-order')
Inform_customer_about_delay = Transition(label='Inform customer about delay')
Receive_back_order = Transition(label='Receive back-order')
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    Place_order,
    Record_order_details,
    Process_payment,
    Notify_about_failed_payment,
    Check_stock_availability,
    Initiate_back_order,
    Inform_customer_about_delay,
    Receive_back_order,
    Pick_items_from_warehouse,
    Perform_quality_control_checks,
    Gift_wrap_items,
    Package_items,
    Prepare_shipping_documents_and_labels,
    Prepare_documentation_for_international_orders,
    Dispatch_order,
    Send_shipping_confirmation_to_customer,
    Update_inventory_levels,
    Send_follow_up_email,
    Customer_reports_issue,
    Send_return_shipping_label,
    Receive_returned_items,
    Inspect_returned_items,
    Process_refund,
    Process_replacement
])

# Define the order of the activities
root.order.add_edge(Place_order, Record_order_details)
root.order.add_edge(Record_order_details, Process_payment)
root.order.add_edge(Process_payment, Check_stock_availability)
root.order.add_edge(Check_stock_availability, Initiate_back_order)
root.order.add_edge(Initiate_back_order, Inform_customer_about_delay)
root.order.add_edge(Inform_customer_about_delay, Receive_back_order)
root.order.add_edge(Receive_back_order, Pick_items_from_warehouse)
root.order.add_edge(Pick_items_from_warehouse, Perform_quality_control_checks)
root.order.add_edge(Perform_quality_control_checks, Gift_wrap_items)
root.order.add_edge(Gift_wrap_items, Package_items)
root.order.add_edge(Package_items, Prepare_shipping_documents_and_labels)
root.order.add_edge(Prepare_shipping_documents_and_labels, Prepare_documentation_for_international_orders)
root.order.add_edge(Prepare_documentation_for_international_orders, Dispatch_order)
root.order.add_edge(Dispatch_order, Send_shipping_confirmation_to_customer)
root.order.add_edge(Send_shipping_confirmation_to_customer, Update_inventory_levels)
root.order.add_edge(Update_inventory_levels, Send_follow_up_email)
root.order.add_edge(Send_follow_up_email, Customer_reports_issue)
root.order.add_edge(Customer_reports_issue, Send_return_shipping_label)
root.order.add_edge(Send_return_shipping_label, Receive_returned_items)
root.order.add_edge(Receive_returned_items, Inspect_returned_items)
root.order.add_edge(Inspect_returned_items, Process_refund)
root.order.add_edge(Process_refund, Process_replacement)

# Define the loop for back-order
loop = OperatorPOWL(operator=Operator.LOOP, children=[Initiate_back_order, Inform_customer_about_delay, Receive_back_order])
root.order.add_edge(Check_stock_availability, loop)

# Define the choice for payment failure
xor_payment = OperatorPOWL(operator=Operator.XOR, children=[Notify_about_failed_payment, Process_payment])
root.order.add_edge(Process_payment, xor_payment)

# Define the choice for international orders
xor_international = OperatorPOWL(operator=Operator.XOR, children=[Prepare_documentation_for_international_orders, SilentTransition()])
root.order.add_edge(Prepare_shipping_documents_and_labels, xor_international)

# Define the choice for customer issue
xor_issue = OperatorPOWL(operator=Operator.XOR, children=[Customer_reports_issue, SilentTransition()])
root.order.add_edge(Send_shipping_confirmation_to_customer, xor_issue)

# Define the choice for refund or replacement
xor_refund = OperatorPOWL(operator=Operator.XOR, children=[Process_refund, Process_replacement])
root.order.add_edge(Inspect_returned_items, xor_refund)

# Define the final result in the variable 'root'
root