import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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

# Build the monitoring & adjustment sub‐process
monitoring = StrictPartialOrder(nodes=[climate_monitor, irrigate_adjust, nutrient_feed, pest_control])
monitoring.order.add_edge(climate_monitor, irrigate_adjust)
monitoring.order.add_edge(climate_monitor, nutrient_feed)
monitoring.order.add_edge(irrigate_adjust, pest_control)
monitoring.order.add_edge(nutrient_feed, pest_control)

# Build the community‐engagement sub‐process
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, feedback_collect])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_analyze, soil_enhance, seed_select, plant_precise, sensor_deploy,
    monitoring, community_loop,
    yield_harvest, waste_sort, compost_create, data_analyze, network_distribute
])

# Sequential dependencies
root.order.add_edge(site_analyze, soil_enhance)
root.order.add_edge(soil_enhance, seed_select)
root.order.add_edge(seed_select, plant_precise)
root.order.add_edge(plant_precise, sensor_deploy)

# After sensor deployment, run monitoring in parallel
root.order.add_edge(sensor_deploy, monitoring)

# After monitoring, run community loop in parallel
root.order.add_edge(monitoring, community_loop)

# Community loop results feed into harvest
root.order.add_edge(community_loop, yield_harvest)

# Harvest results go to waste sorting
root.order.add_edge(yield_harvest, waste_sort)

# Waste sorting leads to compost creation
root.order.add_edge(waste_sort, compost_create)

# Compost creation and harvest data feed into data analysis
root.order.add_edge(compost_create, data_analyze)
root.order.add_edge(yield_harvest, data_analyze)

# Finally, distribute through network
root.order.add_edge(data_analyze, network_distribute)