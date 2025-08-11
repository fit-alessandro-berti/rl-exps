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
xor = OperatorPOWL(operator=Operator.XOR, children=[sterilize_crop, skip])

loop = OperatorPOWL(operator=Operator.LOOP, children=[light_optimize, climate_adjust])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])

loop2 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_sync, demand_forecast])

loop3 = OperatorPOWL(operator=Operator.LOOP, children=[growth_analyze, data_feedback])

root = StrictPartialOrder(nodes=[loop, loop2, loop3, xor2, xor, planting_robotic, growth_monitor, nutrient_mix, seed_select])
root.order.add_edge(loop, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor, planting_robotic)
root.order.add_edge(xor2, growth_monitor)
root.order.add_edge(planting_robotic, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_select)