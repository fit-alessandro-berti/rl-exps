import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
guest_calls = Transition(label='Guest calls room service')
manager_takes_order = Transition(label='Manager takes down the order')
manager_submits_ticket = Transition(label='Manager submits order ticket to kitchen')
manager_assigns_order = Transition(label='Manager assigns order to waiter')
manager_gives_order = Transition(label='Manager gives order to sommelier')
kitchen_prepares_food = Transition(label='Kitchen prepares food')
sommelier_fetches_wine = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
waiter_prepares_nonalcoholic = Transition(label='Waiter prepares nonalcoholic drinks')
waiter_readies_cart = Transition(label='Waiter readies cart')
waiter_delivers_order = Transition(label='Waiter delivers order to guest\'s room')
waiter_debits_account = Transition(label='Waiter debits guest\'s account')
waiter_returns = Transition(label='Waiter returns to room-service station')
waiter_waits = Transition(label='Waiter waits/delays debiting')

# Define choices and loops
choice_alcohol = OperatorPOWL(operator=Operator.XOR, children=[sommelier_fetches_wine, SilentTransition()])
loop_waiter = OperatorPOWL(operator=Operator.LOOP, children=[waiter_prepares_nonalcoholic, waiter_readies_cart, waiter_delivers_order, waiter_debits_account, waiter_returns])

# Define the root
root = StrictPartialOrder(nodes=[guest_calls, manager_takes_order, manager_submits_ticket, manager_assigns_order, manager_gives_order, kitchen_prepares_food, choice_alcohol, loop_waiter])

# Define the order
root.order.add_edge(guest_calls, manager_takes_order)
root.order.add_edge(manager_takes_order, manager_submits_ticket)
root.order.add_edge(manager_takes_order, manager_assigns_order)
root.order.add_edge(manager_takes_order, manager_gives_order)
root.order.add_edge(manager_submits_ticket, kitchen_prepares_food)
root.order.add_edge(manager_gives_order, choice_alcohol)
root.order.add_edge(manager_assigns_order, loop_waiter)
root.order.add_edge(kitchen_prepares_food, loop_waiter)
root.order.add_edge(choice_alcohol, loop_waiter)
root.order.add_edge(waiter_delivers_order, waiter_debits_account)
root.order.add_edge(waiter_debits_account, waiter_returns)
root.order.add_edge(waiter_returns, waiter_waits)
root.order.add_edge(waiter_waits, waiter_prepares_nonalcoholic)

root