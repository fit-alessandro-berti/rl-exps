import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define activities
A_receive_returns = Transition(label='Receive Returns')
A_inspect_items = Transition(label='Inspect Items')
A_segregate_stock = Transition(label='Segregate Stock')
A_wipe_data = Transition(label='Wipe Data')
A_harvest_parts = Transition(label='Harvest Parts')
A_refurbish_units = Transition(label='Refurbish Units')
A_test_quality = Transition(label='Test Quality')
A_recycle_waste = Transition(label='Recycle Waste')
A_dispose_defects = Transition(label='Dispose Defects')
A_update_inventory = Transition(label='Update Inventory')
A_coordinate_resale = Transition(label='Coordinate Resale')
A_process_refunds = Transition(label='Process Refunds')
A_analyze_patterns = Transition(label='Analyze Patterns')
A_improve_design = Transition(label='Improve Design')
A_report_metrics = Transition(label='Report Metrics')

# Define silent activities
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[A_receive_returns, A_inspect_items, A_segregate_stock, A_wipe_data, A_harvest_parts, A_refurbish_units, A_test_quality, A_recycle_waste, A_dispose_defects, A_update_inventory])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[A_coordinate_resale, A_process_refunds, A_analyze_patterns, A_improve_design, A_report_metrics])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])

# Define root POWL
root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, xor2)

# Print the root POWL model
print(root)