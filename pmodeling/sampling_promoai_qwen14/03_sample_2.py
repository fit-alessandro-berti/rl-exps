import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
update_delivery_dates = Transition(label='Update inventory system with expected delivery dates')

# Define operators
check_stock = OperatorPOWL(operator=Operator.XOR, children=[check_inventory, automated_alert, manual_alert])
inspect_and_place = OperatorPOWL(operator=Operator.SEQUENCE, children=[inspect_stock, place_order])
place_stock = OperatorPOWL(operator=Operator.XOR, children=[place_stock_storage, place_stock_shelves])
receive_and_record = OperatorPOWL(operator=Operator.SEQUENCE, children=[receive_stock, record_stock])
update_inventory_final = OperatorPOWL(operator=Operator.SEQUENCE, children=[update_inventory, update_delivery_dates])

# Define the main POWL model
root = StrictPartialOrder(nodes=[check_stock, inspect_and_place, place_stock, receive_and_record, update_inventory_final])

# Define the order of transitions
root.order.add_edge(check_stock, inspect_and_place)
root.order.add_edge(inspect_and_place, place_stock)
root.order.add_edge(place_stock, receive_and_record)
root.order.add_edge(receive_and_record, update_inventory_final)

# Add the silent transition for the automated alert
silent_transition = SilentTransition()
root.nodes.append(silent_transition)
root.order.add_edge(automated_alert, silent_transition)
root.order.add_edge(silent_transition, inspect_and_place)

# Add the silent transition for the manual alert
silent_transition_manual = SilentTransition()
root.nodes.append(silent_transition_manual)
root.order.add_edge(manual_alert, silent_transition_manual)
root.order.add_edge(silent_transition_manual, inspect_and_place)

print(root)