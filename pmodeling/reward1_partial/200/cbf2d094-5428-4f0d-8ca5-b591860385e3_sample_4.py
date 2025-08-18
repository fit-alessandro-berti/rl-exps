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

# Define sub-processes
climate_control = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, nutrient_mix])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, water_recycle, light_optimize])
growth_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control_loop, growth_analyze])
harvest_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_sync, demand_forecast, delivery_plan])
post_harvest = OperatorPOWL(operator=Operator.LOOP, children=[sterilize_crop, package_fresh, data_feedback])

# Define the main process
root = StrictPartialOrder(nodes=[climate_control, planting_robotic, growth_monitoring, harvest_sync_loop, post_harvest])
root.order.add_edge(climate_control, planting_robotic)
root.order.add_edge(planting_robotic, growth_monitoring)
root.order.add_edge(growth_monitoring, harvest_sync_loop)
root.order.add_edge(harvest_sync_loop, post_harvest)