import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
customer_signs_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
set_triggers = Transition(label='Set automatic triggers for billing cycles')
send_updates = Transition(label='Send regular updates')
send_enhancements = Transition(label='Send product enhancements')
send_notifications = Transition(label='Send renewal notifications')
customer_cancels = Transition(label='Customer submits cancellation request')
apply_refund = Transition(label='apply refund')
apply_charges = Transition(label='apply charges')
deactivate_subscription = Transition(label='Deactivate subscription')
settle_balance = Transition(label='Settle final account balance')

# Define the loop for billing cycles
billing_loop = OperatorPOWL(operator=Operator.LOOP, children=[set_triggers, send_updates, send_enhancements, send_notifications])

# Define the choice for refund or charges
refund_or_charges = OperatorPOWL(operator=Operator.XOR, children=[apply_refund, apply_charges])

# Define the main process flow
root = StrictPartialOrder(nodes=[customer_signs_up, generate_account, assign_access, billing_loop, customer_cancels, refund_or_charges, deactivate_subscription, settle_balance])

# Define the order of execution
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, billing_loop)
root.order.add_edge(billing_loop, customer_cancels)
root.order.add_edge(customer_cancels, refund_or_charges)
root.order.add_edge(refund_or_charges, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_balance)