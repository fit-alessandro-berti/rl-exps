import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
check_inventory = Transition(label='Check current inventory level')
send_alert = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Send an automated alert'), Transition(label='Send a manual alert')])
reorder_stock = Transition(label='Place order with suppliers')
update_expected_delivery = Transition(label='Update inventory system with expected delivery dates')
receive_stock = Transition(label='Receive stock')
inspect_stock = Transition(label='Inspect stock for quality')
record_stock = Transition(label='Record stock in system')
place_shelves = Transition(label='Place stock on shelves')
place_storage = Transition(label='Place stock in storage')
update_levels = Transition(label='Update inventory levels')

# Define the POWL model
root = StrictPartialOrder(nodes=[check_inventory, send_alert, reorder_stock, update_expected_delivery, receive_stock, inspect_stock, record_stock, place_shelves, place_storage, update_levels])

# Define the partial order
root.order.add_edge(check_inventory, send_alert)
root.order.add_edge(send_alert, reorder_stock)
root.order.add_edge(reorder_stock, update_expected_delivery)
root.order.add_edge(update_expected_delivery, receive_stock)
root.order.add_edge(receive_stock, inspect_stock)
root.order.add_edge(inspect_stock, record_stock)
root.order.add_edge(record_stock, place_shelves)
root.order.add_edge(place_shelves, update_levels)
root.order.add_edge(record_stock, place_storage)
root.order.add_edge(place_storage, update_levels)