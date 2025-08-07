import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Loop for dynamic resource allocation and monitoring
resource_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[resource_assign, irrigation_adj, pest_scan, nutrient_mix]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    sensor_setup,
    data_collection,
    weather_check,
    soil_testing,
    crop_selection,
    resource_loop,
    growth_monitor,
    community_poll,
    schedule_update,
    harvest_plan,
    yield_report,
    waste_sort
])

# Sequential dependencies
root.order.add_edge(sensor_setup,     data_collection)
root.order.add_edge(data_collection,  weather_check)
root.order.add_edge(data_collection,  soil_testing)
root.order.add_edge(weather_check,    crop_selection)
root.order.add_edge(soil_testing,     crop_selection)
root.order.add_edge(crop_selection,   resource_loop)
root.order.add_edge(resource_loop,    growth_monitor)

# Concurrent after monitoring
root.order.add_edge(growth_monitor, community_poll)

# After community poll, either update schedule or harvest plan
schedule_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[schedule_update, harvest_plan]
)
root.order.add_edge(community_poll, schedule_choice)

# After either schedule update or harvest plan, generate yield report and waste sort
root.order.add_edge(schedule_choice, yield_report)
root.order.add_edge(schedule_choice, waste_sort)