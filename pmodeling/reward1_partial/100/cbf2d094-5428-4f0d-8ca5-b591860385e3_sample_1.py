import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, nutrient_mix])
planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_robotic, growth_monitor])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, water_recycle, light_optimize])
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_analyze, harvest_sync])
delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[delivery_plan, demand_forecast, data_feedback])

root = StrictPartialOrder(nodes=[climate_loop, planting_loop, pest_loop, growth_loop, delivery_loop])
root.order.add_edge(climate_loop, planting_loop)
root.order.add_edge(planting_loop, growth_loop)
root.order.add_edge(growth_loop, delivery_loop)
root.order.add_edge(delivery_loop, climate_loop)

print(root)