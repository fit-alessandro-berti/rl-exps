import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

receive_inspect = OperatorPOWL(operator=Operator.XOR, children=[receive_returns, inspect_items])
inspect_segregate = OperatorPOWL(operator=Operator.XOR, children=[inspect_items, segregate_stock])
segregate_wipe = OperatorPOWL(operator=Operator.XOR, children=[segregate_stock, wipe_data])
wipe_harvest = OperatorPOWL(operator=Operator.XOR, children=[wipe_data, harvest_parts])
harvest_refurbish = OperatorPOWL(operator=Operator.XOR, children=[harvest_parts, refurbish_units])
refurbish_test = OperatorPOWL(operator=Operator.XOR, children=[refurbish_units, test_quality])
test_recycle = OperatorPOWL(operator=Operator.XOR, children=[test_quality, recycle_waste])
recycle_dispose = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, dispose_defects])
dispose_update = OperatorPOWL(operator=Operator.XOR, children=[dispose_defects, update_inventory])
update_resale = OperatorPOWL(operator=Operator.XOR, children=[update_inventory, coordinate_resale])
resale_refunds = OperatorPOWL(operator=Operator.XOR, children=[coordinate_resale, process_refunds])
refunds_analyze = OperatorPOWL(operator=Operator.XOR, children=[process_refunds, analyze_patterns])
analyze_improve = OperatorPOWL(operator=Operator.XOR, children=[analyze_patterns, improve_design])
improve_report = OperatorPOWL(operator=Operator.XOR, children=[improve_design, report_metrics])

root = StrictPartialOrder(nodes=[
    receive_inspect,
    inspect_segregate,
    segregate_wipe,
    wipe_harvest,
    harvest_refurbish,
    refurbish_test,
    test_recycle,
    recycle_dispose,
    dispose_update,
    update_resale,
    resale_refunds,
    refunds_analyze,
    analyze_improve,
    improve_report
])

root.order.add_edge(receive_inspect, inspect_segregate)
root.order.add_edge(inspect_segregate, segregate_wipe)
root.order.add_edge(segregate_wipe, wipe_harvest)
root.order.add_edge(wipe_harvest, harvest_refurbish)
root.order.add_edge(harvest_refurbish, refurbish_test)
root.order.add_edge(refurbish_test, test_recycle)
root.order.add_edge(test_recycle, recycle_dispose)
root.order.add_edge(recycle_dispose, dispose_update)
root.order.add_edge(dispose_update, update_resale)
root.order.add_edge(update_resale, resale_refunds)
root.order.add_edge(resale_refunds, refunds_analyze)
root.order.add_edge(refunds_analyze, analyze_improve)
root.order.add_edge(analyze_improve, improve_report)

print(root)