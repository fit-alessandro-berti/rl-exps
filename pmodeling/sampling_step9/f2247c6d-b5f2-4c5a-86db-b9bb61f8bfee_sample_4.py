import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[HarvestParts, RefurbishUnits, TestQuality, RecycleWaste, DisposeDefects])
xor = OperatorPOWL(operator=Operator.XOR, children=[UpdateInventory, ProcessRefunds])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[AnalyzePatterns, ImproveDesign])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ReportMetrics])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)