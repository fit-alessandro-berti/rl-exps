import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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
root = StrictPartialOrder()

# Add transitions to the root
root.add_transition(site_analyze)
root.add_transition(soil_enhance)
root.add_transition(seed_select)
root.add_transition(plant_precise)
root.add_transition(sensor_deploy)
root.add_transition(climate_monitor)
root.add_transition(irrigate_adjust)
root.add_transition(nutrient_feed)
root.add_transition(pest_control)
root.add_transition(community_engage)
root.add_transition(feedback_collect)
root.add_transition(yield_harvest)
root.add_transition(waste_sort)
root.add_transition(compost_create)
root.add_transition(data_analyze)
root.add_transition(network_distribute)

# Define the control flow operators
root.add_operator(OperatorPOWL(operator=Operator.LOOP, children=[site_analyze, soil_enhance, seed_select, plant_precise, sensor_deploy, climate_monitor, irrigate_adjust, nutrient_feed, pest_control, community_engage, feedback_collect, yield_harvest, waste_sort, compost_create, data_analyze, network_distribute]))
root.add_operator(OperatorPOWL(operator=Operator.XOR, children=[root.get_transition_by_label('Yield Harvest'), root.get_transition_by_label('Waste Sort')]))
root.add_operator(OperatorPOWL(operator=Operator.LOOP, children=[root.get_transition_by_label('Data Analyze'), root.get_transition_by_label('Network Distribute')]))

# Add edges to the partial order
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
root.add_edge(yield_harvest, root.get_transition_by_label('Data Analyze'))
root.add_edge(yield_harvest, root.get_transition_by_label('Network Distribute'))
root.add_edge(waste_sort, compost_create)
root.add_edge(compost_create, root.get_transition_by_label('Data Analyze'))
root.add_edge(compost_create, root.get_transition_by_label('Network Distribute'))