import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
signup = Transition(label='Customer signs up')
assign_access = Transition(label='Assign access')
generate_account = Transition(label='Generate account')
set_billing_triggers = Transition(label='Set automatic triggers for billing cycles')
send_updates = Transition(label='Send regular updates')
send_renewal = Transition(label='Send renewal notifications')
send_product_enhancements = Transition(label='Send product enhancements')
submit_cancel = Transition(label='Customer submits cancellation request')
deactivate = Transition(label='Deactivate subscription')
settle_balance = Transition(label='Settle final account balance')
apply_charges = Transition(label='apply charges')
apply_refund = Transition(label='apply refund')

# Define the partial order
root = StrictPartialOrder(nodes=[
    signup, assign_access, generate_account, set_billing_triggers, send_updates, send_renewal,
    send_product_enhancements, submit_cancel, deactivate, settle_balance, apply_charges, apply_refund
])

# Define the edges
root.order.add_edge(signup, assign_access)
root.order.add_edge(assign_access, generate_account)
root.order.add_edge(generate_account, set_billing_triggers)
root.order.add_edge(set_billing_triggers, send_updates)
root.order.add_edge(send_updates, send_renewal)
root.order.add_edge(send_updates, send_product_enhancements)
root.order.add_edge(submit_cancel, deactivate)
root.order.add_edge(deactivate, settle_balance)
root.order.add_edge(settle_balance, apply_charges)
root.order.add_edge(settle_balance, apply_refund)

print(root)