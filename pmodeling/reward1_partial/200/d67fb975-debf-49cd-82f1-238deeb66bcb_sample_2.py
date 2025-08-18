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

# Define silent transitions for the start and end of the process
start = SilentTransition()
end = SilentTransition()

# Define loops for continuous monitoring and community engagement
climate_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_monitor, community_engage, feedback_collect])
soil_enhance_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_enhance, sensor_deploy, nutrient_feed])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, sensor_deploy, nutrient_feed])
waste_sort_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sort, compost_create])

# Define the partial order structure
root = StrictPartialOrder(nodes=[start, site_analyze, soil_enhance, seed_select, plant_precise, climate_monitor_loop, soil_enhance_loop, pest_control_loop, community_engage, feedback_collect, yield_harvest, waste_sort_loop, network_distribute, end])
root.order.add_edge(start, site_analyze)
root.order.add_edge(site_analyze, soil_enhance)
root.order.add_edge(soil_enhance, seed_select)
root.order.add_edge(seed_select, plant_precise)
root.order.add_edge(plant_precise, climate_monitor_loop)
root.order.add_edge(climate_monitor_loop, soil_enhance_loop)
root.order.add_edge(soil_enhance_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, community_engage)
root.order.add_edge(community_engage, feedback_collect)
root.order.add_edge(feedback_collect, yield_harvest)
root.order.add_edge(yield_harvest, waste_sort_loop)
root.order.add_edge(waste_sort_loop, network_distribute)
root.order.add_edge(network_distribute, end)