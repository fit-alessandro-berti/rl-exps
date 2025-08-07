import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the monitoring‐adjustment loop: monitor then adjust
monitor_adjust = StrictPartialOrder(nodes=[sensor_monitoring, climate_control])
monitor_adjust.order.add_edge(sensor_monitoring, climate_control)

# Define the pest control sub‐process: check then control
pest_loop = StrictPartialOrder(nodes=[health_check, pest_control])
pest_loop.order.add_edge(health_check, pest_control)

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    seedling_transplant,
    nutrient_mix,
    water_delivery,
    light_adjustment,
    climate_control,
    monitor_adjust,
    pest_loop,
    harvest_planning,
    crop_harvest,
    waste_sorting,
    biomass_process,
    energy_recycling,
    data_analysis,
    yield_forecast
])

# Add control‐flow edges
root.order.add_edge(seed_selection,     germination_start)
root.order.add_edge(germination_start, seedling_transplant)
root.order.add_edge(seedling_transplant, nutrient_mix)
root.order.add_edge(nutrient_mix,       water_delivery)
root.order.add_edge(nutrient_mix,       light_adjustment)
root.order.add_edge(water_delivery,     monitor_adjust)
root.order.add_edge(light_adjustment,   monitor_adjust)
root.order.add_edge(monitor_adjust,     pest_loop)
root.order.add_edge(pest_loop,          harvest_planning)
root.order.add_edge(harvest_planning,   crop_harvest)
root.order.add_edge(crop_harvest,       waste_sorting)
root.order.add_edge(waste_sorting,      biomass_process)
root.order.add_edge(biomass_process,    energy_recycling)
root.order.add_edge(energy_recycling,   data_analysis)
root.order.add_edge(data_analysis,      yield_forecast)