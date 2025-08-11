import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) based on the provided list
check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_stock_storage = Transition(label='Place stock in storage')
place_stock_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
manual_alert = Transition(label='Send a manual alert')
automated_alert = Transition(label='Send an automated alert')
update_inventory = Transition(label='Update inventory levels')
update_inventory_system = Transition(label='Update inventory system with expected delivery dates')

# Define the partial order structure
root = StrictPartialOrder(nodes=[check_inventory, inspect_stock, place_order, place_stock_storage, place_stock_shelves, receive_stock, record_stock, manual_alert, automated_alert, update_inventory, update_inventory_system])

# Define the dependencies between the transitions
root.order.add_edge(check_inventory, inspect_stock)
root.order.add_edge(inspect_stock, place_order)
root.order.add_edge(place_order, place_stock_storage)
root.order.add_edge(place_stock_storage, place_stock_shelves)
root.order.add_edge(place_stock_shelves, receive_stock)
root.order.add_edge(receive_stock, record_stock)
root.order.add_edge(record_stock, manual_alert)
root.order.add_edge(record_stock, automated_alert)
root.order.add_edge(manual_alert, update_inventory)
root.order.add_edge(automated_alert, update_inventory)
root.order.add_edge(update_inventory, update_inventory_system)

# Now 'root' contains the POWL model for the described process