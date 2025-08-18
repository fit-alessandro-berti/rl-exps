import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Create exclusive choice for repair or refurbishment
xor = OperatorPOWL(operator=Operator.XOR, children=[refurbish_units, update_inventory])

# Create loop for quality testing and repackaging
loop = OperatorPOWL(operator=Operator.LOOP, children=[test_quality, coordinate_resale])

# Create the root partial order
root = StrictPartialOrder(nodes=[receive_returns, inspect_items, segregate_stock, wipe_data, harvest_parts, xor, loop, process_refunds, analyze_patterns, improve_design, report_metrics])

# Add dependencies to the partial order
root.order.add_edge(receive_returns, inspect_items)
root.order.add_edge(inspect_items, segregate_stock)
root.order.add_edge(segregate_stock, wipe_data)
root.order.add_edge(wipe_data, harvest_parts)
root.order.add_edge(harvest_parts, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, process_refunds)
root.order.add_edge(process_refunds, analyze_patterns)
root.order.add_edge(analyze_patterns, improve_design)
root.order.add_edge(improve_design, report_metrics)