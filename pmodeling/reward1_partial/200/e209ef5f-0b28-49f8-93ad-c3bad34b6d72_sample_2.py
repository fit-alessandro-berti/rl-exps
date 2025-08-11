import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SoilAnalyze = Transition(label='Soil Analyze')
SiteMapping = Transition(label='Site Mapping')
BedSetup = Transition(label='Bed Setup')
CropSelect = Transition(label='Crop Select')
SensorDeploy = Transition(label='Sensor Deploy')
IrrigationAdjust = Transition(label='Irrigation Adjust')
NutrientFeed = Transition(label='Nutrient Feed')
PestScouting = Transition(label='Pest Scouting')
PestPredict = Transition(label='Pest Predict')
WorkshopHost = Transition(label='Workshop Host')
CropRotate = Transition(label='Crop Rotate')
WasteCompost = Transition(label='Waste Compost')
WaterRecycle = Transition(label='Water Recycle')
DataAnalyze = Transition(label='Data Analyze')
CycleRefine = Transition(label='Cycle Refine')
ResourceShare = Transition(label='Resource Share')
YieldReport = Transition(label='Yield Report')

# Define silent transition
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SensorDeploy, IrrigationAdjust, NutrientFeed, PestScouting, PestPredict])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CropRotate, WasteCompost, WaterRecycle])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, WorkshopHost])

# Define the root node with all the nodes and their dependencies
root = StrictPartialOrder(nodes=[SoilAnalyze, SiteMapping, BedSetup, CropSelect, loop1, loop2, xor])
root.order.add_edge(SoilAnalyze, SiteMapping)
root.order.add_edge(SoilAnalyze, BedSetup)
root.order.add_edge(SiteMapping, BedSetup)
root.order.add_edge(BedSetup, CropSelect)
root.order.add_edge(CropSelect, loop1)
root.order.add_edge(loop1, SensorDeploy)
root.order.add_edge(loop1, IrrigationAdjust)
root.order.add_edge(loop1, NutrientFeed)
root.order.add_edge(loop1, PestScouting)
root.order.add_edge(loop1, PestPredict)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, CropRotate)
root.order.add_edge(loop2, WasteCompost)
root.order.add_edge(loop2, WaterRecycle)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, WorkshopHost)
root.order.add_edge(xor, CropRotate)
root.order.add_edge(xor, WasteCompost)
root.order.add_edge(xor, WaterRecycle)
root.order.add_edge(xor, DataAnalyze)
root.order.add_edge(xor, CycleRefine)
root.order.add_edge(xor, ResourceShare)
root.order.add_edge(xor, YieldReport)