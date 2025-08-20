import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
search = Transition(label='Customer searches for ticket')
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
ticket_delivery = OperatorPOWL(operator=Operator.XOR, children=[send_ticket_email, send_ticket_sms])
travel_completion = OperatorPOWL(operator=Operator.XOR, children=[complete_journey, post_travel_feedback])

# Define loops
remind_loop = OperatorPOWL(operator=Operator.LOOP, children=[send_reminder, send_instructions])

# Define partial orders
order1 = StrictPartialOrder(nodes=[search, select_route, select_date_time, provide_info, provide_payment, generate_ticket])
order1.order.add_edge(search, select_route)
order1.order.add_edge(select_route, select_date_time)
order1.order.add_edge(select_date_time, provide_info)
order1.order.add_edge(provide_info, provide_payment)
order1.order.add_edge(provide_payment, generate_ticket)

order2 = StrictPartialOrder(nodes=[generate_ticket, ticket_delivery, update_inventory])
order2.order.add_edge(generate_ticket, ticket_delivery)
order2.order.add_edge(ticket_delivery, update_inventory)

order3 = StrictPartialOrder(nodes=[remind_loop, travel_completion])
order3.order.add_edge(remind_loop, travel_completion)

# Define root POWL
root = StrictPartialOrder(nodes=[order1, order2, order3])
root.order.add_edge(order1, order2)
root.order.add_edge(order2, order3)