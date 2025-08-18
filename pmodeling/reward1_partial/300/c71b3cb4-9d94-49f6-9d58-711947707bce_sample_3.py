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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, sensor_monitoring, health_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, water_delivery, light_adjustment, climate_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, biomass_process])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[energy_recycling, data_analysis, yield_forecast])
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_start, seedling_transplant, xor, xor2])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop, xor3, xor4])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor5])
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

print(root)