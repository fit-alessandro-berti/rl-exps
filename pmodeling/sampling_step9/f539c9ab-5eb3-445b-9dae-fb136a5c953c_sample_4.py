import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order nodes
site_assessment = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, StructuralAudit])
modular_design = OperatorPOWL(operator=Operator.LOOP, children=[ModularDesign, HydroponicSetup])
climate_control = OperatorPOWL(operator=Operator.LOOP, children=[ClimateConfig, NutrientMix])
pest_detection = OperatorPOWL(operator=Operator.LOOP, children=[PestDetect, LightingSetup])
energy_optimization = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, AutomationInstall])
labor_training = OperatorPOWL(operator=Operator.LOOP, children=[StaffTraining, MarketAnalysis])
local_market = OperatorPOWL(operator=Operator.LOOP, children=[RegulationCheck, YieldMonitor])
continuous_yield = OperatorPOWL(operator=Operator.LOOP, children=[WasteManage, DataAnalytics])

# Create the root POWL model
root = StrictPartialOrder(nodes=[site_assessment, modular_design, climate_control, pest_detection, energy_optimization, labor_training, local_market, continuous_yield])

# Define the partial order dependencies
root.order.add_edge(site_assessment, modular_design)
root.order.add_edge(modular_design, climate_control)
root.order.add_edge(climate_control, pest_detection)
root.order.add_edge(pest_detection, energy_optimization)
root.order.add_edge(energy_optimization, labor_training)
root.order.add_edge(labor_training, local_market)
root.order.add_edge(local_market, continuous_yield)

# Print the root POWL model
print(root)