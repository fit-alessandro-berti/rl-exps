import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
skip = SilentTransition()

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, crop_selection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, nutrient_mix])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_adjust, growth_monitor])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[community_poll, schedule_update])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, waste_sort])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[yield_report, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, weather_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6])

root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop2, xor5)
root.order.add_edge(loop2, xor6)

# Print the POWL model
print(root)