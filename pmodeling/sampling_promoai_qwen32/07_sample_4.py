import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
search = Transition(label='Customer searches for ticket')
select_route = Transition(label='Select route')
select_date = Transition(label='Select date and time')
personal_info = Transition(label='Provide personal information')
payment = Transition(label='Provide payment details')
generate_ticket = Transition(label='Generate ticket')
send_email = Transition(label='Send ticket via email')
send_sms = Transition(label='Send ticket via SMS')
update_inventory = Transition(label='Update seat inventory')
reminder = Transition(label='Send reminder')
instructions = Transition(label='Send instructions')
complete_journey = Transition(label='Customer completes journey')
post_travel = Transition(label='Post-travel feedback or services')

# Define the process
root = StrictPartialOrder(nodes=[search, select_route, select_date, personal_info, payment, generate_ticket, send_email, send_sms, update_inventory, reminder, instructions, complete_journey, post_travel])

# Add order relations
root.order.add_edge(search, select_route)
root.order.add_edge(select_route, select_date)
root.order.add_edge(select_date, personal_info)
root.order.add_edge(personal_info, payment)
root.order.add_edge(payment, generate_ticket)
root.order.add_edge(generate_ticket, send_email)
root.order.add_edge(generate_ticket, send_sms)
root.order.add_edge(generate_ticket, update_inventory)
root.order.add_edge(update_inventory, reminder)
root.order.add_edge(update_inventory, instructions)
root.order.add_edge(reminder, complete_journey)
root.order.add_edge(instructions, complete_journey)
root.order.add_edge(complete_journey, post_travel)