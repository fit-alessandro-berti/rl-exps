from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loop for the adaptive urban farming cycle
adaptive_cycle = OperatorPOWL(operator=Operator.LOOP, children=[
    site_analyze,
    soil_enhance,
    seed_select,
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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[adaptive_cycle])
root.order.add_edge(adaptive_cycle, adaptive_cycle)  # Since it's a loop, it points back to itself

print(root)