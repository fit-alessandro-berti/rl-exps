from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
SitePrep = Transition(label='Site Prep')
SeedSelect = Transition(label='Seed Select')
NutrientMix = Transition(label='Nutrient Mix')
PlantingRows = Transition(label='Planting Rows')
EnvMonitor = Transition(label='Env Monitor')
WaterAdjust = Transition(label='Water Adjust')
PestControl = Transition(label='Pest Control')
GrowthCheck = Transition(label='Growth Check')
LightCalibrate = Transition(label='Light Calibrate')
EnergyManage = Transition(label='Energy Manage')
HarvestCrop = Transition(label='Harvest Crop')
QualitySort = Transition(label='Quality Sort')
PackGoods = Transition(label='Pack Goods')
ColdStore = Transition(label='Cold Store')
MarketShip = Transition(label='Market Ship')
DataAnalyze = Transition(label='Data Analyze')

# Define the partial order
root = StrictPartialOrder(nodes=[SitePrep, SeedSelect, NutrientMix, PlantingRows, EnvMonitor, WaterAdjust, PestControl, GrowthCheck, LightCalibrate, EnergyManage, HarvestCrop, QualitySort, PackGoods, ColdStore, MarketShip, DataAnalyze])