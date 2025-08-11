import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, weather_check, soil_testing, crop_selection, resource_assign, irrigation_adjust, pest_scan, nutrient_mix, growth_monitor])

# Define the XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[community_poll, schedule_update, harvest_plan, waste_sort, yield_report])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)