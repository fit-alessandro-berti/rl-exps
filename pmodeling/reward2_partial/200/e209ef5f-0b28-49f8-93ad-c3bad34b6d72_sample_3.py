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

root = StrictPartialOrder(nodes=[
    SoilAnalyze,
    SiteMap,
    BedSetup,
    CropSelect,
    SensorDeploy,
    IrrigationAdjust,
    NutrientFeed,
    PestScout,
    PestPredict,
    WorkshopHost,
    CropRotate,
    WasteCompost,
    WaterRecycle,
    DataAnalyze,
    CycleRefine,
    ResourceShare,
    YieldReport
])

root.order.add_edge(SoilAnalyze, SiteMap)
root.order.add_edge(SoilAnalyze, BedSetup)
root.order.add_edge(SiteMap, CropSelect)
root.order.add_edge(BedSetup, SensorDeploy)
root.order.add_edge(SensorDeploy, IrrigationAdjust)
root.order.add_edge(SensorDeploy, NutrientFeed)
root.order.add_edge(IrrigationAdjust, PestScout)
root.order.add_edge(IrrigationAdjust, PestPredict)
root.order.add_edge(PestScout, WorkshopHost)
root.order.add_edge(PestPredict, CropRotate)
root.order.add_edge(CropRotate, WasteCompost)
root.order.add_edge(CropRotate, WaterRecycle)
root.order.add_edge(WasteCompost, DataAnalyze)
root.order.add_edge(WaterRecycle, DataAnalyze)
root.order.add_edge(DataAnalyze, CycleRefine)
root.order.add_edge(CycleRefine, ResourceShare)
root.order.add_edge(ResourceShare, YieldReport)