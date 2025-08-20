import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Guest_calls_room_service = Transition(label='Guest calls room service')
Kitchen_prepares_food = Transition(label='Kitchen prepares food')
Manager_assigns_order_to_waiter = Transition(label='Manager assigns order to waiter')
Manager_gives_order_to_sommelier = Transition(label='Manager gives order to sommelier')
Manager_submits_order_ticket_to_kitchen = Transition(label='Manager submits order ticket to kitchen')
Manager_takes_down_the_order = Transition(label='Manager takes down the order')
Sommelier_fetches_wine_and_prepare_alcoholic_beverages = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
Waiter_debits_guests_account = Transition(label='Waiter debits guest\'s account')
Waiter_delivers_order_to_guests_room = Transition(label='Waiter delivers order to guest\'s room')
Waiter_prepares_nonalcoholic_drinks = Transition(label='Waiter prepares nonalcoholic drinks')
Waiter_readies_cart = Transition(label='Waiter readies cart')
Waiter_returns_to_room_service_station = Transition(label='Waiter returns to room-service station')
Waiter_waits_delays_debiting = Transition(label='Waiter waits/delays debiting')

# Define silent transitions
skip = SilentTransition()

# Define loops
loop_kitchen_sommelier = OperatorPOWL(operator=Operator.LOOP, children=[Kitchen_prepares_food, Sommelier_fetches_wine_and_prepare_alcoholic_beverages])
loop_waiter = OperatorPOWL(operator=Operator.LOOP, children=[Waiter_prepares_nonalcoholic_drinks, Waiter_delivers_order_to_guests_room])

# Define choices
xor_sommelier = OperatorPOWL(operator=Operator.XOR, children=[Sommelier_fetches_wine_and_prepare_alcoholic_beverages, skip])

# Define partial orders
order1 = StrictPartialOrder(nodes=[Manager_takes_down_the_order, Manager_submits_order_ticket_to_kitchen])
order1.order.add_edge(Manager_takes_down_the_order, Manager_submits_order_ticket_to_kitchen)

order2 = StrictPartialOrder(nodes=[Manager_gives_order_to_sommelier, xor_sommelier])
order2.order.add_edge(Manager_gives_order_to_sommelier, xor_sommelier)

order3 = StrictPartialOrder(nodes=[Manager_assigns_order_to_waiter, Waiter_readies_cart, Waiter_delivers_order_to_guests_room])
order3.order.add_edge(Manager_assigns_order_to_waiter, Waiter_readies_cart)
order3.order.add_edge(Waiter_readies_cart, Waiter_delivers_order_to_guests_room)

# Define root
root = StrictPartialOrder(nodes=[Guest_calls_room_service, order1, order2, loop_kitchen_sommelier, loop_waiter, Waiter_returns_to_room_service_station, Waiter_debits_guests_account, Waiter_waits_delays_debiting])
root.order.add_edge(Guest_calls_room_service, order1)
root.order.add_edge(order1, order2)
root.order.add_edge(order2, loop_kitchen_sommelier)
root.order.add_edge(loop_kitchen_sommelier, loop_waiter)
root.order.add_edge(loop_waiter, Waiter_returns_to_room_service_station)
root.order.add_edge(Waiter_returns_to_room_service_station, Waiter_debits_guests_account)
root.order.add_edge(Waiter_debits_guests_account, Waiter_waits_delays_debiting)