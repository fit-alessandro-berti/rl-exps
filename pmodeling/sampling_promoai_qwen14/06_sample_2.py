import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
place_order_online = Transition(label='Customer places order online')
place_order_phone = Transition(label='Customer places order over the phone')
generate_confirmation = Transition(label='Generate and send order confirmation')
generate_shipping_label = Transition(label='Generate shipping label')
hand_over_to_provider = Transition(label='Hand over order to logistics provider')
monitor_shipment = Transition(label='Monitor shipment')
pick_pack_items = Transition(label='Pick and pack items')
process_feedback_returns = Transition(label='Process customer feedback or returns')
send_tracking_info = Transition(label='Send tracking information to customer')
successful_delivery = Transition(label='Successful delivery')

# Define the choice for placing order (online or phone)
place_order_choice = OperatorPOWL(operator=Operator.XOR, children=[place_order_online, place_order_phone])

# Define the loop for monitoring shipment until successful delivery
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_shipment, successful_delivery])

# Define the root process
root = StrictPartialOrder(nodes=[
    place_order_choice,
    generate_confirmation,
    pick_pack_items,
    generate_shipping_label,
    hand_over_to_provider,
    monitor_loop,
    send_tracking_info,
    process_feedback_returns
])

# Define the partial order dependencies
root.order.add_edge(place_order_choice, generate_confirmation)
root.order.add_edge(generate_confirmation, pick_pack_items)
root.order.add_edge(pick_pack_items, generate_shipping_label)
root.order.add_edge(generate_shipping_label, hand_over_to_provider)
root.order.add_edge(hand_over_to_provider, monitor_loop)
root.order.add_edge(monitor_loop, send_tracking_info)
root.order.add_edge(send_tracking_info, process_feedback_returns)

# The loop dependency is already defined within the monitor_loop node