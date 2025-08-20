import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
inquiry = Transition(label='Receive customer inquiry')
collect_info = Transition(label='Collect customer information')
address_concerns = Transition(label='Address customer concerns or questions')
guide_selection = Transition(label='Guide customer in selecting product/service')
provide_quote = Transition(label='Provide quote')
place_order = Transition(label='Place order')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the choice of whether the customer is interested
skip = SilentTransition()
interested = OperatorPOWL(operator=Operator.XOR, children=[guide_selection, skip])

# Define the loop for placing the order
order_loop = OperatorPOWL(operator=Operator.LOOP, children=[place_order, record_order])

# Define the main process
root = StrictPartialOrder(nodes=[inquiry, collect_info, address_concerns, interested, provide_quote, order_loop, send_confirmation])
root.order.add_edge(inquiry, collect_info)
root.order.add_edge(collect_info, address_concerns)
root.order.add_edge(address_concerns, interested)
root.order.add_edge(interested, provide_quote)
root.order.add_edge(provide_quote, order_loop)
root.order.add_edge(order_loop, send_confirmation)

# Print the POWL model
print(root)