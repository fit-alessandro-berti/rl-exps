import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
seed_selection    = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
seedling_transplant = Transition(label='Seedling Transplant')
nutrient_mix      = Transition(label='Nutrient Mix')
water_delivery    = Transition(label='Water Delivery')
light_adjustment  = Transition(label='Light Adjustment')
climate_control   = Transition(label='Climate Control')
sensor_monitoring = Transition(label='Sensor Monitoring')
health_check      = Transition(label='Health Check')
pest_control      = Transition(label='Pest Control')
harvest_planning  = Transition(label='Harvest Planning')
crop_harvest      = Transition(label='Crop Harvest')
waste_sorting     = Transition(label='Waste Sorting')
biomass_process   = Transition(label='Biomass Process')
energy_recycling  = Transition(label='Energy Recycling')
data_analysis     = Transition(label='Data Analysis')
yield_forecast    = Transition(label='Yield Forecast')

# Build the monitoring and control loop: Sensor Monitoring -> {Health Check, Pest Control} -> repeat
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sensor_monitoring, OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])]
)

# Build the post-harvest sequence: Waste Sorting -> Biomass Process -> Energy Recycling
post_harvest_seq = StrictPartialOrder(nodes=[waste_sorting, biomass_process, energy_recycling])
post_harvest_seq.order.add_edge(waste_sorting, biomass_process)
post_harvest_seq.order.add_edge(biomass_process, energy_recycling)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    seedling_transplant,
    nutrient_mix,
    water_delivery,
    light_adjustment,
    climate_control,
    monitoring_loop,
    harvest_planning,
    crop_harvest,
    post_harvest_seq,
    data_analysis,
    yield_forecast
])

# Define the control-flow dependencies
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, seedling_transplant)
root.order.add_edge(seedling_transplant, nutrient_mix)
root.order.add_edge(nutrient_mix, water_delivery)
root.order.add_edge(water_delivery, light_adjustment)
root.order.add_edge(light_adjustment, climate_control)
root.order.add_edge(climate_control, monitoring_loop)
root.order.add_edge(monitoring_loop, harvest_planning)
root.order.add_edge(harvest_planning, crop_harvest)
root.order.add_edge(crop_harvest, post_harvest_seq)
root.order.add_edge(post_harvest_seq, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)