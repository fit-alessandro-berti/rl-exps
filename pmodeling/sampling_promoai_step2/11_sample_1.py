import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
assign_access = Transition(label='Assign access')
customer_signs_up = Transition(label='Customer signs up')
customer_submits_cancellation_request = Transition(label='Customer submits cancellation request')
deactivate_subscription = Transition(label='Deactivate subscription')
generate_account = Transition(label='Generate account')
send_product_enhancements = Transition(label='Send product enhancements')
send_regular_updates = Transition(label='Send regular updates')
send_renewal_notifications = Transition(label='Send renewal notifications')
set_automatic_triggers_for_billing_cycles = Transition(label='Set automatic triggers for billing cycles')
settle_final_account_balance = Transition(label='Settle final account balance')
apply_charges = Transition(label='apply charges')
apply_refund = Transition(label='apply refund')

# Define the partial order structure
root = StrictPartialOrder(nodes=[assign_access, customer_signs_up, customer_submits_cancellation_request, deactivate_subscription, generate_account, send_product_enhancements, send_regular_updates, send_renewal_notifications, set_automatic_triggers_for_billing_cycles, settle_final_account_balance, apply_charges, apply_refund])

# Define the dependencies between transitions
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(customer_submits_cancellation_request, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_final_account_balance)
root.order.add_edge(settle_final_account_balance, apply_charges)
root.order.add_edge(settle_final_account_balance, apply_refund)
root.order.add_edge(generate_account, send_product_enhancements)
root.order.add_edge(generate_account, send_regular_updates)
root.order.add_edge(generate_account, send_renewal_notifications)
root.order.add_edge(generate_account, set_automatic_triggers_for_billing_cycles)