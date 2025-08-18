import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

site_assess_env = OperatorPOWL(operator=Operator.XOR, children=[SiteAssess, EnvAnalysis])
modular_install_irrigation = OperatorPOWL(operator=Operator.LOOP, children=[ModularInstall, IrrigationSetup])
crop_selection = OperatorPOWL(operator=Operator.LOOP, children=[CropSelection, NutrientMix, LightingCalibrate, PestMonitor])
staff_training_energy = OperatorPOWL(operator=Operator.LOOP, children=[StaffTraining, EnergyIntegrate])
data_analytics_market = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalytics, WasteRecycle, MarketDevelop])
yield_optimize_climate = OperatorPOWL(operator=Operator.LOOP, children=[YieldOptimize, ClimateSimulate])

root = StrictPartialOrder(nodes=[site_assess_env, modular_install_irrigation, crop_selection, staff_training_energy, data_analytics_market, yield_optimize_climate])
root.order.add_edge(site_assess_env, modular_install_irrigation)
root.order.add_edge(modular_install_irrigation, crop_selection)
root.order.add_edge(crop_selection, staff_training_energy)
root.order.add_edge(staff_training_energy, data_analytics_market)
root.order.add_edge(data_analytics_market, yield_optimize_climate)

print(root)