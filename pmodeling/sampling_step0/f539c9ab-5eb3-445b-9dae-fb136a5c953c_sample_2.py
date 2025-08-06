import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
StructuralAudit = Transition(label='Structural Audit')
ModularDesign = Transition(label='Modular Design')
HydroponicSetup = Transition(label='Hydroponic Setup')
ClimateConfig = Transition(label='Climate Config')
NutrientMix = Transition(label='Nutrient Mix')
PestDetect = Transition(label='Pest Detect')
LightingSetup = Transition(label='Lighting Setup')
EnergyAudit = Transition(label='Energy Audit')
AutomationInstall = Transition(label='Automation Install')
StaffTraining = Transition(label='Staff Training')
MarketAnalysis = Transition(label='Market Analysis')
RegulationCheck = Transition(label='Regulation Check')
YieldMonitor = Transition(label='Yield Monitor')
WasteManage = Transition(label='Waste Manage')
DataAnalytics = Transition(label='Data Analytics')

# Define silent transitions
skip = SilentTransition()

# Define loops
ClimateConfigLoop = OperatorPOWL(operator=Operator.LOOP, children=[ClimateConfig])
EnergyAuditLoop = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit])

# Define choices
SiteSurveyChoice = OperatorPOWL(operator=Operator.XOR, children=[StructuralAudit, skip])
ModularDesignChoice = OperatorPOWL(operator=Operator.XOR, children=[HydroponicSetup, skip])
ClimateConfigChoice = OperatorPOWL(operator=Operator.XOR, children=[ClimateConfigLoop, skip])
EnergyAuditChoice = OperatorPOWL(operator=Operator.XOR, children=[EnergyAuditLoop, skip])
AutomationInstallChoice = OperatorPOWL(operator=Operator.XOR, children=[PestDetect, skip])
StaffTrainingChoice = OperatorPOWL(operator=Operator.XOR, children=[LightingSetup, skip])
MarketAnalysisChoice = OperatorPOWL(operator=Operator.XOR, children=[RegulationCheck, skip])
DataAnalyticsChoice = OperatorPOWL(operator=Operator.XOR, children=[WasteManage, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, SiteSurveyChoice, ModularDesign, ModularDesignChoice, ClimateConfig, ClimateConfigChoice, EnergyAudit, EnergyAuditChoice, AutomationInstall, AutomationInstallChoice, StaffTraining, StaffTrainingChoice, MarketAnalysis, MarketAnalysisChoice, RegulationCheck, YieldMonitor, YieldMonitorChoice, WasteManage, DataAnalyticsChoice])
root.order.add_edge(SiteSurvey, SiteSurveyChoice)
root.order.add_edge(SiteSurveyChoice, ModularDesign)
root.order.add_edge(ModularDesign, ModularDesignChoice)
root.order.add_edge(ModularDesignChoice, ClimateConfig)
root.order.add_edge(ClimateConfig, ClimateConfigChoice)
root.order.add_edge(ClimateConfigChoice, EnergyAudit)
root.order.add_edge(EnergyAudit, EnergyAuditChoice)
root.order.add_edge(EnergyAuditChoice, AutomationInstall)
root.order.add_edge(AutomationInstall, AutomationInstallChoice)
root.order.add_edge(AutomationInstallChoice, StaffTraining)
root.order.add_edge(StaffTraining, StaffTrainingChoice)
root.order.add_edge(StaffTrainingChoice, MarketAnalysis)
root.order.add_edge(MarketAnalysis, MarketAnalysisChoice)
root.order.add_edge(MarketAnalysisChoice, RegulationCheck)
root.order.add_edge(RegulationCheck, YieldMonitor)
root.order.add_edge(YieldMonitor, YieldMonitorChoice)
root.order.add_edge(YieldMonitorChoice, WasteManage)
root.order.add_edge(WasteManage, DataAnalyticsChoice)
root.order.add_edge(DataAnalyticsChoice, YieldMonitor)
root.order.add_edge(YieldMonitor, DataAnalytics)
root.order.add_edge(DataAnalytics, YieldMonitor)