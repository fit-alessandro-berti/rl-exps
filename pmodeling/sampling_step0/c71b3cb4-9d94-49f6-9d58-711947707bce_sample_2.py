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

# Define the silent transitions
skip_1 = SilentTransition()
skip_2 = SilentTransition()
skip_3 = SilentTransition()

# Define the loops and exclusive choices
# Seed Selection to Germination Start
seed_selection_to_germination_start = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_start])

# Germination Start to Seedling Transplant
germination_start_to_seedling_transplant = OperatorPOWL(operator=Operator.LOOP, children=[germination_start, seedling_transplant])

# Seedling Transplant to Nutrient Mix
seedling_transplant_to_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[seedling_transplant, nutrient_mix])

# Nutrient Mix to Water Delivery
nutrient_mix_to_water_delivery = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_delivery])

# Water Delivery to Light Adjustment
water_delivery_to_light_adjustment = OperatorPOWL(operator=Operator.LOOP, children=[water_delivery, light_adjustment])

# Light Adjustment to Climate Control
light_adjustment_to_climate_control = OperatorPOWL(operator=Operator.LOOP, children=[light_adjustment, climate_control])

# Climate Control to Sensor Monitoring
climate_control_to_sensor_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, sensor_monitoring])

# Sensor Monitoring to Health Check
sensor_monitoring_to_health_check = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, health_check])

# Health Check to Pest Control
health_check_to_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[health_check, pest_control])

# Pest Control to Harvest Planning
pest_control_to_harvest_planning = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, harvest_planning])

# Harvest Planning to Crop Harvest
harvest_planning_to_crop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[harvest_planning, crop_harvest])

# Crop Harvest to Waste Sorting
crop_harvest_to_waste_sorting = OperatorPOWL(operator=Operator.LOOP, children=[crop_harvest, waste_sorting])

# Waste Sorting to Biomass Process
waste_sorting_to_biomass_process = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting, biomass_process])

# Biomass Process to Energy Recycling
biomass_process_to_energy_recycling = OperatorPOWL(operator=Operator.LOOP, children=[biomass_process, energy_recycling])

# Energy Recycling to Data Analysis
energy_recycling_to_data_analysis = OperatorPOWL(operator=Operator.LOOP, children=[energy_recycling, data_analysis])

# Data Analysis to Yield Forecast
data_analysis_to_yield_forecast = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, yield_forecast])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    seed_selection_to_germination_start,
    germination_start_to_seedling_transplant,
    seedling_transplant_to_nutrient_mix,
    nutrient_mix_to_water_delivery,
    water_delivery_to_light_adjustment,
    light_adjustment_to_climate_control,
    climate_control_to_sensor_monitoring,
    sensor_monitoring_to_health_check,
    health_check_to_pest_control,
    pest_control_to_harvest_planning,
    harvest_planning_to_crop_harvest,
    crop_harvest_to_waste_sorting,
    waste_sorting_to_biomass_process,
    biomass_process_to_energy_recycling,
    energy_recycling_to_data_analysis,
    data_analysis_to_yield_forecast
])
root.order.add_edge(seed_selection_to_germination_start, germination_start_to_seedling_transplant)
root.order.add_edge(germination_start_to_seedling_transplant, seedling_transplant_to_nutrient_mix)
root.order.add_edge(seedling_transplant_to_nutrient_mix, nutrient_mix_to_water_delivery)
root.order.add_edge(nutrient_mix_to_water_delivery, water_delivery_to_light_adjustment)
root.order.add_edge(water_delivery_to_light_adjustment, light_adjustment_to_climate_control)
root.order.add_edge(light_adjustment_to_climate_control, climate_control_to_sensor_monitoring)
root.order.add_edge(climate_control_to_sensor_monitoring, sensor_monitoring_to_health_check)
root.order.add_edge(sensor_monitoring_to_health_check, health_check_to_pest_control)
root.order.add_edge(health_check_to_pest_control, pest_control_to_harvest_planning)
root.order.add_edge(pest_control_to_harvest_planning, harvest_planning_to_crop_harvest)
root.order.add_edge(harvest_planning_to_crop_harvest, crop_harvest_to_waste_sorting)
root.order.add_edge(crop_harvest_to_waste_sorting, waste_sorting_to_biomass_process)
root.order.add_edge(waste_sorting_to_biomass_process, biomass_process_to_energy_recycling)
root.order.add_edge(biomass_process_to_energy_recycling, energy_recycling_to_data_analysis)
root.order.add_edge(energy_recycling_to_data_analysis, data_analysis_to_yield_forecast)