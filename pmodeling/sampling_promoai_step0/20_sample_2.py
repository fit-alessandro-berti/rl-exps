import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
guest_calls_room_service = Transition(label='Guest calls room service')
kitchen_prepares_food = Transition(label='Kitchen prepares food')
manager_assigns_order_to_waiter = Transition(label='Manager assigns order to waiter')
manager_gives_order_to_sommelier = Transition(label='Manager gives order to sommelier')
manager_submits_order_ticket_to_kitchen = Transition(label='Manager submits order ticket to kitchen')
manager_takes_down_the_order = Transition(label='Manager takes down the order')
sommelier_fetches_wine_and_prepares_alcoholic_beverages = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
waiter_debits_guests_account = Transition(label='Waiter debits guest\'s account')
waiter_delivers_order_to_guests_room = Transition(label='Waiter delivers order to guest\'s room')
waiter_preps_nonalcoholic_drinks = Transition(label='Waiter prepares nonalcoholic drinks')
waiter_readies_cart = Transition(label='Waiter readies cart')
waiter_returns_to_room_service_station = Transition(label='Waiter returns to room-service station')
waiter_waits_delays_debiting = Transition(label='Waiter waits/delays debiting')

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        guest_calls_room_service,
        kitchen_prepares_food,
        manager_assigns_order_to_waiter,
        manager_gives_order_to_sommelier,
        manager_submits_order_ticket_to_kitchen,
        manager_takes_down_the_order,
        sommelier_fetches_wine_and_prepares_alcoholic_beverages,
        waiter_debits_guests_account,
        waiter_delivers_order_to_guests_room,
        waiter_preps_nonalcoholic_drinks,
        waiter_readies_cart,
        waiter_returns_to_room_service_station,
        waiter_waits_delays_debiting
    ],
    order={
        (guest_calls_room_service, manager_takes_down_the_order): None,
        (guest_calls_room_service, manager_gives_order_to_sommelier): None,
        (manager_takes_down_the_order, manager_submits_order_ticket_to_kitchen): None,
        (manager_takes_down_the_order, manager_gives_order_to_sommelier): None,
        (manager_submits_order_ticket_to_kitchen, kitchen_prepares_food): None,
        (manager_gives_order_to_sommelier, sommelier_fetches_wine_and_prepares_alcoholic_beverages): None,
        (kitchen_prepares_food, waiter_debits_guests_account): None,
        (kitchen_prepares_food, waiter_delivers_order_to_guests_room): None,
        (kitchen_prepares_food, waiter_preps_nonalcoholic_drinks): None,
        (kitchen_prepares_food, waiter_readies_cart): None,
        (kitchen_prepares_food, waiter_returns_to_room_service_station): None,
        (kitchen_prepares_food, waiter_waits_delays_debiting): None,
        (waiter_debits_guests_account, waiter_returns_to_room_service_station): None,
        (waiter_debits_guests_account, waiter_waits_delays_debiting): None,
        (waiter_delivers_order_to_guests_room, waiter_returns_to_room_service_station): None,
        (waiter_delivers_order_to_guests_room, waiter_waits_delays_debiting): None,
        (waiter_preps_nonalcoholic_drinks, waiter_returns_to_room_service_station): None,
        (waiter_preps_nonalcoholic_drinks, waiter_waits_delays_debiting): None,
        (waiter_readies_cart, waiter_returns_to_room_service_station): None,
        (waiter_readies_cart, waiter_waits_delays_debiting): None,
        (waiter_returns_to_room_service_station, waiter_debits_guests_account): None,
        (waiter_waits_delays_debiting, waiter_debits_guests_account): None
    }
)

# Print the result
print(root)