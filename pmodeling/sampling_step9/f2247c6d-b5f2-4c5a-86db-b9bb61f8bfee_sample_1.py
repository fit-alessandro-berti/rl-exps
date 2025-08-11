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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[inspect_items, segregate_stock])
loop_refurbish = OperatorPOWL(operator=Operator.LOOP, children=[harvest_parts, refurbish_units])
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[test_quality, recycle_waste, dispose_defects])
loop_analyze = OperatorPOWL(operator=Operator.LOOP, children=[process_refunds, analyze_patterns])

xor_update = OperatorPOWL(operator=Operator.XOR, children=[update_inventory, skip])
xor_resale = OperatorPOWL(operator=Operator.XOR, children=[coordinate_resale, skip])
xor_design = OperatorPOWL(operator=Operator.XOR, children=[improve_design, skip])
xor_metrics = OperatorPOWL(operator=Operator.XOR, children=[report_metrics, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[receive_returns, loop_inspect, loop_refurbish, loop_test, loop_analyze, xor_update, xor_resale, xor_design, xor_metrics])
root.order.add_edge(receive_returns, loop_inspect)
root.order.add_edge(receive_returns, loop_refurbish)
root.order.add_edge(receive_returns, loop_test)
root.order.add_edge(receive_returns, loop_analyze)
root.order.add_edge(loop_inspect, xor_update)
root.order.add_edge(loop_refurbish, xor_resale)
root.order.add_edge(loop_test, xor_design)
root.order.add_edge(loop_analyze, xor_metrics)

# Save the root model in the variable 'root'