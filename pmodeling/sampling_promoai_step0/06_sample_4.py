import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[process_customer_feedback_or_returns, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[pick_and_pack_items, monitor_shipment])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_places_order_online, customer_places_order_over_the_phone])
sequential = OperatorPOWL(operator=Operator.SEQ, children=[generate_and_send_order_confirmation, generate_shipping_label, hand_over_order_to_logistics_provider])

# Define the root node
root = StrictPartialOrder(nodes=[exclusive_choice, sequential, loop, xor, send_tracking_information_to_customer, successful_delivery])
root.order.add_edge(exclusive_choice, sequential)
root.order.add_edge(sequential, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, send_tracking_information_to_customer)
root.order.add_edge(send_tracking_information_to_customer, successful_delivery)

# Print the root node
print(root)