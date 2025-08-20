import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities as transitions
receive_customer_inquiry = Transition(label='Receive customer inquiry')
collect_customer_info = Transition(label='Collect customer information')
guide_customer = Transition(label='Guide customer in selecting product/service')
place_order = Transition(label='Place order')
provide_quote = Transition(label='Provide quote')
address_customer_concerns = Transition(label='Address customer concerns or questions')
record_order = Transition(label='Record order in system')
send_order_confirmation = Transition(label='Send order confirmation to customer')

# Create operators for the process
xor1 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[provide_quote, address_customer_concerns])
xor2 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[guide_customer, xor1])
xor3 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[record_order, xor2])
xor4 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[place_order, xor3])

# Define the partial order structure
root = StrictPartialOrder(nodes=[receive_customer_inquiry, collect_customer_info, guide_customer, provide_quote, address_customer_concerns, record_order, send_order_confirmation, place_order])
root.order.add_edge(receive_customer_inquiry, collect_customer_info)
root.order.add_edge(collect_customer_info, guide_customer)
root.order.add_edge(guide_customer, xor1)
root.order.add_edge(xor1, provide_quote)
root.order.add_edge(xor1, address_customer_concerns)
root.order.add_edge(address_customer_concerns, xor2)
root.order.add_edge(xor2, guide_customer)
root.order.add_edge(xor2, record_order)
root.order.add_edge(record_order, xor3)
root.order.add_edge(xor3, place_order)
root.order.add_edge(xor3, send_order_confirmation)
root.order.add_edge(place_order, xor4)
root.order.add_edge(xor4, send_order_confirmation)

# Print the final POWL model
print(root)