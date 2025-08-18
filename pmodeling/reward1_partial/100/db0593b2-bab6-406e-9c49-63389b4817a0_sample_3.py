import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_site_assess = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess])
xor_env_analysis = OperatorPOWL(operator=Operator.XOR, children=[EnvAnalysis, skip])
xor_modular_install = OperatorPOWL(operator=Operator.XOR, children=[ModularInstall, skip])
xor_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSetup, skip])
xor_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[CropSelection, skip])
xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[NutrientMix, skip])
xor_lighting_calibrate = OperatorPOWL(operator=Operator.XOR, children=[LightingCalibrate, skip])
xor_pest_monitor = OperatorPOWL(operator=Operator.XOR, children=[PestMonitor, skip])
xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[StaffTraining, skip])
xor_energy_integrate = OperatorPOWL(operator=Operator.XOR, children=[EnergyIntegrate, skip])
xor_data_analytics = OperatorPOWL(operator=Operator.XOR, children=[DataAnalytics, skip])
xor_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[WasteRecycle, skip])
xor_market_develop = OperatorPOWL(operator=Operator.XOR, children=[MarketDevelop, skip])
xor_yield_optimize = OperatorPOWL(operator=Operator.XOR, children=[YieldOptimize, skip])
xor_climate_simulate = OperatorPOWL(operator=Operator.XOR, children=[ClimateSimulate, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    loop_site_assess,
    xor_env_analysis,
    xor_modular_install,
    xor_irrigation_setup,
    xor_crop_selection,
    xor_nutrient_mix,
    xor_lighting_calibrate,
    xor_pest_monitor,
    xor_staff_training,
    xor_energy_integrate,
    xor_data_analytics,
    xor_waste_recycle,
    xor_market_develop,
    xor_yield_optimize,
    xor_climate_simulate
])

# Define the dependencies in the POWL model
root.order.add_edge(loop_site_assess, xor_env_analysis)
root.order.add_edge(xor_env_analysis, xor_modular_install)
root.order.add_edge(xor_modular_install, xor_irrigation_setup)
root.order.add_edge(xor_irrigation_setup, xor_crop_selection)
root.order.add_edge(xor_crop_selection, xor_nutrient_mix)
root.order.add_edge(xor_nutrient_mix, xor_lighting_calibrate)
root.order.add_edge(xor_lighting_calibrate, xor_pest_monitor)
root.order.add_edge(xor_pest_monitor, xor_staff_training)
root.order.add_edge(xor_staff_training, xor_energy_integrate)
root.order.add_edge(xor_energy_integrate, xor_data_analytics)
root.order.add_edge(xor_data_analytics, xor_waste_recycle)
root.order.add_edge(xor_waste_recycle, xor_market_develop)
root.order.add_edge(xor_market_develop, xor_yield_optimize)
root.order.add_edge(xor_yield_optimize, xor_climate_simulate)