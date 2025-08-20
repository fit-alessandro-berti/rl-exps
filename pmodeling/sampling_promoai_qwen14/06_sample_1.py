import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
customer_online = Transition(label='Customer places order online')
customer_phone = Transition(label='Customer places order over the phone')
generate_order = Transition(label='Generate and send order confirmation')
generate_label = Transition(label='Generate shipping label')
hand_over = Transition(label='Hand over order to logistics provider')
monitor = Transition(label='Monitor shipment')
pick_pack = Transition(label='Pick and pack items')
feedback = Transition(label='Process customer feedback or returns')
tracking = Transition(label='Send tracking information to customer')
delivery = Transition(label='Successful delivery')

# Define choice operator for customer placing order
customer_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_online, customer_phone])

# Define loop for monitoring shipment until successful delivery
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, feedback])

# Define root POWL model
root = StrictPartialOrder(nodes=[customer_choice, generate_order, generate_label, hand_over, monitor_loop, pick_pack, tracking, delivery])
root.order.add_edge(customer_choice, generate_order)
root.order.add_edge(generate_order, generate_label)
root.order.add_edge(generate_label, hand_over)
root.order.add_edge(hand_over, monitor_loop)
root.order.add_edge(monitor_loop, pick_pack)
root.order.add_edge(pick_pack, tracking)
root.order.add_edge(tracking, delivery)