import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
check_current_inventory_level = Transition(label='Check current inventory level')
inspect_stock_for_quality = Transition(label='Inspect stock for quality')
place_order_with_suppliers = Transition(label='Place order with suppliers')
place_stock_in_storage = Transition(label='Place stock in storage')
place_stock_on_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock_in_system = Transition(label='Record stock in system')
send_a_manual_alert = Transition(label='Send a manual alert')
send_an_automated_alert = Transition(label='Send an automated alert')
update_inventory_levels = Transition(label='Update inventory levels')
update_inventory_system_with_expected_delivery_dates = Transition(label='Update inventory system with expected delivery dates')

# Define the silent transitions
skip = SilentTransition()

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[check_current_inventory_level, place_order_with_suppliers])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[send_a_manual_alert, send_an_automated_alert])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add edges between nodes
root.order.add_edge(check_current_inventory_level, place_order_with_suppliers)
root.order.add_edge(place_order_with_suppliers, receive_stock)
root.order.add_edge(receive_stock, inspect_stock_for_quality)
root.order.add_edge(inspect_stock_for_quality, place_stock_in_storage)
root.order.add_edge(place_stock_in_storage, place_stock_on_shelves)
root.order.add_edge(place_stock_on_shelves, record_stock_in_system)
root.order.add_edge(record_stock_in_system, update_inventory_system_with_expected_delivery_dates)
root.order.add_edge(update_inventory_system_with_expected_delivery_dates, update_inventory_levels)