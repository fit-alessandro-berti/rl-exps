import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
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

# Define the control-flow operators
xor_returning = OperatorPOWL(operator=Operator.XOR, children=[segregate_stock, wipe_data, harvest_parts])
xor_testing = OperatorPOWL(operator=Operator.XOR, children=[refurbish_units, test_quality])
xor_recycling = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, dispose_defects])
xor_processing = OperatorPOWL(operator=Operator.XOR, children=[update_inventory, coordinate_resale, process_refunds])
xor_analyzing = OperatorPOWL(operator=Operator.XOR, children=[analyze_patterns, improve_design, report_metrics])

# Define the partial order
root = StrictPartialOrder(nodes=[receive_returns, inspect_items, xor_returning, xor_testing, xor_recycling, xor_processing, xor_analyzing])
root.order.add_edge(receive_returns, inspect_items)
root.order.add_edge(inspect_items, xor_returning)
root.order.add_edge(inspect_items, xor_testing)
root.order.add_edge(inspect_items, xor_recycling)
root.order.add_edge(inspect_items, xor_processing)
root.order.add_edge(inspect_items, xor_analyzing)

# Print the root of the POWL model
print(root)