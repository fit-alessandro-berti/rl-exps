import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ReceiveReturns = Transition(label='Receive Returns')
InspectItems = Transition(label='Inspect Items')
SegregateStock = Transition(label='Segregate Stock')
WipeData = Transition(label='Wipe Data')
HarvestParts = Transition(label='Harvest Parts')
RefurbishUnits = Transition(label='Refurbish Units')
TestQuality = Transition(label='Test Quality')
RecycleWaste = Transition(label='Recycle Waste')
DisposeDefects = Transition(label='Dispose Defects')
UpdateInventory = Transition(label='Update Inventory')
CoordinateResale = Transition(label='Coordinate Resale')
ProcessRefunds = Transition(label='Process Refunds')
AnalyzePatterns = Transition(label='Analyze Patterns')
ImproveDesign = Transition(label='Improve Design')
ReportMetrics = Transition(label='Report Metrics')

# Define silent transitions
skip = SilentTransition()

# Define POWL models
loop_receive_inspect = OperatorPOWL(operator=Operator.LOOP, children=[ReceiveReturns, InspectItems])
loop_segregate_wipe = OperatorPOWL(operator=Operator.LOOP, children=[SegregateStock, WipeData])
loop_harvest_refurbish = OperatorPOWL(operator=Operator.LOOP, children=[HarvestParts, RefurbishUnits])
loop_test_recycle = OperatorPOWL(operator=Operator.LOOP, children=[TestQuality, RecycleWaste])
loop_defect_dispose = OperatorPOWL(operator=Operator.LOOP, children=[DisposeDefects, skip])
loop_inventory_resale = OperatorPOWL(operator=Operator.LOOP, children=[UpdateInventory, CoordinateResale])
loop_refunds_analyze = OperatorPOWL(operator=Operator.LOOP, children=[ProcessRefunds, AnalyzePatterns])
loop_design_metrics = OperatorPOWL(operator=Operator.LOOP, children=[ImproveDesign, ReportMetrics])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_receive_inspect,
    loop_segregate_wipe,
    loop_harvest_refurbish,
    loop_test_recycle,
    loop_defect_dispose,
    loop_inventory_resale,
    loop_refunds_analyze,
    loop_design_metrics
])

# Add dependencies between the loops
root.order.add_edge(loop_receive_inspect, loop_segregate_wipe)
root.order.add_edge(loop_segregate_wipe, loop_harvest_refurbish)
root.order.add_edge(loop_harvest_refurbish, loop_test_recycle)
root.order.add_edge(loop_test_recycle, loop_defect_dispose)
root.order.add_edge(loop_defect_dispose, loop_inventory_resale)
root.order.add_edge(loop_inventory_resale, loop_refunds_analyze)
root.order.add_edge(loop_refunds_analyze, loop_design_metrics)

print(root)