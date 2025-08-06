import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

skip = SilentTransition()

# Define the partial order of activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[StructuralAudit, ModularDesign])
xor = OperatorPOWL(operator=Operator.XOR, children=[HydroponicSetup, ClimateConfig, NutrientMix, PestDetect, LightingSetup, EnergyAudit, AutomationInstall, StaffTraining])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[MarketAnalysis, RegulationCheck])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[YieldMonitor, WasteManage, DataAnalytics])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor3)

# Save the final result in the variable 'root'