import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_stock_storage = Transition(label='Place stock in storage')
place_stock_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
send_manual_alert = Transition(label='Send a manual alert')
send_automated_alert = Transition(label='Send an automated alert')
update_inventory_levels = Transition(label='Update inventory levels')
update_inventory_dates = Transition(label='Update inventory system with expected delivery dates')

# Define the partial order
root = StrictPartialOrder(nodes=[check_inventory, send_manual_alert, send_automated_alert, place_order, update_inventory_dates, receive_stock, inspect_stock, record_stock, place_stock_storage, place_stock_shelves, update_inventory_levels])
root.order.add_edge(check_inventory, send_manual_alert)
root.order.add_edge(check_inventory, send_automated_alert)
root.order.add_edge(send_manual_alert, place_order)
root.order.add_edge(send_automated_alert, place_order)
root.order.add_edge(place_order, update_inventory_dates)
root.order.add_edge(update_inventory_dates, receive_stock)
root.order.add_edge(receive_stock, inspect_stock)
root.order.add_edge(inspect_stock, record_stock)
root.order.add_edge(record_stock, place_stock_storage)
root.order.add_edge(place_stock_storage, place_stock_shelves)
root.order.add_edge(place_stock_shelves, update_inventory_levels)