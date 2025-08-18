from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the adaptive urban farming process
root = StrictPartialOrder()

# Define the activities
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

# Define the partial order structure
root.add_node(site_analyze)
root.add_node(soil_enhance)
root.add_node(seed_select)
root.add_node(plant_precise)
root.add_node(sensor_deploy)
root.add_node(climate_monitor)
root.add_node(irrigate_adjust)
root.add_node(nutrient_feed)
root.add_node(pest_control)
root.add_node(community_engage)
root.add_node(feedback_collect)
root.add_node(yield_harvest)
root.add_node(waste_sort)
root.add_node(compost_create)
root.add_node(data_analyze)
root.add_node(network_distribute)

# Define the dependencies between activities
root.add_edge(site_analyze, soil_enhance)
root.add_edge(soil_enhance, seed_select)
root.add_edge(seed_select, plant_precise)
root.add_edge(plant_precise, sensor_deploy)
root.add_edge(sensor_deploy, climate_monitor)
root.add_edge(climate_monitor, irrigate_adjust)
root.add_edge(irrigate_adjust, nutrient_feed)
root.add_edge(nutrient_feed, pest_control)
root.add_edge(pest_control, community_engage)
root.add_edge(community_engage, feedback_collect)
root.add_edge(feedback_collect, yield_harvest)
root.add_edge(yield_harvest, waste_sort)
root.add_edge(waste_sort, compost_create)
root.add_edge(compost_create, data_analyze)
root.add_edge(data_analyze, network_distribute)

# Print the root of the POWL model
print(root)