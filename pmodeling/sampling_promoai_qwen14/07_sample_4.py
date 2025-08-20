import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
customer_searches = Transition(label='Customer searches for ticket')
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
post_travel_feedback = Transition(label='Post-travel feedback or services')

# Define the control-flow operators
xor_provide_personal_info = OperatorPOWL(operator=Operator.XOR, children=[provide_personal_info, SilentTransition()])
xor_send_ticket = OperatorPOWL(operator=Operator.XOR, children=[send_ticket_email, send_ticket_sms])
xor_post_travel_feedback = OperatorPOWL(operator=Operator.XOR, children=[post_travel_feedback, SilentTransition()])

# Define the loops
loop_send_reminder = OperatorPOWL(operator=Operator.LOOP, children=[send_reminder, SilentTransition()])
loop_send_instructions = OperatorPOWL(operator=Operator.LOOP, children=[send_instructions, SilentTransition()])

# Define the main workflow
root = StrictPartialOrder(nodes=[
    customer_searches,
    select_route,
    select_date_time,
    xor_provide_personal_info,
    provide_payment_details,
    generate_ticket,
    xor_send_ticket,
    update_seat_inventory,
    loop_send_reminder,
    loop_send_instructions,
    customer_completes_journey,
    xor_post_travel_feedback
])

# Define the order of execution
root.order.add_edge(customer_searches, select_route)
root.order.add_edge(select_route, select_date_time)
root.order.add_edge(select_date_time, xor_provide_personal_info)
root.order.add_edge(xor_provide_personal_info, provide_payment_details)
root.order.add_edge(provide_payment_details, generate_ticket)
root.order.add_edge(generate_ticket, xor_send_ticket)
root.order.add_edge(xor_send_ticket, update_seat_inventory)
root.order.add_edge(update_seat_inventory, loop_send_reminder)
root.order.add_edge(loop_send_reminder, loop_send_instructions)
root.order.add_edge(loop_send_instructions, customer_completes_journey)
root.order.add_edge(customer_completes_journey, xor_post_travel_feedback)