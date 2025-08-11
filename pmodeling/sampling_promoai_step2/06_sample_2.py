from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
customer_places_order_online = Transition(label='Customer places order online')
customer_places_order_over_the_phone = Transition(label='Customer places order over the phone')
generate_and_send_order_confirmation = Transition(label='Generate and send order confirmation')
generate_shipping_label = Transition(label='Generate shipping label')
hand_over_order_to_logistics_provider = Transition(label='Hand over order to logistics provider')
monitor_shipment = Transition(label='Monitor shipment')
pick_and_pack_items = Transition(label='Pick and pack items')
process_customer_feedback_or_returns = Transition(label='Process customer feedback or returns')
send_tracking_information_to_customer = Transition(label='Send tracking information to customer')
successful_delivery = Transition(label='Successful delivery')

# Define the partial order
root = StrictPartialOrder(nodes=[
    customer_places_order_online,
    customer_places_order_over_the_phone,
    generate_and_send_order_confirmation,
    generate_shipping_label,
    hand_over_order_to_logistics_provider,
    monitor_shipment,
    pick_and_pack_items,
    process_customer_feedback_or_returns,
    send_tracking_information_to_customer,
    successful_delivery
])

# Define the dependencies between the activities
root.order.add_edge(customer_places_order_online, generate_and_send_order_confirmation)
root.order.add_edge(customer_places_order_online, generate_shipping_label)
root.order.add_edge(customer_places_order_online, hand_over_order_to_logistics_provider)
root.order.add_edge(generate_and_send_order_confirmation, monitor_shipment)
root.order.add_edge(generate_shipping_label, monitor_shipment)
root.order.add_edge(hand_over_order_to_logistics_provider, monitor_shipment)
root.order.add_edge(monitor_shipment, process_customer_feedback_or_returns)
root.order.add_edge(monitor_shipment, send_tracking_information_to_customer)
root.order.add_edge(process_customer_feedback_or_returns, successful_delivery)
root.order.add_edge(send_tracking_information_to_customer, successful_delivery)