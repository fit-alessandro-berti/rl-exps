import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
nutrient_mix_and_delivery = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_delivery])
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, light_adjustment])
health_check_and_pest_control = OperatorPOWL(operator=Operator.XOR, children=[health_check, pest_control])
harvest_and_waste_sorting = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, waste_sorting])
biomass_and_energy_recycling = OperatorPOWL(operator=Operator.XOR, children=[biomass_process, energy_recycling])

# Define the main process
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    seedling_transplant,
    nutrient_mix_and_delivery,
    climate_control_loop,
    health_check_and_pest_control,
    harvest_and_waste_sorting,
    biomass_and_energy_recycling,
    data_analysis,
    yield_forecast
])

# Define dependencies
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, seedling_transplant)
root.order.add_edge(seedling_transplant, nutrient_mix_and_delivery)
root.order.add_edge(nutrient_mix_and_delivery, climate_control_loop)
root.order.add_edge(climate_control_loop, health_check_and_pest_control)
root.order.add_edge(health_check_and_pest_control, harvest_and_waste_sorting)
root.order.add_edge(harvest_and_waste_sorting, biomass_and_energy_recycling)
root.order.add_edge(biomass_and_energy_recycling, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)

# Print the root of the POWL model
print(root)