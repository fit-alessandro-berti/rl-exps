import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_billing = OperatorPOWL(operator=Operator.LOOP, children=[set_automatic_triggers_for_billing_cycles, settle_final_account_balance])
loop_updates = OperatorPOWL(operator=Operator.LOOP, children=[send_regular_updates, send_product_enhancements, send_renewal_notifications])
xor_billing_updates = OperatorPOWL(operator=Operator.XOR, children=[loop_billing, loop_updates])

xor_billing_updates.order.add_edge(loop_billing, loop_updates)
xor_billing_updates.order.add_edge(loop_updates, loop_billing)

root = StrictPartialOrder(nodes=[customer_signs_up, generate_account, xor_billing_updates, customer_submits_cancellation_request, deactivate_subscription])
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, xor_billing_updates)
root.order.add_edge(customer_submits_cancellation_request, deactivate_subscription)
root.order.add_edge(deactivate_subscription, apply_charges)
root.order.add_edge(deactivate_subscription, apply_refund)

print(root)