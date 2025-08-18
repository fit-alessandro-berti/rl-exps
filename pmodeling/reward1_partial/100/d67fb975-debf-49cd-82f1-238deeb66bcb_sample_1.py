import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_select, waste_sort])
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_monitor, nutrient_feed, pest_control, community_engage, feedback_collect, yield_harvest])
po = StrictPartialOrder(nodes=[site_analyze, soil_enhance, sensor_deploy, xor, loop])

# Define the order
po.order.add_edge(site_analyze, soil_enhance)
po.order.add_edge(soil_enhance, plant_precise)
po.order.add_edge(plant_precise, sensor_deploy)
po.order.add_edge(sensor_deploy, xor)
po.order.add_edge(xor, loop)
po.order.add_edge(loop, data_analyze)
po.order.add_edge(data_analyze, network_distribute)

# Set the root
root = po