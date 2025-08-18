from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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
skip_data_collection = SilentTransition()
skip_soil_testing = SilentTransition()
skip_pest_scan = SilentTransition()
skip_nutrient_mix = SilentTransition()
skip_waste_sort = SilentTransition()

# Define the loops and choices
data_collection_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, skip_data_collection])
soil_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, skip_soil_testing])
pest_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, skip_pest_scan])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, skip_nutrient_mix])
waste_sort_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sort, skip_waste_sort])

# Define the root model
root = StrictPartialOrder(nodes=[
    sensor_setup,
    data_collection_loop,
    weather_check,
    soil_testing_loop,
    crop_selection,
    resource_assign,
    irrigation_adjust,
    pest_scan_loop,
    nutrient_mix_loop,
    growth_monitor,
    community_poll,
    schedule_update,
    harvest_plan,
    waste_sort_loop,
    yield_report
])
root.order.add_edge(sensor_setup, data_collection_loop)
root.order.add_edge(data_collection_loop, weather_check)
root.order.add_edge(weather_check, soil_testing_loop)
root.order.add_edge(soil_testing_loop, crop_selection)
root.order.add_edge(crop_selection, resource_assign)
root.order.add_edge(resource_assign, irrigation_adjust)
root.order.add_edge(irrigation_adjust, pest_scan_loop)
root.order.add_edge(pest_scan_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, growth_monitor)
root.order.add_edge(growth_monitor, community_poll)
root.order.add_edge(community_poll, schedule_update)
root.order.add_edge(schedule_update, harvest_plan)
root.order.add_edge(harvest_plan, waste_sort_loop)
root.order.add_edge(waste_sort_loop, yield_report)