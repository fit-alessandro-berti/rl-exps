import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow
seed_selection_process = StrictPartialOrder(nodes=[seed_selection, germination_start])
germination_start_process = StrictPartialOrder(nodes=[germination_start, seedling_transplant])
seedling_transplant_process = StrictPartialOrder(nodes=[seedling_transplant, nutrient_mix])
nutrient_mix_process = StrictPartialOrder(nodes=[nutrient_mix, water_delivery])
water_delivery_process = StrictPartialOrder(nodes=[water_delivery, light_adjustment])
light_adjustment_process = StrictPartialOrder(nodes=[light_adjustment, climate_control])
climate_control_process = StrictPartialOrder(nodes=[climate_control, sensor_monitoring])
sensor_monitoring_process = StrictPartialOrder(nodes=[sensor_monitoring, health_check])
health_check_process = StrictPartialOrder(nodes=[health_check, pest_control])
pest_control_process = StrictPartialOrder(nodes=[pest_control, harvest_planning])
harvest_planning_process = StrictPartialOrder(nodes=[harvest_planning, crop_harvest])
crop_harvest_process = StrictPartialOrder(nodes=[crop_harvest, waste_sorting])
waste_sorting_process = StrictPartialOrder(nodes=[waste_sorting, biomass_process])
biomass_process_process = StrictPartialOrder(nodes=[biomass_process, energy_recycling])
energy_recycling_process = StrictPartialOrder(nodes=[energy_recycling, data_analysis])
data_analysis_process = StrictPartialOrder(nodes=[data_analysis, yield_forecast])

# Define the dependencies
seed_selection_process.order.add_edge(seed_selection, germination_start)
germination_start_process.order.add_edge(germination_start, seedling_transplant)
seedling_transplant_process.order.add_edge(seedling_transplant, nutrient_mix)
nutrient_mix_process.order.add_edge(nutrient_mix, water_delivery)
water_delivery_process.order.add_edge(water_delivery, light_adjustment)
light_adjustment_process.order.add_edge(light_adjustment, climate_control)
climate_control_process.order.add_edge(climate_control, sensor_monitoring)
sensor_monitoring_process.order.add_edge(sensor_monitoring, health_check)
health_check_process.order.add_edge(health_check, pest_control)
pest_control_process.order.add_edge(pest_control, harvest_planning)
harvest_planning_process.order.add_edge(harvest_planning, crop_harvest)
crop_harvest_process.order.add_edge(crop_harvest, waste_sorting)
waste_sorting_process.order.add_edge(waste_sorting, biomass_process)
biomass_process_process.order.add_edge(biomass_process, energy_recycling)
energy_recycling_process.order.add_edge(energy_recycling, data_analysis)
data_analysis_process.order.add_edge(data_analysis, yield_forecast)

# Define the root
root = StrictPartialOrder(nodes=[seed_selection_process, germination_start_process, seedling_transplant_process, nutrient_mix_process, water_delivery_process, light_adjustment_process, climate_control_process, sensor_monitoring_process, health_check_process, pest_control_process, harvest_planning_process, crop_harvest_process, waste_sorting_process, biomass_process_process, energy_recycling_process, data_analysis_process, yield_forecast])

print(root)