import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions in the POWL model
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, climate_adjust])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, light_optimize])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[growth_analyze, data_feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, delivery_plan])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, nutrient_mix, xor1, xor2, xor3, xor4])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, planting_robotic, harvest_sync, sterilize_crop, package_fresh])

# Add dependencies between the nodes
root.order.add_edge(loop, planting_robotic)
root.order.add_edge(planting_robotic, harvest_sync)
root.order.add_edge(harvest_sync, sterilize_crop)
root.order.add_edge(sterilize_crop, package_fresh)
root.order.add_edge(planting_robotic, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, harvest_sync)
root.order.add_edge(planting_robotic, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_select)