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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_start, seedling_transplant])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_delivery, light_adjustment, climate_control])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, health_check, pest_control, harvest_planning])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[crop_harvest, waste_sorting, biomass_process])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[energy_recycling, data_analysis, yield_forecast])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)