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

skip = SilentTransition()

# Establishing the process flow
site_assessment = OperatorPOWL(operator=Operator.CONCURRENT, children=[SiteAssess, EnvAnalysis])
modular_install = OperatorPOWL(operator=Operator.CONCURRENT, children=[ModularInstall, IrrigationSetup])
crop_selection = OperatorPOWL(operator=Operator.CONCURRENT, children=[CropSelection, NutrientMix])
lighting_calibrate = OperatorPOWL(operator=Operator.CONCURRENT, children=[LightingCalibrate, PestMonitor])
staff_training = OperatorPOWL(operator=Operator.CONCURRENT, children=[StaffTraining, EnergyIntegrate])
data_analytics = OperatorPOWL(operator=Operator.CONCURRENT, children=[DataAnalytics, WasteRecycle])
market_develop = OperatorPOWL(operator=Operator.CONCURRENT, children=[MarketDevelop, YieldOptimize])
climate_simulate = OperatorPOWL(operator=Operator.CONCURRENT, children=[ClimateSimulate])

root = StrictPartialOrder(nodes=[site_assessment, modular_install, crop_selection, lighting_calibrate, staff_training, data_analytics, market_develop, climate_simulate])
root.order.add_edge(site_assessment, modular_install)
root.order.add_edge(modular_install, crop_selection)
root.order.add_edge(crop_selection, lighting_calibrate)
root.order.add_edge(lighting_calibrate, staff_training)
root.order.add_edge(staff_training, data_analytics)
root.order.add_edge(data_analytics, market_develop)
root.order.add_edge(market_develop, climate_simulate)