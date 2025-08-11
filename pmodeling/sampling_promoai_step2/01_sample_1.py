import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
address_customer = Transition(label='Address customer concerns or questions')
collect_info = Transition(label='Collect customer information')
guide_select = Transition(label='Guide customer in selecting product/service')
place_order = Transition(label='Place order')
provide_quote = Transition(label='Provide quote')
receive_inquiry = Transition(label='Receive customer inquiry')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the workflow
root = StrictPartialOrder(nodes=[
    address_customer,
    collect_info,
    guide_select,
    provide_quote,
    receive_inquiry,
    record_order,
    send_confirmation
])

# Define the dependencies
root.order.add_edge(address_customer, collect_info)
root.order.add_edge(collect_info, guide_select)
root.order.add_edge(guide_select, provide_quote)
root.order.add_edge(provide_quote, receive_inquiry)
root.order.add_edge(receive_inquiry, record_order)
root.order.add_edge(record_order, send_confirmation)

print(root)