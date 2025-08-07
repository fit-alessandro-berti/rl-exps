import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analyze    = Transition(label='Site Analyze')
soil_enhance    = Transition(label='Soil Enhance')
seed_select     = Transition(label='Seed Select')
plant_precise   = Transition(label='Plant Precise')
sensor_deploy   = Transition(label='Sensor Deploy')
climate_monitor = Transition(label='Climate Monitor')
irrigate_adjust = Transition(label='Irrigate Adjust')
nutrient_feed   = Transition(label='Nutrient Feed')
pest_control    = Transition(label='Pest Control')
community_engage= Transition(label='Community Engage')
feedback_collect= Transition(label='Feedback Collect')
yield_harvest   = Transition(label='Yield Harvest')
waste_sort      = Transition(label='Waste Sort')
compost_create  = Transition(label='Compost Create')
data_analyze    = Transition(label='Data Analyze')
network_distribute = Transition(label='Network Distribute')

# Build the monitoring sub-process: Sensor Deploy -> Climate Monitor -> Irrigate Adjust -> Nutrient Feed -> Pest Control
monitoring = StrictPartialOrder(nodes=[
    sensor_deploy,
    climate_monitor,
    irrigate_adjust,
    nutrient_feed,
    pest_control
])
monitoring.order.add_edge(sensor_deploy, climate_monitor)
monitoring.order.add_edge(climate_monitor, irrigate_adjust)
monitoring.order.add_edge(irrigate_adjust, nutrient_feed)
monitoring.order.add_edge(nutrient_feed, pest_control)

# Build the iterative cycle: Feedback Collect -> Yield Harvest -> Waste Sort -> Compost Create -> Data Analyze
cycle = StrictPartialOrder(nodes=[
    feedback_collect,
    yield_harvest,
    waste_sort,
    compost_create,
    data_analyze
])
cycle.order.add_edge(feedback_collect, yield_harvest)
cycle.order.add_edge(yield_harvest, waste_sort)
cycle.order.add_edge(waste_sort, compost_create)
cycle.order.add_edge(compost_create, data_analyze)

# Build the loop: execute monitoring, then optionally repeat the cycle and monitoring again
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, cycle])

# Assemble the overall process: Site Analyze -> Soil Enhance -> Seed Select -> Plant Precise -> loop
root = StrictPartialOrder(nodes=[
    site_analyze,
    soil_enhance,
    seed_select,
    plant_precise,
    loop
])
root.order.add_edge(site_analyze, soil_enhance)
root.order.add_edge(soil_enhance, seed_select)
root.order.add_edge(seed_select, plant_precise)
root.order.add_edge(plant_precise, loop)