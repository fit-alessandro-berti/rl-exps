from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
SiteSurvey = Transition(label='Site Survey')
StructureCheck = Transition(label='Structure Check')
SoilSample = Transition(label='Soil Sample')
WaterTest = Transition(label='Water Test')
CropSelection = Transition(label='Crop Selection')
MaterialOrder = Transition(label='Material Order')
PlanterSetup = Transition(label='Planter Setup')
IrrigationInstall = Transition(label='Irrigation Install')
SensorDeploy = Transition(label='Sensor Deploy')
SolarSetup = Transition(label='Solar Setup')
DataIntegration = Transition(label='Data Integration')
CommunityMeet = Transition(label='Community Meet')
TrainingSession = Transition(label='Training Session')
YieldMonitor = Transition(label='Yield Monitor')
AdjustPlan = Transition(label='Adjust Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[SiteSurvey, StructureCheck, SoilSample, WaterTest, CropSelection, MaterialOrder, PlanterSetup, IrrigationInstall, SensorDeploy, SolarSetup, DataIntegration, CommunityMeet, TrainingSession, YieldMonitor, AdjustPlan])

# Define the dependencies (order)
root.order.add_edge(SiteSurvey, StructureCheck)
root.order.add_edge(StructureCheck, SoilSample)
root.order.add_edge(SoilSample, WaterTest)
root.order.add_edge(WaterTest, CropSelection)
root.order.add_edge(CropSelection, MaterialOrder)
root.order.add_edge(MaterialOrder, PlanterSetup)
root.order.add_edge(PlanterSetup, IrrigationInstall)
root.order.add_edge(IrrigationInstall, SensorDeploy)
root.order.add_edge(SensorDeploy, SolarSetup)
root.order.add_edge(SolarSetup, DataIntegration)
root.order.add_edge(DataIntegration, CommunityMeet)
root.order.add_edge(CommunityMeet, TrainingSession)
root.order.add_edge(TrainingSession, YieldMonitor)
root.order.add_edge(YieldMonitor, AdjustPlan)

# Print the root to verify
print(root)