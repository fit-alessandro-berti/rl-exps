import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
tau = SilentTransition()
sensor_setup    = Transition(label='Sensor Setup')
data_collection = Transition(label='Data Collection')
weather_check   = Transition(label='Weather Check')
soil_testing    = Transition(label='Soil Testing')
crop_selection  = Transition(label='Crop Selection')
resource_assign = Transition(label='Resource Assign')
irrigation_adj  = Transition(label='Irrigation Adjust')
pest_scan       = Transition(label='Pest Scan')
nutrient_mix    = Transition(label='Nutrient Mix')
growth_monitor  = Transition(label='Growth Monitor')
community_poll  = Transition(label='Community Poll')
schedule_update = Transition(label='Schedule Update')
harvest_plan    = Transition(label='Harvest Plan')
yield_report    = Transition(label='Yield Report')
waste_sort      = Transition(label='Waste Sort')

# Build the monitoring sub-process: concurrent sensor/data collection, weather check, soil testing
monitoring = StrictPartialOrder(nodes=[
    sensor_setup, data_collection, weather_check, soil_testing
])
monitoring.order.add_edge(sensor_setup, data_collection)
monitoring.order.add_edge(data_collection, weather_check)
monitoring.order.add_edge(data_collection, soil_testing)

# Build the resource allocation sub-process: crop selection, resource assignment
resource = StrictPartialOrder(nodes=[
    crop_selection, resource_assign
])
resource.order.add_edge(crop_selection, resource_assign)

# Build the adaptive loop: concurrent monitoring, resource allocation, then optionally pest scan & nutrient mix
adaptive_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, resource])

# Build the pest & nutrient sub-process: concurrent pest scan & nutrient mix
pest_nutrient = StrictPartialOrder(nodes=[pest_scan, nutrient_mix])
pest_nutrient.order.add_edge(pest_scan, nutrient_mix)

# Build the growth monitoring sub-process: concurrent growth monitor & community poll
growth_monitoring = StrictPartialOrder(nodes=[
    growth_monitor, community_poll
])
growth_monitoring.order.add_edge(growth_monitor, community_poll)

# Build the update sub-process: schedule update & harvest plan
update = StrictPartialOrder(nodes=[schedule_update, harvest_plan])
update.order.add_edge(schedule_update, harvest_plan)

# Build the waste sorting sub-process: waste sort
waste = StrictPartialOrder(nodes=[waste_sort])

# Build the final root process: adaptive loop, pest & nutrient, growth monitoring, update, waste
root = StrictPartialOrder(nodes=[
    adaptive_loop, pest_nutrient, growth_monitoring, update, waste
])
root.order.add_edge(adaptive_loop, pest_nutrient)
root.order.add_edge(adaptive_loop, growth_monitoring)
root.order.add_edge(pest_nutrient, update)
root.order.add_edge(growth_monitoring, update)
root.order.add_edge(update, waste)

# Add a silent transition to terminate the process
root.order.add_edge(waste, tau)