import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for growth monitoring and pest control
growth_monitor_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])
water_recycle_light_optimize = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, light_optimize])
harvest_sync_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[harvest_sync, demand_forecast])
delivery_plan_data_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan, data_feedback])

# Define the root node with all the activities
root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_adjust, planting_robotic, growth_monitor_pest_control, water_recycle_light_optimize, harvest_sync_demand_forecast, sterilize_crop, package_fresh, delivery_plan_data_feedback])

# Add edges to connect the activities in the partial order
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_adjust)
root.order.add_edge(climate_adjust, planting_robotic)
root.order.add_edge(planting_robotic, growth_monitor_pest_control)
root.order.add_edge(growth_monitor_pest_control, water_recycle_light_optimize)
root.order.add_edge(water_recycle_light_optimize, harvest_sync_demand_forecast)
root.order.add_edge(harvest_sync_demand_forecast, sterilize_crop)
root.order.add_edge(sterilize_crop, package_fresh)
root.order.add_edge(package_fresh, delivery_plan_data_feedback)

print(root)