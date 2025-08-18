import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sensor_setup = Transition(label='Sensor Setup')
data_collection = Transition(label='Data Collection')
weather_check = Transition(label='Weather Check')
soil_testing = Transition(label='Soil Testing')
crop_selection = Transition(label='Crop Selection')
resource_assign = Transition(label='Resource Assign')
irrigation_adjust = Transition(label='Irrigation Adjust')
pest_scan = Transition(label='Pest Scan')
nutrient_mix = Transition(label='Nutrient Mix')
growth_monitor = Transition(label='Growth Monitor')
community_poll = Transition(label='Community Poll')
schedule_update = Transition(label='Schedule Update')
harvest_plan = Transition(label='Harvest Plan')
waste_sort = Transition(label='Waste Sort')
yield_report = Transition(label='Yield Report')

# Define silent transitions
skip = SilentTransition()

# Define the process model using POWL
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_adjust, nutrient_mix])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[community_poll, schedule_update])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, waste_sort])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[sensor_setup, data_collection, weather_check, soil_testing, crop_selection, resource_assign, loop1, loop2, loop3, xor, yield_report])
root.order.add_edge(sensor_setup, data_collection)
root.order.add_edge(data_collection, weather_check)
root.order.add_edge(data_collection, soil_testing)
root.order.add_edge(soil_testing, crop_selection)
root.order.add_edge(crop_selection, resource_assign)
root.order.add_edge(resource_assign, loop1)
root.order.add_edge(resource_assign, loop2)
root.order.add_edge(resource_assign, loop3)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, yield_report)