import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    ReceiveReturns,
    InspectItems,
    SegregateStock,
    WipeData,
    HarvestParts,
    RefurbishUnits,
    TestQuality,
    RecycleWaste,
    DisposeDefects,
    UpdateInventory,
    CoordinateResale,
    ProcessRefunds,
    AnalyzePatterns,
    ImproveDesign,
    ReportMetrics
])

# Define the dependencies (partial order)
root.order.add_edge(ReceiveReturns, InspectItems)
root.order.add_edge(InspectItems, SegregateStock)
root.order.add_edge(SegregateStock, WipeData)
root.order.add_edge(WipeData, HarvestParts)
root.order.add_edge(HarvestParts, RefurbishUnits)
root.order.add_edge(RefurbishUnits, TestQuality)
root.order.add_edge(TestQuality, RecycleWaste)
root.order.add_edge(RecycleWaste, DisposeDefects)
root.order.add_edge(DisposeDefects, UpdateInventory)
root.order.add_edge(UpdateInventory, CoordinateResale)
root.order.add_edge(CoordinateResale, ProcessRefunds)
root.order.add_edge(ProcessRefunds, AnalyzePatterns)
root.order.add_edge(AnalyzePatterns, ImproveDesign)
root.order.add_edge(ImproveDesign, ReportMetrics)

print(root)