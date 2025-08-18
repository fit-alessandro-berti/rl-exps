import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
SiteSurvey = Transition(label='Site Survey')
EnvAnalysis = Transition(label='Env Analysis')
ModularBuild = Transition(label='Modular Build')
HydroponicSetup = Transition(label='Hydroponic Setup')
SeedSelect = Transition(label='Seed Select')
NutrientPrep = Transition(label='Nutrient Prep')
ClimateCalibrate = Transition(label='Climate Calibrate')
SensorInstall = Transition(label='Sensor Install')
AIIntegration = Transition(label='AI Integration')
CropMonitor = Transition(label='Crop Monitor')
GrowthAdjust = Transition(label='Growth Adjust')
HarvestSort = Transition(label='Harvest Sort')
Packaging = Transition(label='Packaging')
DistributionPlan = Transition(label='Distribution Plan')
SustainAudit = Transition(label='Sustain Audit')
EnergyOptimize = Transition(label='Energy Optimize')

# Define the process structure
SiteSurveyToEnvAnalysis = OperatorPOWL(operator=Operator.XOR, children=[SiteSurvey, EnvAnalysis])
EnvAnalysisToModularBuild = OperatorPOWL(operator=Operator.XOR, children=[EnvAnalysis, ModularBuild])
ModularBuildToHydroponicSetup = OperatorPOWL(operator=Operator.XOR, children=[ModularBuild, HydroponicSetup])
HydroponicSetupToSeedSelect = OperatorPOWL(operator=Operator.XOR, children=[HydroponicSetup, SeedSelect])
SeedSelectToNutrientPrep = OperatorPOWL(operator=Operator.XOR, children=[SeedSelect, NutrientPrep])
NutrientPrepToClimateCalibrate = OperatorPOWL(operator=Operator.XOR, children=[NutrientPrep, ClimateCalibrate])
ClimateCalibrateToSensorInstall = OperatorPOWL(operator=Operator.XOR, children=[ClimateCalibrate, SensorInstall])
SensorInstallToAIIntegration = OperatorPOWL(operator=Operator.XOR, children=[SensorInstall, AIIntegration])
AIIntegrationToCropMonitor = OperatorPOWL(operator=Operator.XOR, children=[AIIntegration, CropMonitor])
CropMonitorToGrowthAdjust = OperatorPOWL(operator=Operator.XOR, children=[CropMonitor, GrowthAdjust])
GrowthAdjustToHarvestSort = OperatorPOWL(operator=Operator.XOR, children=[GrowthAdjust, HarvestSort])
HarvestSortToPackaging = OperatorPOWL(operator=Operator.XOR, children=[HarvestSort, Packaging])
PackagingToDistributionPlan = OperatorPOWL(operator=Operator.XOR, children=[Packaging, DistributionPlan])
DistributionPlanToSustainAudit = OperatorPOWL(operator=Operator.XOR, children=[DistributionPlan, SustainAudit])
SustainAuditToEnergyOptimize = OperatorPOWL(operator=Operator.XOR, children=[SustainAudit, EnergyOptimize])

# Define the partial order of the process
root = StrictPartialOrder(nodes=[
    SiteSurveyToEnvAnalysis,
    EnvAnalysisToModularBuild,
    ModularBuildToHydroponicSetup,
    HydroponicSetupToSeedSelect,
    SeedSelectToNutrientPrep,
    NutrientPrepToClimateCalibrate,
    ClimateCalibrateToSensorInstall,
    SensorInstallToAIIntegration,
    AIIntegrationToCropMonitor,
    CropMonitorToGrowthAdjust,
    GrowthAdjustToHarvestSort,
    HarvestSortToPackaging,
    PackagingToDistributionPlan,
    DistributionPlanToSustainAudit,
    SustainAuditToEnergyOptimize
])

# Define the edges between nodes
root.order.add_edge(SiteSurveyToEnvAnalysis, EnvAnalysisToModularBuild)
root.order.add_edge(EnvAnalysisToModularBuild, ModularBuildToHydroponicSetup)
root.order.add_edge(ModularBuildToHydroponicSetup, HydroponicSetupToSeedSelect)
root.order.add_edge(HydroponicSetupToSeedSelect, SeedSelectToNutrientPrep)
root.order.add_edge(SeedSelectToNutrientPrep, NutrientPrepToClimateCalibrate)
root.order.add_edge(NutrientPrepToClimateCalibrate, ClimateCalibrateToSensorInstall)
root.order.add_edge(ClimateCalibrateToSensorInstall, SensorInstallToAIIntegration)
root.order.add_edge(SensorInstallToAIIntegration, AIIntegrationToCropMonitor)
root.order.add_edge(AIIntegrationToCropMonitor, CropMonitorToGrowthAdjust)
root.order.add_edge(CropMonitorToGrowthAdjust, GrowthAdjustToHarvestSort)
root.order.add_edge(GrowthAdjustToHarvestSort, HarvestSortToPackaging)
root.order.add_edge(HarvestSortToPackaging, PackagingToDistributionPlan)
root.order.add_edge(PackagingToDistributionPlan, DistributionPlanToSustainAudit)
root.order.add_edge(DistributionPlanToSustainAudit, SustainAuditToEnergyOptimize)

print(root)