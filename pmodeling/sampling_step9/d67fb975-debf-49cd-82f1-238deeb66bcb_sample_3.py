import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAnalyze = Transition(label='Site Analyze')
SoilEnhance = Transition(label='Soil Enhance')
SeedSelect = Transition(label='Seed Select')
PlantPrecise = Transition(label='Plant Precise')
SensorDeploy = Transition(label='Sensor Deploy')
ClimateMonitor = Transition(label='Climate Monitor')
IrrigateAdjust = Transition(label='Irrigate Adjust')
NutrientFeed = Transition(label='Nutrient Feed')
PestControl = Transition(label='Pest Control')
CommunityEngage = Transition(label='Community Engage')
FeedbackCollect = Transition(label='Feedback Collect')
YieldHarvest = Transition(label='Yield Harvest')
WasteSort = Transition(label='Waste Sort')
CompostCreate = Transition(label='Compost Create')
DataAnalyze = Transition(label='Data Analyze')
NetworkDistribute = Transition(label='Network Distribute')
skip = SilentTransition()

site_analysis = OperatorPOWL(operator=Operator.XOR, children=[SiteAnalyze, skip])
soil_enhancement = OperatorPOWL(operator=Operator.XOR, children=[SoilEnhance, skip])
seed_selection = OperatorPOWL(operator=Operator.XOR, children=[SeedSelect, skip])
plant_precise = OperatorPOWL(operator=Operator.XOR, children=[PlantPrecise, skip])
sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[SensorDeploy, skip])
climate_monitor = OperatorPOWL(operator=Operator.XOR, children=[ClimateMonitor, skip])
irrigate_adjust = OperatorPOWL(operator=Operator.XOR, children=[IrrigateAdjust, skip])
nutrient_feed = OperatorPOWL(operator=Operator.XOR, children=[NutrientFeed, skip])
pest_control = OperatorPOWL(operator=Operator.XOR, children=[PestControl, skip])
community_engage = OperatorPOWL(operator=Operator.XOR, children=[CommunityEngage, skip])
feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[FeedbackCollect, skip])
yield_harvest = OperatorPOWL(operator=Operator.XOR, children=[YieldHarvest, skip])
waste_sort = OperatorPOWL(operator=Operator.XOR, children=[WasteSort, skip])
compost_create = OperatorPOWL(operator=Operator.XOR, children=[CompostCreate, skip])
data_analyze = OperatorPOWL(operator=Operator.XOR, children=[DataAnalyze, skip])
network_distribute = OperatorPOWL(operator=Operator.XOR, children=[NetworkDistribute, skip])

root = StrictPartialOrder(nodes=[
    site_analysis,
    soil_enhancement,
    seed_selection,
    plant_precise,
    sensor_deploy,
    climate_monitor,
    irrigate_adjust,
    nutrient_feed,
    pest_control,
    community_engage,
    feedback_collect,
    yield_harvest,
    waste_sort,
    compost_create,
    data_analyze,
    network_distribute
])

root.order.add_edge(site_analysis, soil_enhancement)
root.order.add_edge(soil_enhancement, seed_selection)
root.order.add_edge(seed_selection, plant_precise)
root.order.add_edge(plant_precise, sensor_deploy)
root.order.add_edge(sensor_deploy, climate_monitor)
root.order.add_edge(climate_monitor, irrigate_adjust)
root.order.add_edge(irrigate_adjust, nutrient_feed)
root.order.add_edge(nutrient_feed, pest_control)
root.order.add_edge(pest_control, community_engage)
root.order.add_edge(community_engage, feedback_collect)
root.order.add_edge(feedback_collect, yield_harvest)
root.order.add_edge(yield_harvest, waste_sort)
root.order.add_edge(waste_sort, compost_create)
root.order.add_edge(compost_create, data_analyze)
root.order.add_edge(data_analyze, network_distribute)

print(root)