import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Customer_completes_journey = Transition(label='Customer completes journey')
Customer_searches_for_ticket = Transition(label='Customer searches for ticket')
Generate_ticket = Transition(label='Generate ticket')
Post_travel_feedback_or_services = Transition(label='Post-travel feedback or services')
Provide_payment_details = Transition(label='Provide payment details')
Provide_personal_information = Transition(label='Provide personal information')
Select_date_and_time = Transition(label='Select date and time')
Select_route = Transition(label='Select route')
Send_instructions = Transition(label='Send instructions')
Send_reminder = Transition(label='Send reminder')
Send_ticket_via_SMS = Transition(label='Send ticket via SMS')
Send_ticket_via_email = Transition(label='Send ticket via email')
Update_seat_inventory = Transition(label='Update seat inventory')

# Define loops and choices
loop_customer_journey = OperatorPOWL(operator=Operator.LOOP, children=[Customer_completes_journey])
choice_send_ticket = OperatorPOWL(operator=Operator.XOR, children=[Send_ticket_via_SMS, Send_ticket_via_email])
loop_post_travel = OperatorPOWL(operator=Operator.LOOP, children=[Post_travel_feedback_or_services])

# Define partial order
root = StrictPartialOrder(nodes=[
    Customer_searches_for_ticket,
    Select_route,
    Select_date_and_time,
    Provide_personal_information,
    Provide_payment_details,
    Generate_ticket,
    choice_send_ticket,
    Update_seat_inventory,
    Send_reminder,
    Send_instructions,
    loop_customer_journey,
    loop_post_travel
])

# Define dependencies
root.order.add_edge(Customer_searches_for_ticket, Select_route)
root.order.add_edge(Select_route, Select_date_and_time)
root.order.add_edge(Select_date_and_time, Provide_personal_information)
root.order.add_edge(Provide_personal_information, Provide_payment_details)
root.order.add_edge(Provide_payment_details, Generate_ticket)
root.order.add_edge(Generate_ticket, choice_send_ticket)
root.order.add_edge(choice_send_ticket, Update_seat_inventory)
root.order.add_edge(Update_seat_inventory, Send_reminder)
root.order.add_edge(Send_reminder, Send_instructions)
root.order.add_edge(Send_instructions, loop_customer_journey)
root.order.add_edge(loop_customer_journey, loop_post_travel)