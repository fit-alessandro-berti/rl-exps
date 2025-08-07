import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names as given
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

# Create the root Partial Order with all activities
root = StrictPartialOrder(nodes=[
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

# Since there are no explicit dependencies in the problem description, we assume all activities are concurrent.
# If there were dependencies, they would be added using root.order.add_edge(source, target)

print(root)