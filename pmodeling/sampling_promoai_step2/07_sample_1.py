import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
customer_searches_for_ticket = Transition(label='Customer searches for ticket')
select_route = Transition(label='Select route')
select_date_and_time = Transition(label='Select date and time')
provide_personal_information = Transition(label='Provide personal information')
provide_payment_details = Transition(label='Provide payment details')
generate_ticket = Transition(label='Generate ticket')
send_instructions = Transition(label='Send instructions')
send_reminder = Transition(label='Send reminder')
send_ticket_via_sms = Transition(label='Send ticket via SMS')
send_ticket_via_email = Transition(label='Send ticket via email')
update_seat_inventory = Transition(label='Update seat inventory')
customer_completes_journey = Transition(label='Customer completes journey')
post_travel_feedback_or_services = Transition(label='Post-travel feedback or services')

# Define the partial order
root = StrictPartialOrder(nodes=[
    customer_searches_for_ticket,
    select_route,
    select_date_and_time,
    provide_personal_information,
    provide_payment_details,
    generate_ticket,
    send_instructions,
    send_reminder,
    send_ticket_via_sms,
    send_ticket_via_email,
    update_seat_inventory,
    customer_completes_journey,
    post_travel_feedback_or_services
])

# Define the dependencies
root.order.add_edge(customer_searches_for_ticket, select_route)
root.order.add_edge(select_route, select_date_and_time)
root.order.add_edge(select_date_and_time, provide_personal_information)
root.order.add_edge(provide_personal_information, provide_payment_details)
root.order.add_edge(provide_payment_details, generate_ticket)
root.order.add_edge(generate_ticket, send_instructions)
root.order.add_edge(send_instructions, send_reminder)
root.order.add_edge(send_reminder, send_ticket_via_sms)
root.order.add_edge(send_ticket_via_sms, send_ticket_via_email)
root.order.add_edge(send_ticket_via_email, update_seat_inventory)
root.order.add_edge(update_seat_inventory, customer_completes_journey)
root.order.add_edge(customer_completes_journey, post_travel_feedback_or_services)

# Print the root POWL model
print(root)