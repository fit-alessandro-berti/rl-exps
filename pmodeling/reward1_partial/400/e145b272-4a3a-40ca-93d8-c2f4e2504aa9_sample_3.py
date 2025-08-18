import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
SystemDesign = Transition(label='System Design')
PermitFiling = Transition(label='Permit Filing')
ModularBuild = Transition(label='Modular Build')
SensorInstall = Transition(label='Sensor Install')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
WasteSetup = Transition(label='Waste Setup')
IoTDeploy = Transition(label='IoT Deploy')
AI_Scheduling = Transition(label='AI Scheduling')
EnergyAudit = Transition(label='Energy Audit')
ComplianceCheck = Transition(label='Compliance Check')
CropPlanting = Transition(label='Crop Planting')
YieldMonitor = Transition(label='Yield Monitor')
DataAnalysis = Transition(label='Data Analysis')
SystemUpgrade = Transition(label='System Upgrade')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    SystemDesign,
    PermitFiling,
    ModularBuild,
    SensorInstall,
    ClimateSetup,
    NutrientMix,
    WasteSetup,
    IoTDeploy,
    AI_Scheduling,
    EnergyAudit,
    ComplianceCheck,
    CropPlanting,
    YieldMonitor,
    DataAnalysis,
    SystemUpgrade
])

# Define the partial order dependencies
root.order.add_edge(SiteSurvey, SystemDesign)
root.order.add_edge(SystemDesign, PermitFiling)
root.order.add_edge(PermitFiling, ModularBuild)
root.order.add_edge(ModularBuild, SensorInstall)
root.order.add_edge(SensorInstall, ClimateSetup)
root.order.add_edge(ClimateSetup, NutrientMix)
root.order.add_edge(NutrientMix, WasteSetup)
root.order.add_edge(WasteSetup, IoTDeploy)
root.order.add_edge(IoTDeploy, AI_Scheduling)
root.order.add_edge(AI_Scheduling, EnergyAudit)
root.order.add_edge(EnergyAudit, ComplianceCheck)
root.order.add_edge(ComplianceCheck, CropPlanting)
root.order.add_edge(CropPlanting, YieldMonitor)
root.order.add_edge(YieldMonitor, DataAnalysis)
root.order.add_edge(DataAnalysis, SystemUpgrade)

# Print the root POWL model
print(root)