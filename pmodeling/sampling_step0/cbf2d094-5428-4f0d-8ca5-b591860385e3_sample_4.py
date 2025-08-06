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

# Define silent transitions
skip = SilentTransition()

# Define the loop for nutrient mix and climate adjust
loop_nutrient_climate = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, climate_adjust])

# Define the XOR for growth monitor and pest control
xor_growth_pest = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])

# Define the XOR for water recycle and light optimize
xor_water_light = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, light_optimize])

# Define the loop for growth analyze and sterilize crop
loop_growth_sterilize = OperatorPOWL(operator=Operator.LOOP, children=[growth_analyze, sterilize_crop])

# Define the XOR for harvest sync and package fresh
xor_harvest_package = OperatorPOWL(operator=Operator.XOR, children=[harvest_sync, package_fresh])

# Define the loop for demand forecast and delivery plan
loop_demand_delivery = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, delivery_plan])

# Define the XOR for data feedback and skip
xor_data_skip = OperatorPOWL(operator=Operator.XOR, children=[data_feedback, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_nutrient_climate, xor_growth_pest, xor_water_light, loop_growth_sterilize, xor_harvest_package, loop_demand_delivery, xor_data_skip])
root.order.add_edge(loop_nutrient_climate, xor_growth_pest)
root.order.add_edge(xor_growth_pest, xor_water_light)
root.order.add_edge(xor_water_light, loop_growth_sterilize)
root.order.add_edge(loop_growth_sterilize, xor_harvest_package)
root.order.add_edge(xor_harvest_package, loop_demand_delivery)
root.order.add_edge(loop_demand_delivery, xor_data_skip)

print(root)