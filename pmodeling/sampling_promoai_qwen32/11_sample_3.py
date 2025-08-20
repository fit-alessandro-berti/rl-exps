import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
sign_up = Transition(label='Customer signs up')
generate_account = Transition(label='Generate account')
assign_access = Transition(label='Assign access')
set_triggers = Transition(label='Set automatic triggers for billing cycles')
send_updates = Transition(label='Send regular updates')
send_enhancements = Transition(label='Send product enhancements')
send_notifications = Transition(label='Send renewal notifications')
submit_request = Transition(label='Customer submits cancellation request')
process_request = Transition(label='Support team processes cancellation request')
apply_refund = Transition(label='Apply refund')
apply_charges = Transition(label='Apply charges')
deactivate = Transition(label='Deactivate subscription')
settle_balance = Transition(label='Settle final account balance')
skip = SilentTransition()

# Define the loops and choices
billing_cycle = OperatorPOWL(operator=Operator.LOOP, children=[set_triggers])
customer_choice = OperatorPOWL(operator=Operator.XOR, children=[send_updates, send_enhancements, send_notifications])
cancellation_choice = OperatorPOWL(operator=Operator.XOR, children=[apply_refund, apply_charges, skip])

# Define the strict partial order
root = StrictPartialOrder(nodes=[sign_up, generate_account, assign_access, billing_cycle, customer_choice, submit_request, process_request, cancellation_choice, deactivate, settle_balance])
root.order.add_edge(sign_up, generate_account)
root.order.add_edge(generate_account, assign_access)
root.order.add_edge(assign_access, billing_cycle)
root.order.add_edge(billing_cycle, customer_choice)
root.order.add_edge(customer_choice, submit_request)
root.order.add_edge(submit_request, process_request)
root.order.add_edge(process_request, cancellation_choice)
root.order.add_edge(cancellation_choice, deactivate)
root.order.add_edge(deactivate, settle_balance)