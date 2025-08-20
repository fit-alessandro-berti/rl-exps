import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Customer_places_order_online = Transition(label='Customer places order online')
Customer_places_order_over_the_phone = Transition(label='Customer places order over the phone')
Generate_and_send_order_confirmation = Transition(label='Generate and send order confirmation')
Generate_shipping_label = Transition(label='Generate shipping label')
Hand_over_order_to_logistics_provider = Transition(label='Hand over order to logistics provider')
Monitor_shipment = Transition(label='Monitor shipment')
Pick_and_pack_items = Transition(label='Pick and pack items')
Process_customer_feedback_or_returns = Transition(label='Process customer feedback or returns')
Send_tracking_information_to_customer = Transition(label='Send tracking information to customer')
Successful_delivery = Transition(label='Successful delivery')

# Define the silent transition
skip = SilentTransition()

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Pick_and_pack_items, Monitor_shipment])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Generate_shipping_label, Hand_over_order_to_logistics_provider])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[Process_customer_feedback_or_returns, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[Customer_places_order_online, Customer_places_order_over_the_phone, Generate_and_send_order_confirmation, loop1, loop2, Generate_shipping_label, Hand_over_order_to_logistics_provider, Monitor_shipment, Pick_and_pack_items, Send_tracking_information_to_customer, Successful_delivery])
root.order.add_edge(Customer_places_order_online, Generate_and_send_order_confirmation)
root.order.add_edge(Generate_and_send_order_confirmation, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, Generate_shipping_label)
root.order.add_edge(Generate_shipping_label, Hand_over_order_to_logistics_provider)
root.order.add_edge(Hand_over_order_to_logistics_provider, Monitor_shipment)
root.order.add_edge(Monitor_shipment, Pick_and_pack_items)
root.order.add_edge(Pick_and_pack_items, loop1)
root.order.add_edge(Generate_and_send_order_confirmation, loop2)
root.order.add_edge(loop2, Generate_shipping_label)
root.order.add_edge(Generate_shipping_label, Hand_over_order_to_logistics_provider)
root.order.add_edge(Hand_over_order_to_logistics_provider, Monitor_shipment)
root.order.add_edge(Monitor_shipment, Pick_and_pack_items)
root.order.add_edge(Pick_and_pack_items, loop1)
root.order.add_edge(Generate_and_send_order_confirmation, xor)
root.order.add_edge(xor, Send_tracking_information_to_customer)
root.order.add_edge(Generate_and_send_order_confirmation, Successful_delivery)