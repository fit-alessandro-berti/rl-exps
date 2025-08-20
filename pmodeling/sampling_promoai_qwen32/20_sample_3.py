import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
guest_calls_room_service = Transition(label='Guest calls room service')
kitchen_prepares_food = Transition(label='Kitchen prepares food')
manager_assigns_order_to_waiter = Transition(label='Manager assigns order to waiter')
manager_gives_order_to_sommelier = Transition(label='Manager gives order to sommelier')
manager_submits_order_ticket_to_kitchen = Transition(label='Manager submits order ticket to kitchen')
manager_takes_down_the_order = Transition(label='Manager takes down the order')
sommelier_fetches_wine_and_prepare_alcoholic_beverages = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
waiter_debits_guests_account = Transition(label='Waiter debits guest\'s account')
waiter_delivers_order_to_guests_room = Transition(label='Waiter delivers order to guest\'s room')
waiter_prepares_nonalcoholic_drinks = Transition(label='Waiter prepares nonalcoholic drinks')
waiter_readies_cart = Transition(label='Waiter readies cart')
waiter_returns_to_room_service_station = Transition(label='Waiter returns to room-service station')
waiter_waits_delays_debiting = Transition(label='Waiter waits/delays debiting')

# Define choices and loops
choice_alcoholic_beverage = OperatorPOWL(operator=Operator.XOR, children=[sommelier_fetches_wine_and_prepare_alcoholic_beverages, SilentTransition()])
loop_debiting = OperatorPOWL(operator=Operator.LOOP, children=[waiter_debits_guests_account, waiter_waits_delays_debiting])

# Define the partial order
root = StrictPartialOrder(nodes=[guest_calls_room_service, manager_takes_down_the_order, manager_submits_order_ticket_to_kitchen, manager_gives_order_to_sommelier, manager_assigns_order_to_waiter, kitchen_prepares_food, choice_alcoholic_beverage, waiter_readies_cart, waiter_prepares_nonalcoholic_drinks, waiter_delivers_order_to_guests_room, waiter_returns_to_room_service_station, loop_debiting])
root.order.add_edge(guest_calls_room_service, manager_takes_down_the_order)
root.order.add_edge(manager_takes_down_the_order, manager_submits_order_ticket_to_kitchen)
root.order.add_edge(manager_takes_down_the_order, manager_gives_order_to_sommelier)
root.order.add_edge(manager_takes_down_the_order, manager_assigns_order_to_waiter)
root.order.add_edge(manager_submits_order_ticket_to_kitchen, kitchen_prepares_food)
root.order.add_edge(manager_gives_order_to_sommelier, choice_alcoholic_beverage)
root.order.add_edge(manager_assigns_order_to_waiter, waiter_readies_cart)
root.order.add_edge(manager_assigns_order_to_waiter, waiter_prepares_nonalcoholic_drinks)
root.order.add_edge(kitchen_prepares_food, waiter_delivers_order_to_guests_room)
root.order.add_edge(choice_alcoholic_beverage, waiter_delivers_order_to_guests_room)
root.order.add_edge(waiter_readies_cart, waiter_delivers_order_to_guests_room)
root.order.add_edge(waiter_prepares_nonalcoholic_drinks, waiter_delivers_order_to_guests_room)
root.order.add_edge(waiter_delivers_order_to_guests_room, waiter_returns_to_room_service_station)
root.order.add_edge(waiter_returns_to_room_service_station, loop_debiting)