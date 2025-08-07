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

# Define the root process
root = StrictPartialOrder(nodes=[
    SiteAssess, EnvAnalysis, ModularInstall, IrrigationSetup, CropSelection, NutrientMix, LightingCalibrate, PestMonitor,
    StaffTraining, EnergyIntegrate, DataAnalytics, WasteRecycle, MarketDevelop, YieldOptimize, ClimateSimulate
])