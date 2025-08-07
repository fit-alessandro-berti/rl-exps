import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Build the adaptive cycle: Data Collection -> Weather Check -> Soil Testing -> Crop Selection
adaptive_cycle = StrictPartialOrder(nodes=[
    data_collection, weather_check, soil_testing, crop_selection
])
adaptive_cycle.order.add_edge(data_collection, weather_check)
adaptive_cycle.order.add_edge(weather_check, soil_testing)
adaptive_cycle.order.add_edge(soil_testing, crop_selection)

# Loop: Irrigation Adjust -> Pest Scan -> Nutrient Mix -> Growth Monitor -> Community Poll -> Schedule Update
irrigation_loop = StrictPartialOrder(nodes=[
    irrigation_adjust, pest_scan, nutrient_mix, growth_monitor, community_poll, schedule_update
])
irrigation_loop.order.add_edge(irrigation_adjust, pest_scan)
irrigation_loop.order.add_edge(pest_scan, nutrient_mix)
irrigation_loop.order.add_edge(nutrient_mix, growth_monitor)
irrigation_loop.order.add_edge(growth_monitor, community_poll)
irrigation_loop.order.add_edge(community_poll, schedule_update)

# Final loop: Harvest Plan -> Waste Sort -> Yield Report
harvest_loop = StrictPartialOrder(nodes=[harvest_plan, waste_sort, yield_report])
harvest_loop.order.add_edge(harvest_plan, waste_sort)
harvest_loop.order.add_edge(waste_sort, yield_report)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    sensor_setup, adaptive_cycle,
    irrigation_loop, harvest_loop
])
root.order.add_edge(sensor_setup, adaptive_cycle)
root.order.add_edge(adaptive_cycle, irrigation_loop)
root.order.add_edge(adaptive_cycle, harvest_loop)