import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitAcquire = Transition(label='Permit Acquire')
ModularBuild = Transition(label='Modular Build')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SeedAutomation = Transition(label='Seed Automation')
PestControl = Transition(label='Pest Control')
EnergyAudit = Transition(label='Energy Audit')
SensorInstall = Transition(label='Sensor Install')
GrowthMonitor = Transition(label='Growth Monitor')
WasteProcess = Transition(label='Waste Process')
DataAnalysis = Transition(label='Data Analysis')
StaffTrain = Transition(label='Staff Train')
CommunityLink = Transition(label='Community Link')
YieldReport = Transition(label='Yield Report')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, DesignLayout, PermitAcquire, ModularBuild,
    ClimateSetup, NutrientMix, SeedAutomation, PestControl,
    EnergyAudit, SensorInstall, GrowthMonitor, WasteProcess,
    DataAnalysis, StaffTrain, CommunityLink, YieldReport
])

# Define the dependencies between activities
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, PermitAcquire)
root.order.add_edge(PermitAcquire, ModularBuild)
root.order.add_edge(ModularBuild, ClimateSetup)
root.order.add_edge(ClimateSetup, NutrientMix)
root.order.add_edge(NutrientMix, SeedAutomation)
root.order.add_edge(SeedAutomation, PestControl)
root.order.add_edge(PestControl, EnergyAudit)
root.order.add_edge(EnergyAudit, SensorInstall)
root.order.add_edge(SensorInstall, GrowthMonitor)
root.order.add_edge(GrowthMonitor, WasteProcess)
root.order.add_edge(WasteProcess, DataAnalysis)
root.order.add_edge(DataAnalysis, StaffTrain)
root.order.add_edge(StaffTrain, CommunityLink)
root.order.add_edge(CommunityLink, YieldReport)

# Print the root to verify the model
print(root)