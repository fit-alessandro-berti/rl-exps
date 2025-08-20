import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_storage = Transition(label='Place stock in storage')
place_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
manual_alert = Transition(label='Send a manual alert')
automated_alert = Transition(label='Send an automated alert')
update_inventory = Transition(label='Update inventory levels')
update_delivery = Transition(label='Update inventory system with expected delivery dates')

# Define silent transitions
skip = SilentTransition()

# Define the loop for ordering and receiving stock
loop_order = OperatorPOWL(operator=Operator.LOOP, children=[place_order, receive_stock, inspect_stock, record_stock, update_inventory])

# Define the choice between manual and automated alert
xor_alert = OperatorPOWL(operator=Operator.XOR, children=[manual_alert, automated_alert])

# Define the root POWL model
root = StrictPartialOrder(nodes=[check_inventory, loop_order, xor_alert, update_delivery, place_storage, place_shelves])
root.order.add_edge(check_inventory, loop_order)
root.order.add_edge(loop_order, xor_alert)
root.order.add_edge(xor_alert, update_delivery)
root.order.add_edge(update_delivery, place_storage)
root.order.add_edge(place_storage, place_shelves)