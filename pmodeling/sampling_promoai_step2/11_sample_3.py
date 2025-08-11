import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
customer_sign_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
set_automatic_triggers = Transition(label='Set automatic triggers for billing cycles')
send_regular_updates = Transition(label='Send regular updates')
send_renewal_notifications = Transition(label='Send renewal notifications')
send_product_enhancements = Transition(label='Send product enhancements')
apply_charges = Transition(label='apply charges')
apply_refund = Transition(label='apply refund')
deactivate_subscription = Transition(label='Deactivate subscription')
settle_final_account_balance = Transition(label='Settle final account balance')
cancel_subscription_request = Transition(label='Customer submits cancellation request')

# Define partial order
root = StrictPartialOrder(nodes=[
    customer_sign_up,
    generate_account,
    set_automatic_triggers,
    send_regular_updates,
    send_renewal_notifications,
    send_product_enhancements,
    apply_charges,
    apply_refund,
    deactivate_subscription,
    settle_final_account_balance,
    cancel_subscription_request
])

# Define dependencies between activities
root.order.add_edge(customer_sign_up, generate_account)
root.order.add_edge(generate_account, set_automatic_triggers)
root.order.add_edge(set_automatic_triggers, send_regular_updates)
root.order.add_edge(set_automatic_triggers, send_renewal_notifications)
root.order.add_edge(set_automatic_triggers, send_product_enhancements)
root.order.add_edge(send_regular_updates, apply_charges)
root.order.add_edge(send_renewal_notifications, apply_refund)
root.order.add_edge(send_product_enhancements, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_final_account_balance)
root.order.add_edge(cancel_subscription_request, apply_charges)
root.order.add_edge(cancel_subscription_request, apply_refund)
root.order.add_edge(cancel_subscription_request, deactivate_subscription)
root.order.add_edge(cancel_subscription_request, settle_final_account_balance)

# Print the root POWL model
print(root)