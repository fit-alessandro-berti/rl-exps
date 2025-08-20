import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_in_storage = Transition(label='Place stock in storage')
place_on_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
manual_alert = Transition(label='Send a manual alert')
automated_alert = Transition(label='Send an automated alert')
update_levels = Transition(label='Update inventory levels')
update_delivery_dates = Transition(label='Update inventory system with expected delivery dates')

# Define silent transition for choice between manual and automated alert
skip = SilentTransition()

# Define choice between manual and automated alert
alert_choice = OperatorPOWL(operator=Operator.XOR, children=[manual_alert, automated_alert])

# Define loop for monitoring inventory levels
monitor_inventory = OperatorPOWL(operator=Operator.LOOP, children=[check_inventory, alert_choice])

# Define choice between placing stock in storage or on shelves
storage_choice = OperatorPOWL(operator=Operator.XOR, children=[place_in_storage, place_on_shelves])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[monitor_inventory, place_order, receive_stock, record_stock, storage_choice, update_levels, update_delivery_dates])
root.order.add_edge(monitor_inventory, place_order)
root.order.add_edge(place_order, receive_stock)
root.order.add_edge(receive_stock, record_stock)
root.order.add_edge(record_stock, storage_choice)
root.order.add_edge(storage_choice, update_levels)
root.order.add_edge(place_order, update_delivery_dates)