import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define partial order
root = StrictPartialOrder(nodes=[
    SoilAnalyze, SiteMapping, BedSetup, CropSelect, SensorDeploy,
    IrrigationAdjust, NutrientFeed, PestScouting, PestPredict,
    WorkshopHost, CropRotate, WasteCompost, WaterRecycle,
    DataAnalyze, CycleRefine, ResourceShare, YieldReport
])

# Define dependencies
root.order.add_edge(SoilAnalyze, SiteMapping)
root.order.add_edge(SiteMapping, BedSetup)
root.order.add_edge(BedSetup, CropSelect)
root.order.add_edge(CropSelect, SensorDeploy)
root.order.add_edge(SensorDeploy, IrrigationAdjust)
root.order.add_edge(IrrigationAdjust, NutrientFeed)
root.order.add_edge(NutrientFeed, PestScouting)
root.order.add_edge(PestScouting, PestPredict)
root.order.add_edge(PestPredict, WorkshopHost)
root.order.add_edge(WorkshopHost, CropRotate)
root.order.add_edge(CropRotate, WasteCompost)
root.order.add_edge(WasteCompost, WaterRecycle)
root.order.add_edge(WaterRecycle, DataAnalyze)
root.order.add_edge(DataAnalyze, CycleRefine)
root.order.add_edge(CycleRefine, ResourceShare)
root.order.add_edge(ResourceShare, YieldReport)

print(root)