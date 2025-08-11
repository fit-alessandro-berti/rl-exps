import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, data_collection, weather_check, soil_testing])
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, resource_assign, irrigation_adjust, pest_scan, nutrient_mix, growth_monitor])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_poll, schedule_update])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, waste_sort])

root = StrictPartialOrder(nodes=[sensor_loop, crop_loop, community_loop, harvest_loop])
root.order.add_edge(sensor_loop, crop_loop)
root.order.add_edge(community_loop, crop_loop)
root.order.add_edge(community_loop, harvest_loop)
root.order.add_edge(harvest_loop, community_loop)