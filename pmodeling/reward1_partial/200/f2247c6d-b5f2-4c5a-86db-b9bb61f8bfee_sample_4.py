from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip_inspection = SilentTransition()
skip_wipe_data = SilentTransition()
skip_harvest_parts = SilentTransition()
skip_refurbish_units = SilentTransition()
skip_test_quality = SilentTransition()

# Define the loop nodes
defective_parts_loop = OperatorPOWL(operator=Operator.LOOP, children=[recycle_waste, dispose_defects])
refurbish_units_loop = OperatorPOWL(operator=Operator.LOOP, children=[refurbish_units, skip_refurbish_units])
test_quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_quality, skip_test_quality])

# Define the partial order
root = StrictPartialOrder(nodes=[receive_returns, inspect_items, segregate_stock, wipe_data, harvest_parts, refurbish_units_loop, test_quality_loop, defective_parts_loop, update_inventory, coordinate_resale, process_refunds, analyze_patterns, improve_design, report_metrics])
root.order.add_edge(receive_returns, inspect_items)
root.order.add_edge(inspect_items, segregate_stock)
root.order.add_edge(segregate_stock, wipe_data)
root.order.add_edge(wipe_data, harvest_parts)
root.order.add_edge(harvest_parts, refurbish_units_loop)
root.order.add_edge(refurbish_units_loop, test_quality_loop)
root.order.add_edge(test_quality_loop, defective_parts_loop)
root.order.add_edge(defective_parts_loop, update_inventory)
root.order.add_edge(update_inventory, coordinate_resale)
root.order.add_edge(coordinate_resale, process_refunds)
root.order.add_edge(process_refunds, analyze_patterns)
root.order.add_edge(analyze_patterns, improve_design)
root.order.add_edge(improve_design, report_metrics)

# Add silent transitions if necessary
root.order.add_edge(inspect_items, skip_inspection)
root.order.add_edge(wipe_data, skip_wipe_data)
root.order.add_edge(harvest_parts, skip_harvest_parts)
root.order.add_edge(refurbish_units, skip_refurbish_units)
root.order.add_edge(test_quality, skip_test_quality)

# Print the final POWL model
print(root)