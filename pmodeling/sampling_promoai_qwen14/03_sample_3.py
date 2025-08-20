import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_stock_storage = Transition(label='Place stock in storage')
place_stock_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
manual_alert = Transition(label='Send a manual alert')
automated_alert = Transition(label='Send an automated alert')
update_inventory_levels = Transition(label='Update inventory levels')
update_inventory_system = Transition(label='Update inventory system with expected delivery dates')

# Define silent transition for empty labels
skip = SilentTransition()

# Define operators for choice and loop
xor = OperatorPOWL(operator=Operator.XOR, children=[manual_alert, automated_alert])
loop = OperatorPOWL(operator=Operator.LOOP, children=[place_order, update_inventory_system])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[check_inventory, xor, loop, inspect_stock, receive_stock, record_stock, place_stock_storage, place_stock_shelves, update_inventory_levels])

# Define the partial order of activities
root.order.add_edge(check_inventory, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, inspect_stock)
root.order.add_edge(inspect_stock, receive_stock)
root.order.add_edge(receive_stock, record_stock)
root.order.add_edge(record_stock, place_stock_storage)
root.order.add_edge(place_stock_storage, place_stock_shelves)
root.order.add_edge(place_stock_shelves, update_inventory_levels)