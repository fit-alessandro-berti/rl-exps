import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define choice for order placement
order_placement_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_places_order_online, customer_places_order_over_the_phone])

# Define the main process flow
main_process_flow = StrictPartialOrder(nodes=[order_placement_choice, generate_and_send_order_confirmation, pick_and_pack_items, generate_shipping_label, hand_over_order_to_logistics_provider, send_tracking_information_to_customer, monitor_shipment, successful_delivery])
main_process_flow.order.add_edge(order_placement_choice, generate_and_send_order_confirmation)
main_process_flow.order.add_edge(generate_and_send_order_confirmation, pick_and_pack_items)
main_process_flow.order.add_edge(pick_and_pack_items, generate_shipping_label)
main_process_flow.order.add_edge(generate_shipping_label, hand_over_order_to_logistics_provider)
main_process_flow.order.add_edge(hand_over_order_to_logistics_provider, send_tracking_information_to_customer)
main_process_flow.order.add_edge(send_tracking_information_to_customer, monitor_shipment)
main_process_flow.order.add_edge(monitor_shipment, successful_delivery)

# Define the final POWL model
root = StrictPartialOrder(nodes=[main_process_flow, process_customer_feedback_or_returns])
root.order.add_edge(main_process_flow, process_customer_feedback_or_returns)

root