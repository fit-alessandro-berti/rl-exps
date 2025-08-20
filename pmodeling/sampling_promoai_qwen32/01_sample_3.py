import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
receive_inquiry = Transition(label='Receive customer inquiry')
collect_info = Transition(label='Collect customer information')
address_concerns = Transition(label='Address customer concerns or questions')
guide_selection = Transition(label='Guide customer in selecting product/service')
provide_quote = Transition(label='Provide quote')
place_order = Transition(label='Place order')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')

# Define the POWL model
root = StrictPartialOrder(nodes=[receive_inquiry, collect_info, address_concerns, guide_selection, provide_quote, place_order, record_order, send_confirmation])

# Define the partial order (dependencies)
root.order.add_edge(receive_inquiry, collect_info)
root.order.add_edge(collect_info, address_concerns)
root.order.add_edge(address_concerns, guide_selection)
root.order.add_edge(guide_selection, provide_quote)
root.order.add_edge(provide_quote, place_order)
root.order.add_edge(place_order, record_order)
root.order.add_edge(record_order, send_confirmation)