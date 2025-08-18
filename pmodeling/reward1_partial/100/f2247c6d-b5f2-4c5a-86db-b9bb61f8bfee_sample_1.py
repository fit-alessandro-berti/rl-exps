import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (e.g., for skipping certain steps)
skip_inspection = SilentTransition()
skip_segregation = SilentTransition()
skip_wipe_data = SilentTransition()
skip_harvest_parts = SilentTransition()
skip_refurbish_units = SilentTransition()
skip_test_quality = SilentTransition()
skip_recycle_waste = SilentTransition()
skip_dispose_defects = SilentTransition()
skip_update_inventory = SilentTransition()
skip_analyze_patterns = SilentTransition()
skip_improve_design = SilentTransition()
skip_report_metrics = SilentTransition()

# Define loops and exclusive choices
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[inspect_items, skip_inspection])
segregation_loop = OperatorPOWL(operator=Operator.LOOP, children=[segregate_stock, skip_segregation])
wipe_data_loop = OperatorPOWL(operator=Operator.LOOP, children=[wipe_data, skip_wipe_data])
harvest_parts_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_parts, skip_harvest_parts])
refurbish_units_loop = OperatorPOWL(operator=Operator.LOOP, children=[refurbish_units, skip_refurbish_units])
test_quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_quality, skip_test_quality])
recycle_waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[recycle_waste, skip_recycle_waste])
dispose_defects_loop = OperatorPOWL(operator=Operator.LOOP, children=[dispose_defects, skip_dispose_defects])
update_inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[update_inventory, skip_update_inventory])
analyze_patterns_loop = OperatorPOWL(operator=Operator.LOOP, children=[analyze_patterns, skip_analyze_patterns])
improve_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[improve_design, skip_improve_design])
report_metrics_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_metrics, skip_report_metrics])

# Define exclusive choices
exclusive_choice_inspection = OperatorPOWL(operator=Operator.XOR, children=[inspection_loop, skip_inspection])
exclusive_choice_segregation = OperatorPOWL(operator=Operator.XOR, children=[segregation_loop, skip_segregation])
exclusive_choice_wipe_data = OperatorPOWL(operator=Operator.XOR, children=[wipe_data_loop, skip_wipe_data])
exclusive_choice_harvest_parts = OperatorPOWL(operator=Operator.XOR, children=[harvest_parts_loop, skip_harvest_parts])
exclusive_choice_refurbish_units = OperatorPOWL(operator=Operator.XOR, children=[refurbish_units_loop, skip_refurbish_units])
exclusive_choice_test_quality = OperatorPOWL(operator=Operator.XOR, children=[test_quality_loop, skip_test_quality])
exclusive_choice_recycle_waste = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste_loop, skip_recycle_waste])
exclusive_choice_dispose_defects = OperatorPOWL(operator=Operator.XOR, children=[dispose_defects_loop, skip_dispose_defects])
exclusive_choice_update_inventory = OperatorPOWL(operator=Operator.XOR, children=[update_inventory_loop, skip_update_inventory])
exclusive_choice_analyze_patterns = OperatorPOWL(operator=Operator.XOR, children=[analyze_patterns_loop, skip_analyze_patterns])
exclusive_choice_improve_design = OperatorPOWL(operator=Operator.XOR, children=[improve_design_loop, skip_improve_design])
exclusive_choice_report_metrics = OperatorPOWL(operator=Operator.XOR, children=[report_metrics_loop, skip_report_metrics])

# Define the root node with all activities
root = StrictPartialOrder(nodes=[
    receive_returns,
    exclusive_choice_inspection,
    exclusive_choice_segregation,
    exclusive_choice_wipe_data,
    exclusive_choice_harvest_parts,
    exclusive_choice_refurbish_units,
    exclusive_choice_test_quality,
    exclusive_choice_recycle_waste,
    exclusive_choice_dispose_defects,
    exclusive_choice_update_inventory,
    exclusive_choice_analyze_patterns,
    exclusive_choice_improve_design,
    exclusive_choice_report_metrics
])

# Add dependencies between nodes (if any)
root.order.add_edge(receive_returns, exclusive_choice_inspection)
root.order.add_edge(receive_returns, exclusive_choice_segregation)
root.order.add_edge(receive_returns, exclusive_choice_wipe_data)
root.order.add_edge(receive_returns, exclusive_choice_harvest_parts)
root.order.add_edge(receive_returns, exclusive_choice_refurbish_units)
root.order.add_edge(receive_returns, exclusive_choice_test_quality)
root.order.add_edge(receive_returns, exclusive_choice_recycle_waste)
root.order.add_edge(receive_returns, exclusive_choice_dispose_defects)
root.order.add_edge(receive_returns, exclusive_choice_update_inventory)
root.order.add_edge(receive_returns, exclusive_choice_analyze_patterns)
root.order.add_edge(receive_returns, exclusive_choice_improve_design)
root.order.add_edge(receive_returns, exclusive_choice_report_metrics)

print(root)