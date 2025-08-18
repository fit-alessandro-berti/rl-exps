import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
LoadAssess = Transition(label='Load Assess')
PermitReview = Transition(label='Permit Review')
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SoilMix = Transition(label='Soil Mix')
InstallBeds = Transition(label='Install Beds')
IrrigationSet = Transition(label='Irrigation Set')
ClimateTest = Transition(label='Climate Test')
SensorDeploy = Transition(label='Sensor Deploy')
EnergySetup = Transition(label='Energy Setup')
CropSelect = Transition(label='Crop Select')
PlantSeeding = Transition(label='Plant Seeding')
CommunityMeet = Transition(label='Community Meet')
ComplianceCheck = Transition(label='Compliance Check')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestPlan = Transition(label='Harvest Plan')
WasteRecycle = Transition(label='Waste Recycle')

root = StrictPartialOrder(nodes=[LoadAssess, PermitReview, SiteSurvey, DesignLayout, SoilMix, InstallBeds, IrrigationSet, ClimateTest, SensorDeploy, EnergySetup, CropSelect, PlantSeeding, CommunityMeet, ComplianceCheck, GrowthMonitor, HarvestPlan, WasteRecycle])

# Define the dependencies between the activities
root.order.add_edge(LoadAssess, PermitReview)
root.order.add_edge(PermitReview, SiteSurvey)
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, SoilMix)
root.order.add_edge(SoilMix, InstallBeds)
root.order.add_edge(InstallBeds, IrrigationSet)
root.order.add_edge(IrrigationSet, ClimateTest)
root.order.add_edge(ClimateTest, SensorDeploy)
root.order.add_edge(SensorDeploy, EnergySetup)
root.order.add_edge(EnergySetup, CropSelect)
root.order.add_edge(CropSelect, PlantSeeding)
root.order.add_edge(PlantSeeding, CommunityMeet)
root.order.add_edge(CommunityMeet, ComplianceCheck)
root.order.add_edge(ComplianceCheck, GrowthMonitor)
root.order.add_edge(GrowthMonitor, HarvestPlan)
root.order.add_edge(HarvestPlan, WasteRecycle)

# Save the final result in the variable 'root'