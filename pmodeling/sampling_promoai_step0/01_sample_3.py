import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
address_customer = Transition(label='Address customer concerns or questions')
collect_info = Transition(label='Collect customer information')
guide_customer = Transition(label='Guide customer in selecting product/service')
place_order = Transition(label='Place order')
provide_quote = Transition(label='Provide quote')
receive_inquiry = Transition(label='Receive customer inquiry')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the silent transitions
skip = SilentTransition()

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[place_order, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[provide_quote, record_order, send_confirmation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor, receive_inquiry])
root = StrictPartialOrder(nodes=[xor2, address_customer, collect_info, guide_customer])

# Define the dependencies
root.order.add_edge(address_customer, xor2)
root.order.add_edge(collect_info, xor2)
root.order.add_edge(guide_customer, xor2)
root.order.add_edge(receive_inquiry, xor2)
root.order.add_edge(provide_quote, loop)
root.order.add_edge(record_order, loop)
root.order.add_edge(send_confirmation, loop)

# Print the POWL model
print(root)