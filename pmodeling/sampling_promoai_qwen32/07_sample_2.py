import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
search = Transition(label='Customer searches for ticket')
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

# Define the sequence of activities
root = StrictPartialOrder(nodes=[search, select_route, select_date_time, provide_personal_info, provide_payment_details, generate_ticket, send_ticket_email, send_ticket_sms, update_inventory, send_reminder, send_instructions, complete_journey, post_travel_services])

# Define the order of activities
root.order.add_edge(search, select_route)
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

root