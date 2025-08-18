import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Define partial order nodes
seed_cycle = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_adjust, planting_robotic, growth_monitor, pest_control, water_recycle, light_optimize, growth_analyze, harvest_sync, sterilize_crop, package_fresh])
demand_cycle = StrictPartialOrder(nodes=[demand_forecast, delivery_plan, data_feedback])

# Define loop for harvest synchronization
loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_cycle])

# Define XOR for final actions
xor = OperatorPOWL(operator=Operator.XOR, children=[loop])

# Define root
root = StrictPartialOrder(nodes=[seed_cycle, xor])
root.order.add_edge(seed_cycle, xor)