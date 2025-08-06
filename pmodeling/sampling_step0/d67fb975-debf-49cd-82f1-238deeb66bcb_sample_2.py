import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, climate_monitor, irrigate_adjust, nutrient_feed, pest_control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, feedback_collect, seed_select, plant_precise])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, network_distribute])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[compost_create])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)

print(root)