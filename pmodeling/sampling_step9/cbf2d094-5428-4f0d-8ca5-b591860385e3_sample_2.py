import pm4py
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
skip = SilentTransition()

# Define the partial order
climate_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
growth_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_analyze])
harvest_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_sync])
sterilize_crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[sterilize_crop])
package_fresh_loop = OperatorPOWL(operator=Operator.LOOP, children=[package_fresh])
data_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_feedback])
demand_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast])
delivery_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[delivery_plan])

# Define the exclusive choices
climate_adjust_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_adjust_loop, skip])
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix_loop, skip])
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control_loop, skip])
growth_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_analyze_loop, skip])
harvest_sync_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_sync_loop, skip])
sterilize_crop_xor = OperatorPOWL(operator=Operator.XOR, children=[sterilize_crop_loop, skip])
package_fresh_xor = OperatorPOWL(operator=Operator.XOR, children=[package_fresh_loop, skip])
data_feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[data_feedback_loop, skip])
demand_forecast_xor = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast_loop, skip])
delivery_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan_loop, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[climate_adjust_xor, nutrient_mix_xor, pest_control_xor, growth_analyze_xor, harvest_sync_xor, sterilize_crop_xor, package_fresh_xor, data_feedback_xor, demand_forecast_xor, delivery_plan_xor])

# Define the order dependencies
root.order.add_edge(climate_adjust_xor, nutrient_mix_xor)
root.order.add_edge(climate_adjust_xor, pest_control_xor)
root.order.add_edge(climate_adjust_xor, growth_analyze_xor)
root.order.add_edge(climate_adjust_xor, harvest_sync_xor)
root.order.add_edge(climate_adjust_xor, sterilize_crop_xor)
root.order.add_edge(climate_adjust_xor, package_fresh_xor)
root.order.add_edge(climate_adjust_xor, data_feedback_xor)
root.order.add_edge(climate_adjust_xor, demand_forecast_xor)
root.order.add_edge(climate_adjust_xor, delivery_plan_xor)

root.order.add_edge(nutrient_mix_xor, pest_control_xor)
root.order.add_edge(nutrient_mix_xor, growth_analyze_xor)
root.order.add_edge(nutrient_mix_xor, harvest_sync_xor)
root.order.add_edge(nutrient_mix_xor, sterilize_crop_xor)
root.order.add_edge(nutrient_mix_xor, package_fresh_xor)
root.order.add_edge(nutrient_mix_xor, data_feedback_xor)
root.order.add_edge(nutrient_mix_xor, demand_forecast_xor)
root.order.add_edge(nutrient_mix_xor, delivery_plan_xor)

root.order.add_edge(pest_control_xor, growth_analyze_xor)
root.order.add_edge(pest_control_xor, harvest_sync_xor)
root.order.add_edge(pest_control_xor, sterilize_crop_xor)
root.order.add_edge(pest_control_xor, package_fresh_xor)
root.order.add_edge(pest_control_xor, data_feedback_xor)
root.order.add_edge(pest_control_xor, demand_forecast_xor)
root.order.add_edge(pest_control_xor, delivery_plan_xor)

root.order.add_edge(growth_analyze_xor, harvest_sync_xor)
root.order.add_edge(growth_analyze_xor, sterilize_crop_xor)
root.order.add_edge(growth_analyze_xor, package_fresh_xor)
root.order.add_edge(growth_analyze_xor, data_feedback_xor)
root.order.add_edge(growth_analyze_xor, demand_forecast_xor)
root.order.add_edge(growth_analyze_xor, delivery_plan_xor)

root.order.add_edge(harvest_sync_xor, sterilize_crop_xor)
root.order.add_edge(harvest_sync_xor, package_fresh_xor)
root.order.add_edge(harvest_sync_xor, data_feedback_xor)
root.order.add_edge(harvest_sync_xor, demand_forecast_xor)
root.order.add_edge(harvest_sync_xor, delivery_plan_xor)

root.order.add_edge(sterilize_crop_xor, package_fresh_xor)
root.order.add_edge(sterilize_crop_xor, data_feedback_xor)
root.order.add_edge(sterilize_crop_xor, demand_forecast_xor)
root.order.add_edge(sterilize_crop_xor, delivery_plan_xor)

root.order.add_edge(package_fresh_xor, data_feedback_xor)
root.order.add_edge(package_fresh_xor, demand_forecast_xor)
root.order.add_edge(package_fresh_xor, delivery_plan_xor)

root.order.add_edge(data_feedback_xor, demand_forecast_xor)
root.order.add_edge(data_feedback_xor, delivery_plan_xor)

root.order.add_edge(demand_forecast_xor, delivery_plan_xor)