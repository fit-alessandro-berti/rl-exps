import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
receive_customer_inquiry = Transition(label='Receive customer inquiry')
collect_customer_info = Transition(label='Collect customer information')
address_customer_concerns_or_questions = Transition(label='Address customer concerns or questions')
guide_customer_in_selecting_product_service = Transition(label='Guide customer in selecting product/service')
place_order = Transition(label='Place order')
provide_quote = Transition(label='Provide quote')
record_order_in_system = Transition(label='Record order in system')
send_order_confirmation_to_customer = Transition(label='Send order confirmation to customer')

# Define the partial order
root = StrictPartialOrder(nodes=[
    receive_customer_inquiry,
    collect_customer_info,
    address_customer_concerns_or_questions,
    guide_customer_in_selecting_product_service,
    place_order,
    provide_quote,
    record_order_in_system,
    send_order_confirmation_to_customer
])

# Define the dependencies
root.order.add_edge(receive_customer_inquiry, collect_customer_info)
root.order.add_edge(receive_customer_inquiry, address_customer_concerns_or_questions)
root.order.add_edge(collect_customer_info, guide_customer_in_selecting_product_service)
root.order.add_edge(guide_customer_in_selecting_product_service, place_order)
root.order.add_edge(place_order, provide_quote)
root.order.add_edge(provide_quote, record_order_in_system)
root.order.add_edge(record_order_in_system, send_order_confirmation_to_customer)

print(root)