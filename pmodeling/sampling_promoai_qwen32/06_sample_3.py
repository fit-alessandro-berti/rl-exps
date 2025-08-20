import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
place_order_online = Transition(label='Customer places order online')
place_order_phone = Transition(label='Customer places order over the phone')
generate_confirmation = Transition(label='Generate and send order confirmation')
generate_label = Transition(label='Generate shipping label')
handover_to_provider = Transition(label='Hand over order to logistics provider')
monitor_shipment = Transition(label='Monitor shipment')
pick_pack_items = Transition(label='Pick and pack items')
process_feedback_returns = Transition(label='Process customer feedback or returns')
send_tracking_info = Transition(label='Send tracking information to customer')
successful_delivery = Transition(label='Successful delivery')

# Define the choice for placing the order
order_choice = OperatorPOWL(operator=Operator.XOR, children=[place_order_online, place_order_phone])

# Define the loop for monitoring the shipment
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_shipment])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[order_choice, generate_confirmation, generate_label, handover_to_provider, monitor_loop, pick_pack_items, process_feedback_returns, send_tracking_info, successful_delivery])

# Define the order of the activities
root.order.add_edge(order_choice, generate_confirmation)
root.order.add_edge(generate_confirmation, pick_pack_items)
root.order.add_edge(pick_pack_items, generate_label)
root.order.add_edge(generate_label, handover_to_provider)
root.order.add_edge(handover_to_provider, monitor_loop)
root.order.add_edge(monitor_loop, send_tracking_info)
root.order.add_edge(send_tracking_info, monitor_loop)
root.order.add_edge(monitor_loop, successful_delivery)
root.order.add_edge(successful_delivery, process_feedback_returns)