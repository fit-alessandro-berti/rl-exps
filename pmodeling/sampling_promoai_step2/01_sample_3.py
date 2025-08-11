import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
address_customer_concerns = Transition(label='Address customer concerns or questions')
collect_customer_info = Transition(label='Collect customer information')
guide_customer = Transition(label='Guide customer in selecting product/service')
place_order = Transition(label='Place order')
provide_quote = Transition(label='Provide quote')
receive_customer_inquiry = Transition(label='Receive customer inquiry')
record_order_in_system = Transition(label='Record order in system')
send_order_confirmation = Transition(label='Send order confirmation to customer')

# Define the POWL model
root = StrictPartialOrder(nodes=[address_customer_concerns, collect_customer_info, guide_customer, provide_quote, receive_customer_inquiry, place_order, record_order_in_system, send_order_confirmation])
root.order.add_edge(address_customer_concerns, collect_customer_info)
root.order.add_edge(collect_customer_info, guide_customer)
root.order.add_edge(guide_customer, provide_quote)
root.order.add_edge(provide_quote, receive_customer_inquiry)
root.order.add_edge(receive_customer_inquiry, place_order)
root.order.add_edge(place_order, record_order_in_system)
root.order.add_edge(record_order_in_system, send_order_confirmation)

# Print the final result
print(root)