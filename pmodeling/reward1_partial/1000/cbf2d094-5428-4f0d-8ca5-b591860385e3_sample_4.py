import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop nodes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, nutrient_mix])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, water_recycle, light_optimize, growth_analyze])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_sync, demand_forecast, delivery_plan, data_feedback])

# Define partial order model
root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_loop, planting_robotic, growth_monitor, pest_loop, sterilize_crop, package_fresh, harvest_loop])
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_loop)
root.order.add_edge(climate_loop, planting_robotic)
root.order.add_edge(planting_robotic, growth_monitor)
root.order.add_edge(growth_monitor, pest_loop)
root.order.add_edge(pest_loop, sterilize_crop)
root.order.add_edge(sterilize_crop, package_fresh)
root.order.add_edge(package_fresh, harvest_loop)
root.order.add_edge(harvest_loop, demand_forecast)
root.order.add_edge(demand_forecast, delivery_plan)
root.order.add_edge(delivery_plan, data_feedback)