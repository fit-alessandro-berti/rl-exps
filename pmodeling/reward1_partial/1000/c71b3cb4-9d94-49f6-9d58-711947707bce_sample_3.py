import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
seedling_transplant = Transition(label='Seedling Transplant')
nutrient_mix = Transition(label='Nutrient Mix')
water_delivery = Transition(label='Water Delivery')
light_adjustment = Transition(label='Light Adjustment')
climate_control = Transition(label='Climate Control')
sensor_monitoring = Transition(label='Sensor Monitoring')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
harvest_planning = Transition(label='Harvest Planning')
crop_harvest = Transition(label='Crop Harvest')
waste_sorting = Transition(label='Waste Sorting')
biomass_process = Transition(label='Biomass Process')
energy_recycling = Transition(label='Energy Recycling')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

# Define the loop for the sensor monitoring, health check, and pest control activities
sensor_health_pest = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, health_check, pest_control])

# Define the exclusive choice for the nutrient mix, water delivery, and light adjustment activities
nutrient_water_light = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, water_delivery, light_adjustment])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[seed_selection, germination_start, seedling_transplant, nutrient_water_light, sensor_health_pest, harvest_planning, crop_harvest, waste_sorting, biomass_process, energy_recycling, data_analysis, yield_forecast])
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, seedling_transplant)
root.order.add_edge(seedling_transplant, nutrient_water_light)
root.order.add_edge(nutrient_water_light, sensor_health_pest)
root.order.add_edge(sensor_health_pest, harvest_planning)
root.order.add_edge(harvest_planning, crop_harvest)
root.order.add_edge(crop_harvest, waste_sorting)
root.order.add_edge(waste_sorting, biomass_process)
root.order.add_edge(biomass_process, energy_recycling)
root.order.add_edge(energy_recycling, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)