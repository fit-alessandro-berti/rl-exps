import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
guest_calls = Transition(label='Guest calls room service')
manager_takes_order = Transition(label='Manager takes down the order')
manager_submits_ticket = Transition(label='Manager submits order ticket to kitchen')
manager_assigns_waiter = Transition(label='Manager assigns order to waiter')
manager_gives_sommelier = Transition(label='Manager gives order to sommelier')
sommelier_fetches_wine = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
waiter_preps_nonalcoholic = Transition(label='Waiter prepares nonalcoholic drinks')
waiter_readies_cart = Transition(label='Waiter readies cart')
waiter_delivers_order = Transition(label='Waiter delivers order to guest's room')
waiter_debits_account = Transition(label='Waiter debits guest's account')
waiter_returns_station = Transition(label='Waiter returns to room-service station')
waiter_waits_debit = Transition(label='Waiter waits/delays debiting')

# Define operators
loop_food_and_wine = OperatorPOWL(operator=Operator.LOOP, children=[manager_submits_ticket, sommelier_fetches_wine])
choice_alcohol = OperatorPOWL(operator=Operator.XOR, children=[sommelier_fetches_wine, SilentTransition()])
choice_debit = OperatorPOWL(operator=Operator.XOR, children=[waiter_debits_account, waiter_waits_debit])

# Create partial order
nodes = [guest_calls, manager_takes_order, loop_food_and_wine, choice_alcohol, waiter_preps_nonalcoholic, waiter_readies_cart, waiter_delivers_order, choice_debit, waiter_returns_station]
order = set()
order.add_edge(guest_calls, manager_takes_order)
order.add_edge(manager_takes_order, loop_food_and_wine)
order.add_edge(loop_food_and_wine, choice_alcohol)
order.add_edge(choice_alcohol, waiter_preps_nonalcoholic)
order.add_edge(waiter_preps_nonalcoholic, waiter_readies_cart)
order.add_edge(waiter_readies_cart, waiter_delivers_order)
order.add_edge(waiter_delivers_order, choice_debit)
order.add_edge(choice_debit, waiter_returns_station)

# Create root
root = StrictPartialOrder(nodes=nodes, order=order)