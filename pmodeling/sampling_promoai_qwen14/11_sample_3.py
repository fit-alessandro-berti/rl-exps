import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
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

# Define the XOR operator for cancellation request
xor_cancellation_request = OperatorPOWL(operator=Operator.XOR, children=[apply_refund, apply_charges])

# Define the loop for billing cycles
loop_billing_cycles = OperatorPOWL(operator=Operator.LOOP, children=[set_automatic_triggers_for_billing_cycles, send_regular_updates])

# Define the partial order
root = StrictPartialOrder(nodes=[customer_signs_up, generate_account, assign_access, loop_billing_cycles, send_product_enhancements, send_renewal_notifications, customer_submits_cancellation_request, deactivate_subscription, settle_final_account_balance, xor_cancellation_request])

# Define the order of transitions
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, loop_billing_cycles)
root.order.add_edge(loop_billing_cycles, send_product_enhancements)
root.order.add_edge(loop_billing_cycles, send_renewal_notifications)
root.order.add_edge(send_product_enhancements, customer_submits_cancellation_request)
root.order.add_edge(send_renewal_notifications, customer_submits_cancellation_request)
root.order.add_edge(customer_submits_cancellation_request, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_final_account_balance)
root.order.add_edge(settle_final_account_balance, xor_cancellation_request)