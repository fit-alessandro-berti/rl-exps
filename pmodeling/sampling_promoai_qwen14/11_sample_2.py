import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
customer_signs_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
set_automatic_triggers_for_billing_cycles = Transition(label='Set automatic triggers for billing cycles')
send_regular_updates = Transition(label='Send regular updates')
send_product_enhancements = Transition(label='Send product enhancements')
send_renewal_notifications = Transition(label='Send renewal notifications')
customer_submits_cancellation_request = Transition(label='Customer submits cancellation request')
deactivate_subscription = Transition(label='Deactivate subscription')
settle_final_account_balance = Transition(label='Settle final account balance')
apply_refund = Transition(label='apply refund')
apply_charges = Transition(label='apply charges')

# Define choices
send_updates_choice = OperatorPOWL(operator=Operator.XOR, children=[send_regular_updates, send_product_enhancements, send_renewal_notifications])
apply_refund_or_charges_choice = OperatorPOWL(operator=Operator.XOR, children=[apply_refund, apply_charges])

# Define loops
billing_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[set_automatic_triggers_for_billing_cycles, send_updates_choice])

# Define final POWL model
root = StrictPartialOrder(nodes=[customer_signs_up, generate_account, assign_access, billing_cycle_loop, customer_submits_cancellation_request, deactivate_subscription, settle_final_account_balance, apply_refund_or_charges_choice])
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, billing_cycle_loop)
root.order.add_edge(billing_cycle_loop, customer_submits_cancellation_request)
root.order.add_edge(customer_submits_cancellation_request, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_final_account_balance)
root.order.add_edge(settle_final_account_balance, apply_refund_or_charges_choice)