import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
customer_signs_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
set_automatic_triggers = Transition(label='Set automatic triggers for billing cycles')
send_regular_updates = Transition(label='Send regular updates')
send_product_enhancements = Transition(label='Send product enhancements')
send_renewal_notifications = Transition(label='Send renewal notifications')
customer_submits_cancellation_request = Transition(label='Customer submits cancellation request')
apply_refund = Transition(label='apply refund')
apply_charges = Transition(label='apply charges')
deactivate_subscription = Transition(label='Deactivate subscription')
settle_final_account_balance = Transition(label='Settle final account balance')

# Define parallel activities (concurrent updates, enhancements, and notifications)
concurrent_activities = OperatorPOWL(operator=Operator.PARALLEL, children=[
    send_regular_updates,
    send_product_enhancements,
    send_renewal_notifications
])

# Define loop for concurrent activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[concurrent_activities])

# Define choice for cancellation handling
cancellation_handling = OperatorPOWL(operator=Operator.XOR, children=[
    apply_refund,
    apply_charges
])

# Define main process structure
main_process = StrictPartialOrder(nodes=[
    customer_signs_up,
    generate_account,
    assign_access,
    set_automatic_triggers,
    loop,
    customer_submits_cancellation_request,
    cancellation_handling,
    deactivate_subscription,
    settle_final_account_balance
])

# Define dependencies
main_process.order.add_edge(customer_signs_up, generate_account)
main_process.order.add_edge(generate_account, assign_access)
main_process.order.add_edge(assign_access, set_automatic_triggers)
main_process.order.add_edge(set_automatic_triggers, loop)
main_process.order.add_edge(loop, customer_submits_cancellation_request)
main_process.order.add_edge(customer_submits_cancellation_request, cancellation_handling)
main_process.order.add_edge(cancellation_handling, deactivate_subscription)
main_process.order.add_edge(deactivate_subscription, settle_final_account_balance)

# Set root node
root = main_process