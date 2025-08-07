import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the activities
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_analyze, soil_enhance, seed_select, plant_precise, sensor_deploy, climate_monitor, irrigate_adjust, nutrient_feed, pest_control, community_engage, feedback_collect, yield_harvest, waste_sort, compost_create, data_analyze, network_distribute])

# Define the dependencies in the partial order
root.order.add_edge(site_analyze, soil_enhance)
root.order.add_edge(site_analyze, seed_select)
root.order.add_edge(site_analyze, plant_precise)
root.order.add_edge(site_analyze, sensor_deploy)
root.order.add_edge(site_analyze, climate_monitor)
root.order.add_edge(site_analyze, irrigate_adjust)
root.order.add_edge(site_analyze, nutrient_feed)
root.order.add_edge(site_analyze, pest_control)
root.order.add_edge(site_analyze, community_engage)
root.order.add_edge(site_analyze, feedback_collect)
root.order.add_edge(site_analyze, yield_harvest)
root.order.add_edge(site_analyze, waste_sort)
root.order.add_edge(site_analyze, compost_create)
root.order.add_edge(site_analyze, data_analyze)
root.order.add_edge(site_analyze, network_distribute)

# Print the root node
print(root)