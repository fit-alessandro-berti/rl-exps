from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow
seed_select_next = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, climate_adjust])
climate_adjust_next = OperatorPOWL(operator=Operator.XOR, children=[planting_robotic, growth_monitor])
growth_monitor_next = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_recycle])
pest_control_next = OperatorPOWL(operator=Operator.XOR, children=[light_optimize, growth_analyze])
light_optimize_next = OperatorPOWL(operator=Operator.XOR, children=[harvest_sync, sterilize_crop])
harvest_sync_next = OperatorPOWL(operator=Operator.XOR, children=[package_fresh, demand_forecast])
demand_forecast_next = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan, data_feedback])

root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_adjust, planting_robotic, growth_monitor, pest_control, water_recycle, light_optimize, growth_analyze, harvest_sync, sterilize_crop, package_fresh, demand_forecast, delivery_plan, data_feedback])
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_adjust)
root.order.add_edge(climate_adjust, planting_robotic)
root.order.add_edge(planting_robotic, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, water_recycle)
root.order.add_edge(water_recycle, light_optimize)
root.order.add_edge(light_optimize, harvest_sync)
root.order.add_edge(harvest_sync, sterilize_crop)
root.order.add_edge(sterilize_crop, package_fresh)
root.order.add_edge(package_fresh, demand_forecast)
root.order.add_edge(demand_forecast, delivery_plan)
root.order.add_edge(delivery_plan, data_feedback)

# Print the POWL model
print(root)