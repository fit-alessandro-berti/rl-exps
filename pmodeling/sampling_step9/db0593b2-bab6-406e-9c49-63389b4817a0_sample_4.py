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

# Define the loop for pest monitoring and staff training
pest_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[PestMonitor, StaffTraining])

# Define the exclusive choice for crop selection based on local demand and climate simulation
crop_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[CropSelection, ClimateSimulate])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[SiteAssess, EnvAnalysis, ModularInstall, IrrigationSetup, NutrientMix, LightingCalibrate, pest_training_loop, crop_selection_choice, EnergyIntegrate, DataAnalytics, WasteRecycle, MarketDevelop, YieldOptimize])
root.order.add_edge(SiteAssess, EnvAnalysis)
root.order.add_edge(EnvAnalysis, ModularInstall)
root.order.add_edge(ModularInstall, IrrigationSetup)
root.order.add_edge(IrrigationSetup, NutrientMix)
root.order.add_edge(NutrientMix, LightingCalibrate)
root.order.add_edge(LightingCalibrate, pest_training_loop)
root.order.add_edge(pest_training_loop, crop_selection_choice)
root.order.add_edge(crop_selection_choice, EnergyIntegrate)
root.order.add_edge(EnergyIntegrate, DataAnalytics)
root.order.add_edge(DataAnalytics, WasteRecycle)
root.order.add_edge(WasteRecycle, MarketDevelop)
root.order.add_edge(MarketDevelop, YieldOptimize)