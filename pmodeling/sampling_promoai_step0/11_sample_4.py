import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
customer_sign_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
set_automatic_triggers = Transition(label='Set automatic triggers for billing cycles')
send_regular_updates = Transition(label='Send regular updates')
send_product_enhancements = Transition(label='Send product enhancements')
send_renewal_notifications = Transition(label='Send renewal notifications')
settle_final_account_balance = Transition(label='Settle final account balance')
apply_refund = Transition(label='apply refund')
apply_charges = Transition(label='apply charges')
customer_submits_cancellation_request = Transition(label='Customer submits cancellation request')
deactivate_subscription = Transition(label='Deactivate subscription')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for customer actions
customer_actions = OperatorPOWL(operator=Operator.XOR, children=[customer_submits_cancellation_request, skip])

# Define loop for regular updates and notifications
regular_updates = OperatorPOWL(operator=Operator.LOOP, children=[send_regular_updates, send_product_enhancements, send_renewal_notifications])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    customer_sign_up, generate_account, assign_access, set_automatic_triggers, regular_updates,
    customer_actions, settle_final_account_balance, apply_charges, apply_refund, deactivate_subscription
])

# Add edges to define the workflow
root.order.add_edge(customer_sign_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, set_automatic_triggers)
root.order.add_edge(set_automatic_triggers, regular_updates)
root.order.add_edge(regular_updates, customer_actions)
root.order.add_edge(customer_actions, settle_final_account_balance)
root.order.add_edge(customer_actions, apply_charges)
root.order.add_edge(customer_actions, apply_refund)
root.order.add_edge(customer_actions, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_final_account_balance)

# Print the root POWL model
print(root)