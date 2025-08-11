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

# Define silent transitions
skip = SilentTransition()

# Define the loops and exclusive choices
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[inspect_items, segregate_stock, wipe_data, harvest_parts, refurbish_units, test_quality, recycle_waste, dispose_defects, update_inventory, coordinate_resale, process_refunds, analyze_patterns, improve_design, report_metrics])
xor_analyze = OperatorPOWL(operator=Operator.XOR, children=[analyze_patterns, improve_design, report_metrics])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop_inspect, xor_analyze])
root.order.add_edge(loop_inspect, xor_analyze)

# Print the root POWL model
print(root)