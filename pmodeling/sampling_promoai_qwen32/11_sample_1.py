import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the loop for subscription management
subscription_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        send_regular_updates,
        send_product_enhancements,
        send_renewal_notifications,
        set_automatic_triggers_for_billing_cycles
    ]
)

# Define the choice for cancellation
cancellation_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[
        apply_charges,
        apply_refund
    ]
)

# Define the main flow of the process
root = StrictPartialOrder(
    nodes=[
        customer_signs_up,
        generate_account,
        assign_access,
        subscription_loop,
        customer_submits_cancellation_request,
        cancellation_choice,
        deactivate_subscription,
        settle_final_account_balance
    ]
)

# Define the order of the process
root.order.add_edge(customer_signs_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, subscription_loop)
root.order.add_edge(subscription_loop, customer_submits_cancellation_request)
root.order.add_edge(customer_submits_cancellation_request, cancellation_choice)
root.order.add_edge(cancellation_choice, deactivate_subscription)
root.order.add_edge(deactivate_subscription, settle_final_account_balance)