import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
search_ticket = Transition(label='Customer searches for ticket')
select_route = Transition(label='Select route')
select_date_time = Transition(label='Select date and time')
provide_info = Transition(label='Provide personal information')
provide_payment = Transition(label='Provide payment details')
generate_ticket = Transition(label='Generate ticket')
send_ticket_email = Transition(label='Send ticket via email')
send_ticket_sms = Transition(label='Send ticket via SMS')
update_inventory = Transition(label='Update seat inventory')
send_reminder = Transition(label='Send reminder')
send_instructions = Transition(label='Send instructions')
complete_journey = Transition(label='Customer completes journey')
post_travel_feedback = Transition(label='Post-travel feedback or services')

# Define choices
send_ticket_choice = OperatorPOWL(operator=Operator.XOR, children=[send_ticket_email, send_ticket_sms])
post_travel_choice = OperatorPOWL(operator=Operator.XOR, children=[post_travel_feedback, SilentTransition()])

# Define loops
loop_reminder_instructions = OperatorPOWL(operator=Operator.LOOP, children=[send_reminder, send_instructions])

# Define partial orders
root = StrictPartialOrder(nodes=[search_ticket, select_route, select_date_time, provide_info, provide_payment, generate_ticket, send_ticket_choice, update_inventory, loop_reminder_instructions, complete_journey, post_travel_choice])

# Define dependencies
root.order.add_edge(search_ticket, select_route)
root.order.add_edge(select_route, select_date_time)
root.order.add_edge(select_date_time, provide_info)
root.order.add_edge(provide_info, provide_payment)
root.order.add_edge(provide_payment, generate_ticket)
root.order.add_edge(generate_ticket, send_ticket_choice)
root.order.add_edge(send_ticket_choice, update_inventory)
root.order.add_edge(update_inventory, loop_reminder_instructions)
root.order.add_edge(loop_reminder_instructions, complete_journey)
root.order.add_edge(complete_journey, post_travel_choice)