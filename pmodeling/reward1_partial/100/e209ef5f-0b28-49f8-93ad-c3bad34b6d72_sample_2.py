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

# Define silent transitions
Skip1 = SilentTransition()
Skip2 = SilentTransition()
Skip3 = SilentTransition()

# Define loops
SoilSiteMappingLoop = OperatorPOWL(operator=Operator.LOOP, children=[SoilAnalyze, SiteMapping])
BedCropSetupLoop = OperatorPOWL(operator=Operator.LOOP, children=[BedSetup, CropSelect])

# Define XORs
SensorDeployXOR = OperatorPOWL(operator=Operator.XOR, children=[SensorDeploy, Skip1])
PestScoutingXOR = OperatorPOWL(operator=Operator.XOR, children=[PestScouting, Skip2])
PestPredictXOR = OperatorPOWL(operator=Operator.XOR, children=[PestPredict, Skip3])
WorkshopHostXOR = OperatorPOWL(operator=Operator.XOR, children=[WorkshopHost, Skip1])

# Define the root POWL model
root = StrictPartialOrder(
    nodes=[
        SoilSiteMappingLoop,
        BedCropSetupLoop,
        SensorDeployXOR,
        PestScoutingXOR,
        PestPredictXOR,
        WorkshopHostXOR,
        CropRotate,
        WasteCompost,
        WaterRecycle,
        DataAnalyze,
        CycleRefine,
        ResourceShare,
        YieldReport
    ]
)

# Define dependencies
root.order.add_edge(SoilSiteMappingLoop, BedCropSetupLoop)
root.order.add_edge(BedCropSetupLoop, SensorDeployXOR)
root.order.add_edge(SensorDeployXOR, PestScoutingXOR)
root.order.add_edge(PestScoutingXOR, PestPredictXOR)
root.order.add_edge(PestPredictXOR, WorkshopHostXOR)
root.order.add_edge(WorkshopHostXOR, CropRotate)
root.order.add_edge(CropRotate, WasteCompost)
root.order.add_edge(WasteCompost, WaterRecycle)
root.order.add_edge(WaterRecycle, DataAnalyze)
root.order.add_edge(DataAnalyze, CycleRefine)
root.order.add_edge(CycleRefine, ResourceShare)
root.order.add_edge(ResourceShare, YieldReport)

# Print the root POWL model
print(root)