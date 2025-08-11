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
PestScout = Transition(label='Pest Scouting')
PestPredict = Transition(label='Pest Predict')
WorkshopHost = Transition(label='Workshop Host')
CropRotate = Transition(label='Crop Rotate')
WasteCompost = Transition(label='Waste Compost')
WaterRecycle = Transition(label='Water Recycle')
DataAnalyze = Transition(label='Data Analyze')
CycleRefine = Transition(label='Cycle Refine')
ResourceShare = Transition(label='Resource Share')
YieldReport = Transition(label='Yield Report')

# Initialize silent transitions for loop and choice
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[CropSelect, SensorDeploy, IrrigationAdjust, NutrientFeed, PestScout, PestPredict, CropRotate, WasteCompost, WaterRecycle, DataAnalyze, CycleRefine, ResourceShare, YieldReport])
xor = OperatorPOWL(operator=Operator.XOR, children=[WorkshopHost, loop])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)