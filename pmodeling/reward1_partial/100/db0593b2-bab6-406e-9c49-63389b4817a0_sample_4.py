import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAssess = Transition(label='Site Assess')
EnvAnalysis = Transition(label='Env Analysis')
ModularInstall = Transition(label='Modular Install')
IrrigationSetup = Transition(label='Irrigation Setup')
CropSelection = Transition(label='Crop Selection')
NutrientMix = Transition(label='Nutrient Mix')
LightingCalibrate = Transition(label='Lighting Calibrate')
PestMonitor = Transition(label='Pest Monitor')
StaffTraining = Transition(label='Staff Training')
EnergyIntegrate = Transition(label='Energy Integrate')
DataAnalytics = Transition(label='Data Analytics')
WasteRecycle = Transition(label='Waste Recycle')
MarketDevelop = Transition(label='Market Develop')
YieldOptimize = Transition(label='Yield Optimize')
ClimateSimulate = Transition(label='Climate Simulate')

# Process flow
site_assess = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, EnvAnalysis])
modular_install = OperatorPOWL(operator=Operator.LOOP, children=[ModularInstall, IrrigationSetup, CropSelection, NutrientMix, LightingCalibrate, PestMonitor])
staff_training = OperatorPOWL(operator=Operator.LOOP, children=[StaffTraining])
energy_integrate = OperatorPOWL(operator=Operator.LOOP, children=[EnergyIntegrate])
data_analytics = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalytics])
waste_recycle = OperatorPOWL(operator=Operator.LOOP, children=[WasteRecycle])
market_develop = OperatorPOWL(operator=Operator.LOOP, children=[MarketDevelop])
yield_optimize = OperatorPOWL(operator=Operator.LOOP, children=[YieldOptimize])
climate_simulate = OperatorPOWL(operator=Operator.LOOP, children=[ClimateSimulate])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_assess, modular_install, staff_training, energy_integrate, data_analytics, waste_recycle, market_develop, yield_optimize, climate_simulate])
root.order.add_edge(site_assess, modular_install)
root.order.add_edge(modular_install, staff_training)
root.order.add_edge(staff_training, energy_integrate)
root.order.add_edge(energy_integrate, data_analytics)
root.order.add_edge(data_analytics, waste_recycle)
root.order.add_edge(waste_recycle, market_develop)
root.order.add_edge(market_develop, yield_optimize)
root.order.add_edge(yield_optimize, climate_simulate)