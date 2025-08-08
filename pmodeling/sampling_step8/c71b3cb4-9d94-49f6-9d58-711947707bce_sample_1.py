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

# Define the operators for the process
sensor_monitoring_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, SilentTransition()])
sensor_monitoring_to_health_check = OperatorPOWL(operator=Operator.XOR, children=[health_check, SilentTransition()])
health_check_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, SilentTransition()])
pest_control_to_health_check = OperatorPOWL(operator=Operator.XOR, children=[health_check, SilentTransition()])
climate_control_to_light_adjustment = OperatorPOWL(operator=Operator.XOR, children=[light_adjustment, SilentTransition()])
light_adjustment_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[climate_control, SilentTransition()])
water_delivery_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, SilentTransition()])
nutrient_mix_to_water_delivery = OperatorPOWL(operator=Operator.XOR, children=[water_delivery, SilentTransition()])
harvest_planning_to_crop_harvest = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, SilentTransition()])
crop_harvest_to_harvest_planning = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, SilentTransition()])
waste_sorting_to_biomass_process = OperatorPOWL(operator=Operator.XOR, children=[biomass_process, SilentTransition()])
biomass_process_to_waste_sorting = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, SilentTransition()])
energy_recycling_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, SilentTransition()])
data_analysis_to_energy_recycling = OperatorPOWL(operator=Operator.XOR, children=[energy_recycling, SilentTransition()])
seed_selection_to_germination_start = OperatorPOWL(operator=Operator.XOR, children=[germination_start, SilentTransition()])
germination_start_to_seedling_transplant = OperatorPOWL(operator=Operator.XOR, children=[seedling_transplant, SilentTransition()])
seedling_transplant_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, SilentTransition()])
nutrient_mix_to_water_delivery = OperatorPOWL(operator=Operator.XOR, children=[water_delivery, SilentTransition()])
water_delivery_to_light_adjustment = OperatorPOWL(operator=Operator.XOR, children=[light_adjustment, SilentTransition()])
light_adjustment_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[climate_control, SilentTransition()])
climate_control_to_sensor_monitoring = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitoring, SilentTransition()])
sensor_monitoring_to_health_check = OperatorPOWL(operator=Operator.XOR, children=[health_check, SilentTransition()])
health_check_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, SilentTransition()])
pest_control_to_health_check = OperatorPOWL(operator=Operator.XOR, children=[health_check, SilentTransition()])
health_check_to_harvest_planning = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, SilentTransition()])
harvest_planning_to_crop_harvest = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, SilentTransition()])
crop_harvest_to_waste_sorting = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, SilentTransition()])
waste_sorting_to_biomass_process = OperatorPOWL(operator=Operator.XOR, children=[biomass_process, SilentTransition()])
biomass_process_to_energy_recycling = OperatorPOWL(operator=Operator.XOR, children=[energy_recycling, SilentTransition()])
energy_recycling_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, SilentTransition()])
data_analysis_to_energy_recycling = OperatorPOWL(operator=Operator.XOR, children=[energy_recycling, SilentTransition()])
data_analysis_to_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, SilentTransition()])
yield_forecast_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, SilentTransition()])

# Define the partial order
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

# Define the dependencies between nodes
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, seedling_transplant)
root.order.add_edge(seedling_transplant, nutrient_mix)
root.order.add_edge(nutrient_mix, water_delivery)
root.order.add_edge(water_delivery, light_adjustment)
root.order.add_edge(light_adjustment, climate_control)
root.order.add_edge(climate_control, sensor_monitoring)
root.order.add_edge(sensor_monitoring, health_check)
root.order.add_edge(health_check, pest_control)
root.order.add_edge(pest_control, health_check)
root.order.add_edge(health_check, harvest_planning)
root.order.add_edge(harvest_planning, crop_harvest)
root.order.add_edge(crop_harvest, waste_sorting)
root.order.add_edge(waste_sorting, biomass_process)
root.order.add_edge(biomass_process, energy_recycling)
root.order.add_edge(energy_recycling, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)
root.order.add_edge(yield_forecast, data_analysis)

print(root)