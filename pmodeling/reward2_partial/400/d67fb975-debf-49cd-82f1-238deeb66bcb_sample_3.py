import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analyze = Transition(label='Site Analyze')
soil_enhance = Transition(label='Soil Enhance')
seed_select = Transition(label='Seed Select')
plant_precise = Transition(label='Plant Precise')
sensor_deploy = Transition(label='Sensor Deploy')
climate_monitor = Transition(label='Climate Monitor')
irrigate_adjust = Transition(label='Irrigate Adjust')
nutrient_feed = Transition(label='Nutrient Feed')
pest_control = Transition(label='Pest Control')
community_engage = Transition(label='Community Engage')
feedback_collect = Transition(label='Feedback Collect')
yield_harvest = Transition(label='Yield Harvest')
waste_sort = Transition(label='Waste Sort')
compost_create = Transition(label='Compost Create')
data_analyze = Transition(label='Data Analyze')
network_distribute = Transition(label='Network Distribute')

# Define partial order
root = StrictPartialOrder(nodes=[
    site_analyze, soil_enhance, seed_select, plant_precise, sensor_deploy, climate_monitor,
    irrigate_adjust, nutrient_feed, pest_control, community_engage, feedback_collect,
    yield_harvest, waste_sort, compost_create, data_analyze, network_distribute
])

# Define order dependencies
root.order.add_edge(site_analyze, soil_enhance)
root.order.add_edge(soil_enhance, seed_select)
root.order.add_edge(seed_select, plant_precise)
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