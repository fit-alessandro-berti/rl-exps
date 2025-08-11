from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
search_for_ticket = Transition(label='Customer searches for ticket')
select_route = Transition(label='Select route')
select_date_time = Transition(label='Select date and time')
provide_personal_info = Transition(label='Provide personal information')
provide_payment_details = Transition(label='Provide payment details')
generate_ticket = Transition(label='Generate ticket')
send_ticket_sms = Transition(label='Send ticket via SMS')
send_ticket_email = Transition(label='Send ticket via email')
update_seat_inventory = Transition(label='Update seat inventory')
send_reminder = Transition(label='Send reminder')
send_instructions = Transition(label='Send instructions')
customer_completes_journey = Transition(label='Customer completes journey')
post_travel_feedback = Transition(label='Post-travel feedback or services')

# Define the partial order
root = StrictPartialOrder(nodes=[
    search_for_ticket,
    select_route,
    select_date_time,
    provide_personal_info,
    provide_payment_details,
    generate_ticket,
    send_ticket_sms,
    send_ticket_email,
    update_seat_inventory,
    send_reminder,
    send_instructions,
    customer_completes_journey,
    post_travel_feedback
])

# Define the partial order dependencies
root.order.add_edge(search_for_ticket, select_route)
root.order.add_edge(select_route, select_date_time)
root.order.add_edge(select_date_time, provide_personal_info)
root.order.add_edge(provide_personal_info, provide_payment_details)
root.order.add_edge(provide_payment_details, generate_ticket)
root.order.add_edge(generate_ticket, send_ticket_sms)
root.order.add_edge(generate_ticket, send_ticket_email)
root.order.add_edge(generate_ticket, update_seat_inventory)
root.order.add_edge(update_seat_inventory, send_reminder)
root.order.add_edge(update_seat_inventory, send_instructions)
root.order.add_edge(send_reminder, customer_completes_journey)
root.order.add_edge(send_instructions, customer_completes_journey)
root.order.add_edge(customer_completes_journey, post_travel_feedback)