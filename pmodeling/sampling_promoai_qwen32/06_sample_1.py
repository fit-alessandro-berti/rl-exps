import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
online_order = Transition(label='Customer places order online')
phone_order = Transition(label='Customer places order over the phone')
confirmation = Transition(label='Generate and send order confirmation')
pick_pack = Transition(label='Pick and pack items')
shipping_label = Transition(label='Generate shipping label')
logistics_handover = Transition(label='Hand over order to logistics provider')
monitor_shipment = Transition(label='Monitor shipment')
feedback_returns = Transition(label='Process customer feedback or returns')
tracking_info = Transition(label='Send tracking information to customer')
successful_delivery = Transition(label='Successful delivery')

# Define the process structure
# Customer places order (either online or over the phone) -> Generate and send order confirmation
# -> Pick and pack items -> Generate shipping label -> Hand over order to logistics provider
# -> Send tracking information to customer -> Monitor shipment -> Successful delivery
# Concurrently, Process customer feedback or returns (optional)

# Create the nodes
root = StrictPartialOrder(nodes=[online_order, phone_order, confirmation, pick_pack, shipping_label,
                                 logistics_handover, tracking_info, monitor_shipment, successful_delivery,
                                 feedback_returns])

# Define the order
root.order.add_edge(online_order, confirmation)
root.order.add_edge(phone_order, confirmation)
root.order.add_edge(confirmation, pick_pack)
root.order.add_edge(pick_pack, shipping_label)
root.order.add_edge(shipping_label, logistics_handover)
root.order.add_edge(logistics_handover, tracking_info)
root.order.add_edge(tracking_info, monitor_shipment)
root.order.add_edge(monitor_shipment, successful_delivery)

# Add feedback_returns as a concurrent activity
root.order.add_edge(confirmation, feedback_returns)

# Ensure that feedback_returns can occur at any time after confirmation
# This is a simplification as it doesn't model the actual concurrent behavior perfectly.
# A more accurate model would involve additional constructs or a more complex POWL representation.

# Final model
root