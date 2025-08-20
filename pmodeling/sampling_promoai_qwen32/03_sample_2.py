import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_storage = Transition(label='Place stock in storage')
place_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
manual_alert = Transition(label='Send a manual alert')
automated_alert = Transition(label='Send an automated alert')
update_levels = Transition(label='Update inventory levels')
update_expected = Transition(label='Update inventory system with expected delivery dates')

# Define control flow
loop = OperatorPOWL(operator=Operator.LOOP, children=[check_inventory])
choice_alert = OperatorPOWL(operator=Operator.XOR, children=[manual_alert, automated_alert])
choice_placement = OperatorPOWL(operator=Operator.XOR, children=[place_storage, place_shelves])

# Define partial order
root = StrictPartialOrder(nodes=[loop, choice_alert, place_order, update_expected, receive_stock, inspect_stock, record_stock, choice_placement, update_levels])
root.order.add_edge(loop, choice_alert)
root.order.add_edge(choice_alert, place_order)
root.order.add_edge(place_order, update_expected)
root.order.add_edge(update_expected, receive_stock)
root.order.add_edge(receive_stock, inspect_stock)
root.order.add_edge(inspect_stock, record_stock)
root.order.add_edge(record_stock, choice_placement)
root.order.add_edge(choice_placement, update_levels)