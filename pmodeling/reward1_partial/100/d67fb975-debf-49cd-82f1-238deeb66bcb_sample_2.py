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

# Define silent transitions
skip = SilentTransition()

# Define the process structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_monitor, nutrient_feed, pest_control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, climate_monitor, nutrient_feed])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[seed_select, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[community_engage, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[yield_harvest, waste_sort])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])

root = StrictPartialOrder(nodes=[site_analyze, soil_enhance, xor1, xor2, xor3, xor4, loop1, loop2])
root.order.add_edge(site_analyze, soil_enhance)
root.order.add_edge(soil_enhance, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, climate_monitor)
root.order.add_edge(climate_monitor, nutrient_feed)
root.order.add_edge(nutrient_feed, pest_control)
root.order.add_edge(pest_control, loop1)
root.order.add_edge(loop1, sensor_deploy)
root.order.add_edge(sensor_deploy, climate_monitor)
root.order.add_edge(climate_monitor, nutrient_feed)
root.order.add_edge(nutrient_feed, loop2)
root.order.add_edge(loop2, seed_select)
root.order.add_edge(seed_select, xor2)
root.order.add_edge(xor2, community_engage)
root.order.add_edge(community_engage, feedback_collect)
root.order.add_edge(feedback_collect, xor3)
root.order.add_edge(xor3, yield_harvest)
root.order.add_edge(yield_harvest, network_distribute)
root.order.add_edge(yield_harvest, waste_sort)
root.order.add_edge(waste_sort, compost_create)
root.order.add_edge(compost_create, data_analyze)
root.order.add_edge(data_analyze, xor4)
root.order.add_edge(xor4, network_distribute)

print(root)