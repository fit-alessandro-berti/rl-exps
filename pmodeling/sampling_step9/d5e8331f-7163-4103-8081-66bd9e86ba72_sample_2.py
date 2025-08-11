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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SitePrep, SeedSelect, NutrientMix, PlantingRows, EnvMonitor, WaterAdjust, PestControl, GrowthCheck, LightCalibrate, EnergyManage])
xor = OperatorPOWL(operator=Operator.XOR, children=[HarvestCrop, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)