import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
climate_adjust = Transition(label='Climate Adjust')
planting_robotic = Transition(label='Planting Robotic')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
water_recycle = Transition(label='Water Recycle')
light_optimize = Transition(label='Light Optimize')
growth_analyze = Transition(label='Growth Analyze')
harvest_sync = Transition(label='Harvest Sync')
sterilize_crop = Transition(label='Sterilize Crop')
package_fresh = Transition(label='Package Fresh')
demand_forecast = Transition(label='Demand Forecast')
delivery_plan = Transition(label='Delivery Plan')
data_feedback = Transition(label='Data Feedback')

# Define the process
seed_select_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seed_select, nutrient_mix])
nutrient_mix_to_climate_adjust = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, climate_adjust])
climate_adjust_to_planting_robotic = OperatorPOWL(operator=Operator.XOR, children=[climate_adjust, planting_robotic])
planting_robotic_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[planting_robotic, growth_monitor])
growth_monitor_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
pest_control_to_water_recycle = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_recycle])
water_recycle_to_light_optimize = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, light_optimize])
light_optimize_to_growth_analyze = OperatorPOWL(operator=Operator.XOR, children=[light_optimize, growth_analyze])
growth_analyze_to_harvest_sync = OperatorPOWL(operator=Operator.XOR, children=[growth_analyze, harvest_sync])
harvest_sync_to_sterilize_crop = OperatorPOWL(operator=Operator.XOR, children=[harvest_sync, sterilize_crop])
sterilize_crop_to_package_fresh = OperatorPOWL(operator=Operator.XOR, children=[sterilize_crop, package_fresh])
package_fresh_to_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[package_fresh, demand_forecast])
demand_forecast_to_delivery_plan = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, delivery_plan])
delivery_plan_to_data_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan, data_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_select_to_nutrient_mix, nutrient_mix_to_climate_adjust, climate_adjust_to_planting_robotic, planting_robotic_to_growth_monitor, growth_monitor_to_pest_control, pest_control_to_water_recycle, water_recycle_to_light_optimize, light_optimize_to_growth_analyze, growth_analyze_to_harvest_sync, harvest_sync_to_sterilize_crop, sterilize_crop_to_package_fresh, package_fresh_to_demand_forecast, demand_forecast_to_delivery_plan, delivery_plan_to_data_feedback])

# Define the dependencies
root.order.add_edge(seed_select_to_nutrient_mix, nutrient_mix_to_climate_adjust)
root.order.add_edge(nutrient_mix_to_climate_adjust, climate_adjust_to_planting_robotic)
root.order.add_edge(climate_adjust_to_planting_robotic, planting_robotic_to_growth_monitor)
root.order.add_edge(planting_robotic_to_growth_monitor, growth_monitor_to_pest_control)
root.order.add_edge(growth_monitor_to_pest_control, pest_control_to_water_recycle)
root.order.add_edge(pest_control_to_water_recycle, water_recycle_to_light_optimize)
root.order.add_edge(water_recycle_to_light_optimize, light_optimize_to_growth_analyze)
root.order.add_edge(light_optimize_to_growth_analyze, growth_analyze_to_harvest_sync)
root.order.add_edge(growth_analyze_to_harvest_sync, harvest_sync_to_sterilize_crop)
root.order.add_edge(harvest_sync_to_sterilize_crop, sterilize_crop_to_package_fresh)
root.order.add_edge(sterilize_crop_to_package_fresh, package_fresh_to_demand_forecast)
root.order.add_edge(package_fresh_to_demand_forecast, demand_forecast_to_delivery_plan)
root.order.add_edge(demand_forecast_to_delivery_plan, delivery_plan_to_data_feedback)

# Print the root
print(root)