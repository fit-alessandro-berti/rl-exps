import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for the repair/refurbishment process
repair_loop = OperatorPOWL(operator=Operator.LOOP, children=[refurbish_units, test_quality])

# Define the XOR for the data wiping and component harvesting
xor = OperatorPOWL(operator=Operator.XOR, children=[wipe_data, harvest_parts])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[receive_returns, inspect_items, segregate_stock, xor, repair_loop, update_inventory, coordinate_resale, process_refunds, analyze_patterns, improve_design, report_metrics])

# Add dependencies to the partial order
root.order.add_edge(receive_returns, inspect_items)
root.order.add_edge(inspect_items, segregate_stock)
root.order.add_edge(segregate_stock, xor)
root.order.add_edge(xor, repair_loop)
root.order.add_edge(repair_loop, update_inventory)
root.order.add_edge(update_inventory, coordinate_resale)
root.order.add_edge(coordinate_resale, process_refunds)
root.order.add_edge(process_refunds, analyze_patterns)
root.order.add_edge(analyze_patterns, improve_design)
root.order.add_edge(improve_design, report_metrics)

print(root)