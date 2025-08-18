import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the transitions for skipping
skip = SilentTransition()

# Define the loop node for the resource assign and irrigation adjust activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[resource_assign, irrigation_adjust])

# Define the exclusive choice for the pest scan and nutrient mix activities
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, nutrient_mix])

# Define the exclusive choice for the community poll and schedule update activities
xor2 = OperatorPOWL(operator=Operator.XOR, children=[community_poll, schedule_update])

# Define the exclusive choice for the harvest plan and waste sort activities
xor3 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, waste_sort])

# Define the exclusive choice for the yield report and the final activity
xor4 = OperatorPOWL(operator=Operator.XOR, children=[yield_report, skip])

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[sensor_setup, data_collection, weather_check, soil_testing, crop_selection, loop, xor, xor2, xor3, xor4])
root.order.add_edge(sensor_setup, data_collection)
root.order.add_edge(data_collection, weather_check)
root.order.add_edge(weather_check, soil_testing)
root.order.add_edge(soil_testing, crop_selection)
root.order.add_edge(crop_selection, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, yield_report)

# Print the root node of the POWL model
print(root)