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

# Define the partial order
root = StrictPartialOrder(nodes=[
    receive_returns,
    inspect_items,
    segregate_stock,
    wipe_data,
    harvest_parts,
    refurbish_units,
    test_quality,
    recycle_waste,
    dispose_defects,
    update_inventory,
    coordinate_resale,
    process_refunds,
    analyze_patterns,
    improve_design,
    report_metrics
])
# No dependencies specified in the problem description, so we assume concurrent execution
# if there were dependencies, we would add edges to the 'root.order' as shown in the example code