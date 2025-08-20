import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
place_order_online = Transition(label='Customer places order online')
place_order_phone = Transition(label='Customer places order over the phone')
generate_confirmation = Transition(label='Generate and send order confirmation')
generate_shipping_label = Transition(label='Generate shipping label')
hand_over_order = Transition(label='Hand over order to logistics provider')
monitor_shipment = Transition(label='Monitor shipment')
pick_pack_items = Transition(label='Pick and pack items')
process_feedback_returns = Transition(label='Process customer feedback or returns')
send_tracking_info = Transition(label='Send tracking information to customer')
successful_delivery = Transition(label='Successful delivery')

# Create XOR for order placement
order_placement_xor = OperatorPOWL(operator=Operator.XOR, children=[place_order_online, place_order_phone])

# Create sequence for order processing
order_processing_sequence = OperatorPOWL(operator=Operator.SEQUENCE, children=[order_placement_xor, generate_confirmation, pick_pack_items, generate_shipping_label, hand_over_order, send_tracking_info])

# Create loop for shipment monitoring
shipment_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_processing_sequence, monitor_shipment])

# Create XOR for post-delivery actions
post_delivery_xor = OperatorPOWL(operator=Operator.XOR, children=[successful_delivery, process_feedback_returns])

# Create partial order for the entire process
root = StrictPartialOrder(nodes=[shipment_monitoring_loop, post_delivery_xor])
root.order.add_edge(shipment_monitoring_loop, post_delivery_xor)