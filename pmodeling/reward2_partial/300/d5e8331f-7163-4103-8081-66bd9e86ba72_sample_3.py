import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the dependencies
root.order.add_edge(SitePrep, SeedSelect)
root.order.add_edge(SeedSelect, NutrientMix)
root.order.add_edge(NutrientMix, PlantingRows)
root.order.add_edge(PlantingRows, EnvMonitor)
root.order.add_edge(EnvMonitor, WaterAdjust)
root.order.add_edge(WaterAdjust, PestControl)
root.order.add_edge(PestControl, GrowthCheck)
root.order.add_edge(GrowthCheck, LightCalibrate)
root.order.add_edge(LightCalibrate, EnergyManage)
root.order.add_edge(EnergyManage, HarvestCrop)
root.order.add_edge(HarvestCrop, QualitySort)
root.order.add_edge(QualitySort, PackGoods)
root.order.add_edge(PackGoods, ColdStore)
root.order.add_edge(ColdStore, MarketShip)
root.order.add_edge(MarketShip, DataAnalyze)

# Print the root of the POWL model
print(root)