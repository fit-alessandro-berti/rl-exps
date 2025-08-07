import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
sensor_setup        = Transition(label='Sensor Setup')
data_collection     = Transition(label='Data Collection')
weather_check       = Transition(label='Weather Check')
soil_testing        = Transition(label='Soil Testing')
crop_selection      = Transition(label='Crop Selection')
resource_assign     = Transition(label='Resource Assign')
irrigation_adjust   = Transition(label='Irrigation Adjust')
pest_scan           = Transition(label='Pest Scan')
nutrient_mix        = Transition(label='Nutrient Mix')
growth_monitor      = Transition(label='Growth Monitor')
community_poll      = Transition(label='Community Poll')
schedule_update     = Transition(label='Schedule Update')
harvest_plan        = Transition(label='Harvest Plan')
yield_report        = Transition(label='Yield Report')
waste_sort          = Transition(label='Waste Sort')

# Build the partial order
root = StrictPartialOrder(nodes=[
    sensor_setup, data_collection, weather_check, soil_testing,
    crop_selection, resource_assign, irrigation_adjust, pest_scan,
    nutrient_mix, growth_monitor, community_poll, schedule_update,
    harvest_plan, yield_report, waste_sort
])

# Define the control-flow dependencies
root.order.add_edge(sensor_setup, data_collection)
root.order.add_edge(data_collection, weather_check)
root.order.add_edge(data_collection, soil_testing)
root.order.add_edge(weather_check, crop_selection)
root.order.add_edge(soil_testing, crop_selection)
root.order.add_edge(crop_selection, resource_assign)
root.order.add_edge(crop_selection, community_poll)

# After selection, do the rest in parallel
root.order.add_edge(resource_assign, irrigation_adjust)
root.order.add_edge(resource_assign, nutrient_mix)
root.order.add_edge(community_poll, irrigation_adjust)
root.order.add_edge(community_poll, nutrient_mix)

# After irrigation and nutrient, do growth monitor in parallel
root.order.add_edge(irrigation_adjust, growth_monitor)
root.order.add_edge(nutrient_mix, growth_monitor)

# Then update schedule and plan harvest in parallel
root.order.add_edge(growth_monitor, schedule_update)
root.order.add_edge(growth_monitor, harvest_plan)

# After schedule and plan, do the yield report and waste sort in parallel
root.order.add_edge(schedule_update, yield_report)
root.order.add_edge(harvest_plan, yield_report)
root.order.add_edge(schedule_update, waste_sort)
root.order.add_edge(harvest_plan, waste_sort)