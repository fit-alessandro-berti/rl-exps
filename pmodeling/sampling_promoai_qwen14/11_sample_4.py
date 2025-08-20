import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
sign_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
set_triggers = Transition(label='Set automatic triggers for billing cycles')
send_updates = Transition(label='Send regular updates')
send_enhancements = Transition(label='Send product enhancements')
send_notifications = Transition(label='Send renewal notifications')
cancel_request = Transition(label='Customer submits cancellation request')
deactivate_subscription = Transition(label='Deactivate subscription')
settle_balance = Transition(label='Settle final account balance')
apply_refund = Transition(label='apply refund')
apply_charges = Transition(label='apply charges')

# Define silent transitions
skip = SilentTransition()

# Define loop
billing_loop = OperatorPOWL(operator=Operator.LOOP, children=[set_triggers])

# Define exclusive choices
refund_or_charges = OperatorPOWL(operator=Operator.XOR, children=[apply_refund, apply_charges])

# Define partial orders
root = StrictPartialOrder(nodes=[sign_up, generate_account, assign_access, billing_loop, send_updates, send_enhancements, send_notifications, cancel_request, deactivate_subscription, settle_balance, refund_or_charges])

# Define order
root.order.add_edge(sign_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, billing_loop)
root.order.add_edge(billing_loop, send_updates)
root.order.add_edge(send_updates, send_enhancements)
root.order.add_edge(send_enhancements, send_notifications)
root.order.add_edge(cancel_request, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_balance)
root.order.add_edge(settle_balance, refund_or_charges)