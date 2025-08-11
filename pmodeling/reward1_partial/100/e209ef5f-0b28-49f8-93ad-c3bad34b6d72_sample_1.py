from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define silent transitions (no labels)
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[SoilAnalyze, SiteMapping, BedSetup, CropSelect, SensorDeploy, IrrigationAdjust, NutrientFeed, PestScouting, PestPredict, WorkshopHost, CropRotate, WasteCompost, WaterRecycle, DataAnalyze, CycleRefine, ResourceShare, YieldReport])

# Define the partial order
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, YieldReport)