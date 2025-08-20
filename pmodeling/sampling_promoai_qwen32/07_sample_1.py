import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
customer_searches_ticket = Transition(label='Customer searches for ticket')
select_route = Transition(label='Select route')
select_date_time = Transition(label='Select date and time')
provide_personal_info = Transition(label='Provide personal information')
provide_payment_details = Transition(label='Provide payment details')
generate_ticket = Transition(label='Generate ticket')
send_ticket_email = Transition(label='Send ticket via email')
send_ticket_sms = Transition(label='Send ticket via SMS')
update_seat_inventory = Transition(label='Update seat inventory')
send_reminder = Transition(label='Send reminder')
send_instructions = Transition(label='Send instructions')
customer_completes_journey = Transition(label='Customer completes journey')
post_travel_feedback_services = Transition(label='Post-travel feedback or services')

# Define a silent transition for skipping optional steps
skip = SilentTransition()

# Define the loop for reminders and instructions before travel
loop = OperatorPOWL(operator=Operator.LOOP, children=[send_reminder, send_instructions])

# Define the choice between sending the ticket via email or SMS
xor_send_ticket = OperatorPOWL(operator=Operator.XOR, children=[send_ticket_email, send_ticket_sms])

# Define the main workflow
root = StrictPartialOrder(nodes=[
    customer_searches_ticket,
    select_route,
    select_date_time,
    provide_personal_info,
    provide_payment_details,
    generate_ticket,
    xor_send_ticket,
    update_seat_inventory,
    loop,
    customer_completes_journey,
    post_travel_feedback_services
])

# Define the partial order
root.order.add_edge(customer_searches_ticket, select_route)
root.order.add_edge(select_route, select_date_time)
root.order.add_edge(select_date_time, provide_personal_info)
root.order.add_edge(provide_personal_info, provide_payment_details)
root.order.add_edge(provide_payment_details, generate_ticket)
root.order.add_edge(generate_ticket, xor_send_ticket)
root.order.add_edge(xor_send_ticket, update_seat_inventory)
root.order.add_edge(update_seat_inventory, loop)
root.order.add_edge(loop, customer_completes_journey)
root.order.add_edge(customer_completes_journey, post_travel_feedback_services)