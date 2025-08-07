import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
seed_selection     = Transition(label='Seed Selection')
germination_start  = Transition(label='Germination Start')
seedling_transplant = Transition(label='Seedling Transplant')
nutrient_mix       = Transition(label='Nutrient Mix')
water_delivery     = Transition(label='Water Delivery')
light_adjustment   = Transition(label='Light Adjustment')
climate_control    = Transition(label='Climate Control')
sensor_monitoring  = Transition(label='Sensor Monitoring')
health_check       = Transition(label='Health Check')
pest_control       = Transition(label='Pest Control')
harvest_planning   = Transition(label='Harvest Planning')
crop_harvest       = Transition(label='Crop Harvest')
waste_sorting      = Transition(label='Waste Sorting')
biomass_process    = Transition(label='Biomass Process')
energy_recycling   = Transition(label='Energy Recycling')
data_analysis      = Transition(label='Data Analysis')
yield_forecast     = Transition(label='Yield Forecast')

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    seedling_transplant,
    nutrient_mix,
    water_delivery,
    light_adjustment,
    climate_control,
    sensor_monitoring,
    health_check,
    pest_control,
    harvest_planning,
    crop_harvest,
    waste_sorting,
    biomass_process,
    energy_recycling,
    data_analysis,
    yield_forecast
])

# Define the control-flow dependencies
# Germination starts immediately after seed selection
root.order.add_edge(seed_selection, germination_start)

# Seedlings transplant after germination is complete
root.order.add_edge(germination_start, seedling_transplant)

# Nutrient mix, water delivery, and light adjustment run concurrently before climate control
root.order.add_edge(nutrient_mix, climate_control)
root.order.add_edge(water_delivery, climate_control)
root.order.add_edge(light_adjustment, climate_control)

# Climate control starts immediately after all nutrient/light adjustments
root.order.add_edge(climate_control, sensor_monitoring)

# Health check and pest control run concurrently while monitoring
root.order.add_edge(health_check, sensor_monitoring)
root.order.add_edge(pest_control, sensor_monitoring)

# Harvest planning is triggered by health check
root.order.add_edge(health_check, harvest_planning)

# Harvest starts after planning is done
root.order.add_edge(harvest_planning, crop_harvest)

# Waste sorting and biomass processing run concurrently after harvest
root.order.add_edge(waste_sorting, biomass_process)

# Biomass processes feed energy back into the farm
root.order.add_edge(biomass_process, energy_recycling)

# Energy recycling feeds into the farm's power grid
root.order.add_edge(energy_recycling, climate_control)

# Data analysis and yield forecast run concurrently after harvest
root.order.add_edge(data_analysis, yield_forecast)

# Both data analysis and yield forecast are triggered by harvest
root.order.add_edge(crop_harvest, data_analysis)
root.order.add_edge(crop_harvest, yield_forecast)