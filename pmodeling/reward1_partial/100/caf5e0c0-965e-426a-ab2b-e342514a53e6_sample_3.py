from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteSurvey = Transition(label='Site Survey')
SystemDesign = Transition(label='System Design')
ClimateSim = Transition(label='Climate Sim')
SeedSelect = Transition(label='Seed Select')
ModuleSetup = Transition(label='Module Setup')
NutrientMix = Transition(label='Nutrient Mix')
WaterCycle = Transition(label='Water Cycle')
EnergyLink = Transition(label='Energy Link')
SensorInstall = Transition(label='Sensor Install')
PestDetect = Transition(label='Pest Detect')
GrowthScan = Transition(label='Growth Scan')
DataSync = Transition(label='Data Sync')
CommunityMeet = Transition(label='Community Meet')
RegCompliance = Transition(label='Reg Compliance')
SystemTest = Transition(label='System Test')
MaintenancePlan = Transition(label='Maintenance Plan')

# Define the partial order
root = StrictPartialOrder(
    nodes=[SiteSurvey, SystemDesign, ClimateSim, SeedSelect, ModuleSetup, NutrientMix, WaterCycle, EnergyLink, SensorInstall, PestDetect, GrowthScan, DataSync, CommunityMeet, RegCompliance, SystemTest, MaintenancePlan]
)

# Define the order of the partial order
root.order.add_edge(SiteSurvey, SystemDesign)
root.order.add_edge(SystemDesign, ClimateSim)
root.order.add_edge(ClimateSim, SeedSelect)
root.order.add_edge(SeedSelect, ModuleSetup)
root.order.add_edge(ModuleSetup, NutrientMix)
root.order.add_edge(NutrientMix, WaterCycle)
root.order.add_edge(WaterCycle, EnergyLink)
root.order.add_edge(EnergyLink, SensorInstall)
root.order.add_edge(SensorInstall, PestDetect)
root.order.add_edge(PestDetect, GrowthScan)
root.order.add_edge(GrowthScan, DataSync)
root.order.add_edge(DataSync, CommunityMeet)
root.order.add_edge(CommunityMeet, RegCompliance)
root.order.add_edge(RegCompliance, SystemTest)
root.order.add_edge(SystemTest, MaintenancePlan)

print(root)