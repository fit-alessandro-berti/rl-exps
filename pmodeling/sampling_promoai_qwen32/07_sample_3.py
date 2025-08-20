import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
search_ticket = Transition(label='Customer searches for ticket')
select_route = Transition(label='Select route')
select_date_time = Transition(label='Select date and time')
provide_personal_info = Transition(label='Provide personal information')
provide_payment_details = Transition(label='Provide payment details')
generate_ticket = Transition(label='Generate ticket')
send_ticket_email = Transition(label='Send ticket via email')
send_ticket_sms = Transition(label='Send ticket via SMS')
update_inventory = Transition(label='Update seat inventory')
send_reminder = Transition(label='Send reminder')
send_instructions = Transition(label='Send instructions')
complete_journey = Transition(label='Customer completes journey')
post_travel_services = Transition(label='Post-travel feedback or services')

# Define the partial order
root = StrictPartialOrder(nodes=[search_ticket, select_route, select_date_time, provide_personal_info, provide_payment_details, generate_ticket, send_ticket_email, send_ticket_sms, update_inventory, send_reminder, send_instructions, complete_journey, post_travel_services])

# Define the order (dependencies)
root.order.add_edge(search_ticket, select_route)
root.order.add_edge(select_route, select_date_time)
root.order.add_edge(select_date_time, provide_personal_info)
root.order.add_edge(provide_personal_info, provide_payment_details)
root.order.add_edge(provide_payment_details, generate_ticket)
root.order.add_edge(generate_ticket, send_ticket_email)
root.order.add_edge(generate_ticket, send_ticket_sms)
root.order.add_edge(generate_ticket, update_inventory)
root.order.add_edge(update_inventory, send_reminder)
root.order.add_edge(update_inventory, send_instructions)
root.order.add_edge(send_reminder, complete_journey)
root.order.add_edge(send_instructions, complete_journey)
root.order.add_edge(complete_journey, post_travel_services)

# Define the choice for sending the ticket
send_ticket_xor = OperatorPOWL(operator=Operator.XOR, children=[send_ticket_email, send_ticket_sms])
root.nodes.append(send_ticket_xor)
root.order.add_edge(generate_ticket, send_ticket_xor)

# Define the loop for reminders and instructions
reminder_loop = OperatorPOWL(operator=Operator.LOOP, children=[send_reminder, send_instructions])
root.nodes.append(reminder_loop)
root.order.add_edge(update_inventory, reminder_loop)

# Define the choice for post-travel services
post_travel_xor = OperatorPOWL(operator=Operator.XOR, children=[post_travel_services, SilentTransition()])
root.nodes.append(post_travel_xor)
root.order.add_edge(complete_journey, post_travel_xor)

# Final model
root