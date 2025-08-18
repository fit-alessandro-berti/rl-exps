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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (site_analyze, soil_enhance),
        (site_analyze, seed_select),
        (soil_enhance, plant_precise),
        (sensor_deploy, climate_monitor),
        (sensor_deploy, irrigate_adjust),
        (sensor_deploy, nutrient_feed),
        (climate_monitor, irrigate_adjust),
        (climate_monitor, nutrient_feed),
        (irrigate_adjust, pest_control),
        (irrigate_adjust, yield_harvest),
        (nutrient_feed, pest_control),
        (nutrient_feed, yield_harvest),
        (pest_control, community_engage),
        (pest_control, feedback_collect),
        (community_engage, feedback_collect),
        (feedback_collect, data_analyze),
        (yield_harvest, waste_sort),
        (waste_sort, compost_create),
        (compost_create, data_analyze),
        (data_analyze, network_distribute)
    ]
)

print(root)