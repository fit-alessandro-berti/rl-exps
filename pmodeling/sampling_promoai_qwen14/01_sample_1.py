import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

receive_inquiry = Transition(label='Receive customer inquiry')
collect_info = Transition(label='Collect customer information')
address_concerns = Transition(label='Address customer concerns or questions')
select_product = Transition(label='Guide customer in selecting product/service')
provide_quote = Transition(label='Provide quote')
approve_quote = Transition(label='Approve quote')
place_order = Transition(label='Place order')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the process tree structure
process_tree = StrictPartialOrder(nodes=[receive_inquiry, collect_info, address_concerns, select_product, provide_quote, approve_quote, place_order, record_order, send_confirmation])
process_tree.order.add_edge(receive_inquiry, collect_info)
process_tree.order.add_edge(collect_info, address_concerns)
process_tree.order.add_edge(address_concerns, select_product)
process_tree.order.add_edge(select_product, provide_quote)
process_tree.order.add_edge(provide_quote, approve_quote)
process_tree.order.add_edge(approve_quote, place_order)
process_tree.order.add_edge(place_order, record_order)
process_tree.order.add_edge(record_order, send_confirmation)

# Define the final POWL model
root = process_tree