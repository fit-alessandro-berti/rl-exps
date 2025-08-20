import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
receive_inquiry = Transition(label='Receive customer inquiry')
collect_info = Transition(label='Collect customer information')
address_concerns = Transition(label='Address customer concerns or questions')
guide_selection = Transition(label='Guide customer in selecting product/service')
provide_quote = Transition(label='Provide quote')
place_order = Transition(label='Place order')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the choice node for customer interest
customer_interest = OperatorPOWL(operator=Operator.XOR, children=[guide_selection, SilentTransition()])

# Define the loop node for order placement and confirmation
order_loop = OperatorPOWL(operator=Operator.LOOP, children=[place_order, record_order, send_confirmation])

# Define the root POWL model
root = StrictPartialOrder(nodes=[receive_inquiry, collect_info, address_concerns, customer_interest, provide_quote, order_loop])
root.order.add_edge(receive_inquiry, collect_info)
root.order.add_edge(collect_info, address_concerns)
root.order.add_edge(address_concerns, customer_interest)
root.order.add_edge(customer_interest, provide_quote)
root.order.add_edge(provide_quote, order_loop)