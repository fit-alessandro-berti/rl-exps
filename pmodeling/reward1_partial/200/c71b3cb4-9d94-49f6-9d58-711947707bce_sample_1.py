from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the operators for the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, health_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, waste_sorting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[biomass_process, energy_recycling])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, yield_forecast])
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, xor1, nutrient_mix, water_delivery, light_adjustment, climate_control])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, germination_start, seedling_transplant, xor2, xor3, xor4])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor5])

# Add edges to define the order of execution
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, nutrient_mix)
root.order.add_edge(loop, water_delivery)
root.order.add_edge(loop, light_adjustment)
root.order.add_edge(loop, climate_control)
root.order.add_edge(xor1, health_check)
root.order.add_edge(xor1, pest_control)
root.order.add_edge(xor2, crop_harvest)
root.order.add_edge(xor2, waste_sorting)
root.order.add_edge(xor3, biomass_process)
root.order.add_edge(xor3, energy_recycling)
root.order.add_edge(xor4, data_analysis)
root.order.add_edge(xor4, yield_forecast)

# Print the root of the POWL model
print(root)