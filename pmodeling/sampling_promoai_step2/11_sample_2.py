import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
customer_signs_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
send_regular_updates = Transition(label='Send regular updates')
send_product_enhancements = Transition(label='Send product enhancements')
send_renewal_notifications = Transition(label='Send renewal notifications')
set_auto_triggers = Transition(label='Set automatic triggers for billing cycles')
settle_final_balance = Transition(label='Settle final account balance')
apply_charges = Transition(label='apply charges')
apply_refund = Transition(label='apply refund')
customer_cancels = Transition(label='Customer submits cancellation request')
deactivate_subscription = Transition(label='Deactivate subscription')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    customer_signs_up,
    generate_account,
    assign_access,
    send_regular_updates,
    send_product_enhancements,
    send_renewal_notifications,
    set_auto_triggers,
    settle_final_balance,
    apply_charges,
    apply_refund,
    customer_cancels,
    deactivate_subscription
])

# Define the dependencies between the nodes
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, send_regular_updates)
root.order.add_edge(assign_access, send_product_enhancements)
root.order.add_edge(assign_access, send_renewal_notifications)
root.order.add_edge(assign_access, set_auto_triggers)
root.order.add_edge(set_auto_triggers, settle_final_balance)
root.order.add_edge(settle_final_balance, apply_charges)
root.order.add_edge(settle_final_balance, apply_refund)
root.order.add_edge(customer_cancels, deactivate_subscription)

print(root)