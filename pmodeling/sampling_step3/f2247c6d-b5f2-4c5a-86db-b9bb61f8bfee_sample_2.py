from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order
root = StrictPartialOrder(nodes=[receive_returns, inspect_items, segregate_stock, wipe_data, harvest_parts, refurbish_units, test_quality, recycle_waste, dispose_defects, update_inventory, coordinate_resale, process_refunds, analyze_patterns, improve_design, report_metrics])

# Define the dependencies between the nodes
root.order.add_edge(receive_returns, inspect_items)
root.order.add_edge(inspect_items, segregate_stock)
root.order.add_edge(segregate_stock, wipe_data)
root.order.add_edge(wipe_data, harvest_parts)
root.order.add_edge(harvest_parts, refurbish_units)
root.order.add_edge(refurbish_units, test_quality)
root.order.add_edge(test_quality, recycle_waste)
root.order.add_edge(recycle_waste, dispose_defects)
root.order.add_edge(dispose_defects, update_inventory)
root.order.add_edge(update_inventory, coordinate_resale)
root.order.add_edge(coordinate_resale, process_refunds)
root.order.add_edge(process_refunds, analyze_patterns)
root.order.add_edge(analyze_patterns, improve_design)
root.order.add_edge(improve_design, report_metrics)

print(root)