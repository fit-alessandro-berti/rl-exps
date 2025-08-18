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

# Define loop and choice nodes
loop_grow = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control, growth_analyze])
xor_demand = OperatorPOWL(operator=Operator.XOR, children=[harvest_sync, demand_forecast])
loop_plan = OperatorPOWL(operator=Operator.LOOP, children=[delivery_plan, data_feedback])

# Define root partial order
root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_adjust, planting_robotic, loop_grow, xor_demand, loop_plan])
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_adjust)
root.order.add_edge(climate_adjust, planting_robotic)
root.order.add_edge(planting_robotic, loop_grow)
root.order.add_edge(loop_grow, xor_demand)
root.order.add_edge(xor_demand, loop_plan)

print(root)