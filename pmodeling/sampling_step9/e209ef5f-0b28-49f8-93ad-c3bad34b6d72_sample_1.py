import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SoilAnalyze = Transition(label='Soil Analyze')
SiteMap = Transition(label='Site Mapping')
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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SensorDeploy, IrrigationAdjust, NutrientFeed])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[PestScouting, PestPredict])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[WorkshopHost, CropRotate])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[CropSelect, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[YieldReport, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor1, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor1, xor2)

print(root)