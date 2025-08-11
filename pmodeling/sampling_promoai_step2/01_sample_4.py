import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
# Start from receiving a customer inquiry
receive_inquiry = Transition(label='Receive customer inquiry')
# Address customer concerns or questions
address_concerns = Transition(label='Address customer concerns or questions')
# Collect customer information
collect_info = Transition(label='Collect customer information')
# Guide customer in selecting product/service
guide_selection = Transition(label='Guide customer in selecting product/service')
# Provide quote
provide_quote = Transition(label='Provide quote')
# Place order
place_order = Transition(label='Place order')
# Record order in system
record_order = Transition(label='Record order in system')
# Send order confirmation to customer
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the partial order
root = StrictPartialOrder(nodes=[
    receive_inquiry,
    address_concerns,
    collect_info,
    guide_selection,
    provide_quote,
    place_order,
    record_order,
    send_confirmation
])

# Define the dependencies between activities
root.order.add_edge(receive_inquiry, address_concerns)
root.order.add_edge(address_concerns, collect_info)
root.order.add_edge(collect_info, guide_selection)
root.order.add_edge(guide_selection, provide_quote)
root.order.add_edge(provide_quote, place_order)
root.order.add_edge(place_order, record_order)
root.order.add_edge(record_order, send_confirmation)

# Print the final POWL model
print(root)