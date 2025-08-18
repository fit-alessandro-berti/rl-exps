import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
receive_returns = Transition(label='Receive Returns')
inspect_items = Transition(label='Inspect Items')
segregate_stock = Transition(label='Segregate Stock')
wipe_data = Transition(label='Wipe Data')
harvest_parts = Transition(label='Harvest Parts')
refurbish_units = Transition(label='Refurbish Units')
test_quality = Transition(label='Test Quality')
recycle_waste = Transition(label='Recycle Waste')
dispose_defects = Transition(label='Dispose Defects')
update_inventory = Transition(label='Update Inventory')
coordinate_resale = Transition(label='Coordinate Resale')
process_refunds = Transition(label='Process Refunds')
analyze_patterns = Transition(label='Analyze Patterns')
improve_design = Transition(label='Improve Design')
report_metrics = Transition(label='Report Metrics')

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, dispose_defects])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[refurbish_units, update_inventory])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[coordinate_resale, process_refunds])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[analyze_patterns, improve_design, report_metrics])
root = StrictPartialOrder(nodes=[receive_returns, inspect_items, segregate_stock, wipe_data, harvest_parts, xor1, xor2, xor3, xor4])
root.order.add_edge(receive_returns, inspect_items)
root.order.add_edge(inspect_items, segregate_stock)
root.order.add_edge(segregate_stock, wipe_data)
root.order.add_edge(wipe_data, harvest_parts)
root.order.add_edge(harvest_parts, xor1)
root.order.add_edge(harvest_parts, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, report_metrics)

# Print the final result
print(root)