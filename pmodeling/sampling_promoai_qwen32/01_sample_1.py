import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
inquiry = Transition(label='Receive customer inquiry')
collect_info = Transition(label='Collect customer information')
address_concerns = Transition(label='Address customer concerns or questions')
guide_selection = Transition(label='Guide customer in selecting product/service')
provide_quote = Transition(label='Provide quote')
approve_quote = Transition(label='Approve quote')
place_order = Transition(label='Place order')
record_order = Transition(label='Record order in system')
send_confirmation = Transition(label='Send order confirmation to customer')
skip = SilentTransition()

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[approve_quote, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[provide_quote, approve_quote, place_order, record_order, send_confirmation])
xor_loop = OperatorPOWL(operator=Operator.XOR, children=[loop, skip])

# Define partial order
root = StrictPartialOrder(nodes=[inquiry, collect_info, address_concerns, guide_selection, xor_loop])
root.order.add_edge(inquiry, collect_info)
root.order.add_edge(collect_info, address_concerns)
root.order.add_edge(address_concerns, guide_selection)
root.order.add_edge(guide_selection, xor_loop)