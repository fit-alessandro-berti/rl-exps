import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
ModuleBuild = Transition(label='Module Build')
SystemInstall = Transition(label='System Install')
WaterPrep = Transition(label='Water Prep')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
ClimateSetup = Transition(label='Climate Setup')
SensorDeploy = Transition(label='Sensor Deploy')
PestScan = Transition(label='Pest Scan')
GrowthMonitor = Transition(label='Growth Monitor')
DataSync = Transition(label='Data Sync')
EnergyManage = Transition(label='Energy Manage')
HarvestPlan = Transition(label='Harvest Plan')
CommunityLink = Transition(label='Community Link')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, DesignLayout, ModuleBuild, SystemInstall, WaterPrep,
    SeedSelection, NutrientMix, ClimateSetup, SensorDeploy, PestScan,
    GrowthMonitor, DataSync, EnergyManage, HarvestPlan, CommunityLink
])

# Define the partial order dependencies
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, ModuleBuild)
root.order.add_edge(ModuleBuild, SystemInstall)
root.order.add_edge(SystemInstall, WaterPrep)
root.order.add_edge(WaterPrep, SeedSelection)
root.order.add_edge(SeedSelection, NutrientMix)
root.order.add_edge(NutrientMix, ClimateSetup)
root.order.add_edge(ClimateSetup, SensorDeploy)
root.order.add_edge(SensorDeploy, PestScan)
root.order.add_edge(PestScan, GrowthMonitor)
root.order.add_edge(GrowthMonitor, DataSync)
root.order.add_edge(DataSync, EnergyManage)
root.order.add_edge(EnergyManage, HarvestPlan)
root.order.add_edge(HarvestPlan, CommunityLink)

print(root)