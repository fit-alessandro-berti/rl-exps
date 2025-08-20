import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
update_system = Transition(label='Update inventory system with expected delivery dates')

# Define choices
alert_choice = OperatorPOWL(operator=Operator.XOR, children=[manual_alert, automated_alert])

# Define loops
reorder_loop = OperatorPOWL(operator=Operator.LOOP, children=[place_order, update_system])

# Define partial orders
initial_order = StrictPartialOrder(nodes=[check_inventory, alert_choice])
reorder_order = StrictPartialOrder(nodes=[place_storage, place_shelves, receive_stock, record_stock, reorder_loop])
final_order = StrictPartialOrder(nodes=[update_levels])

# Connect partial orders
initial_order.order.add_edge(check_inventory, alert_choice)
reorder_order.order.add_edge(place_storage, place_shelves)
reorder_order.order.add_edge(place_shelves, receive_stock)
reorder_order.order.add_edge(receive_stock, record_stock)
reorder_order.order.add_edge(record_stock, reorder_loop)
final_order.order.add_edge(update_levels)

# Define root
root = StrictPartialOrder(nodes=[initial_order, reorder_order, final_order])
root.order.add_edge(initial_order, reorder_order)
root.order.add_edge(reorder_order, final_order)