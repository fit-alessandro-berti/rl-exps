import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
SiteSurvey = Transition(label='Site Survey')
StructuralAudit = Transition(label='Structural Audit')
SystemDesign = Transition(label='System Design')
PermitFiling = Transition(label='Permit Filing')
FoundationPrep = Transition(label='Foundation Prep')
FrameBuild = Transition(label='Frame Build')
IrrigationSetup = Transition(label='Irrigation Setup')
LightingInstall = Transition(label='Lighting Install')
ClimateControl = Transition(label='Climate Control')
NutrientMix = Transition(label='Nutrient Mix')
CropPlanting = Transition(label='Crop Planting')
PestScouting = Transition(label='Pest Scouting')
DataMonitoring = Transition(label='Data Monitoring')
WasteSorting = Transition(label='Waste Sorting')
EnergyAudit = Transition(label='Energy Audit')
CommunityMeet = Transition(label='Community Meet')
YieldAnalysis = Transition(label='Yield Analysis')

# Define silent transitions
Skip = SilentTransition()

# Define loop nodes
SiteSetup = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, StructuralAudit])
SystemDesignSetup = OperatorPOWL(operator=Operator.LOOP, children=[SystemDesign, PermitFiling])
FoundationBuild = OperatorPOWL(operator=Operator.LOOP, children=[FoundationPrep, FrameBuild])
IrrigationSetupLoop = OperatorPOWL(operator=Operator.LOOP, children=[IrrigationSetup, LightingInstall])
ClimateControlSetup = OperatorPOWL(operator=Operator.LOOP, children=[ClimateControl, NutrientMix])
CropPlantingSetup = OperatorPOWL(operator=Operator.LOOP, children=[CropPlanting, PestScouting])
DataMonitoringSetup = OperatorPOWL(operator=Operator.LOOP, children=[DataMonitoring, WasteSorting])
EnergyAuditSetup = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, CommunityMeet])
YieldAnalysisSetup = OperatorPOWL(operator=Operator.LOOP, children=[YieldAnalysis, Skip])

# Define partial order
root = StrictPartialOrder(nodes=[SiteSetup, SystemDesignSetup, FoundationBuild, IrrigationSetupLoop, ClimateControlSetup, CropPlantingSetup, DataMonitoringSetup, EnergyAuditSetup, YieldAnalysisSetup])
root.order.add_edge(SiteSetup, SystemDesignSetup)
root.order.add_edge(SystemDesignSetup, FoundationBuild)
root.order.add_edge(FoundationBuild, IrrigationSetupLoop)
root.order.add_edge(IrrigationSetupLoop, ClimateControlSetup)
root.order.add_edge(ClimateControlSetup, CropPlantingSetup)
root.order.add_edge(CropPlantingSetup, DataMonitoringSetup)
root.order.add_edge(DataMonitoringSetup, EnergyAuditSetup)
root.order.add_edge(EnergyAuditSetup, YieldAnalysisSetup)