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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[germination_start, seedling_transplant, nutrient_mix, water_delivery, light_adjustment, climate_control, sensor_monitoring, health_check])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, data_analysis])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, energy_recycling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[biomass_process, crop_harvest])
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)

print(root)