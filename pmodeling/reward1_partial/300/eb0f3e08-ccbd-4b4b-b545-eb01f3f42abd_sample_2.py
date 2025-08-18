import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[sensor_setup, data_collection, weather_check, soil_testing, crop_selection, resource_assign, irrigation_adjust, pest_scan, nutrient_mix, growth_monitor, community_poll, schedule_update, harvest_plan, waste_sort, yield_report])

# Define the control-flow operators
data_collection_after_sensor_setup = OperatorPOWL(operator=Operator.XOR, children=[data_collection, sensor_setup])
weather_check_after_data_collection = OperatorPOWL(operator=Operator.XOR, children=[weather_check, data_collection])
soil_testing_after_weather_check = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, weather_check])
crop_selection_after_soil_testing = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, soil_testing])
resource_assign_after_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[resource_assign, crop_selection])
irrigation_adjust_after_resource_assign = OperatorPOWL(operator=Operator.XOR, children=[irrigation_adjust, resource_assign])
pest_scan_after_irrigation_adjust = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, irrigation_adjust])
nutrient_mix_after_pest_scan = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_scan])
growth_monitor_after_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, nutrient_mix])
community_poll_after_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[community_poll, growth_monitor])
schedule_update_after_community_poll = OperatorPOWL(operator=Operator.XOR, children=[schedule_update, community_poll])
harvest_plan_after_schedule_update = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, schedule_update])
waste_sort_after_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[waste_sort, harvest_plan])
yield_report_after_waste_sort = OperatorPOWL(operator=Operator.XOR, children=[yield_report, waste_sort])

# Connect the nodes in the POWL model
root.order.add_edge(sensor_setup, data_collection_after_sensor_setup)
root.order.add_edge(data_collection_after_sensor_setup, weather_check_after_data_collection)
root.order.add_edge(weather_check_after_data_collection, soil_testing_after_weather_check)
root.order.add_edge(soil_testing_after_weather_check, crop_selection_after_soil_testing)
root.order.add_edge(crop_selection_after_soil_testing, resource_assign_after_crop_selection)
root.order.add_edge(resource_assign_after_crop_selection, irrigation_adjust_after_resource_assign)
root.order.add_edge(irrigation_adjust_after_resource_assign, pest_scan_after_irrigation_adjust)
root.order.add_edge(pest_scan_after_irrigation_adjust, nutrient_mix_after_pest_scan)
root.order.add_edge(nutrient_mix_after_pest_scan, growth_monitor_after_nutrient_mix)
root.order.add_edge(growth_monitor_after_nutrient_mix, community_poll_after_growth_monitor)
root.order.add_edge(community_poll_after_growth_monitor, schedule_update_after_community_poll)
root.order.add_edge(schedule_update_after_community_poll, harvest_plan_after_schedule_update)
root.order.add_edge(harvest_plan_after_schedule_update, waste_sort_after_harvest_plan)
root.order.add_edge(waste_sort_after_harvest_plan, yield_report_after_waste_sort)

# Print the POWL model
print(root)