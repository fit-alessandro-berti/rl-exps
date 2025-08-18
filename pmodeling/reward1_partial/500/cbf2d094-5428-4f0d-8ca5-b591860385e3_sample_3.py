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

# Define loop and choice nodes
climate_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, SilentTransition()])

# Define partial order and add dependencies
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_mix,
    climate_adjust_loop,
    planting_robotic,
    growth_monitor,
    pest_control_choice,
    water_recycle,
    light_optimize,
    growth_analyze,
    harvest_sync,
    sterilize_crop,
    package_fresh,
    demand_forecast,
    delivery_plan,
    data_feedback
])
root.order.add_edge(climate_adjust_loop, planting_robotic)
root.order.add_edge(climate_adjust_loop, growth_monitor)
root.order.add_edge(climate_adjust_loop, water_recycle)
root.order.add_edge(climate_adjust_loop, light_optimize)
root.order.add_edge(climate_adjust_loop, growth_analyze)
root.order.add_edge(climate_adjust_loop, harvest_sync)
root.order.add_edge(climate_adjust_loop, sterilize_crop)
root.order.add_edge(climate_adjust_loop, package_fresh)
root.order.add_edge(climate_adjust_loop, demand_forecast)
root.order.add_edge(climate_adjust_loop, delivery_plan)
root.order.add_edge(climate_adjust_loop, data_feedback)
root.order.add_edge(pest_control_choice, harvest_sync)
root.order.add_edge(pest_control_choice, demand_forecast)
root.order.add_edge(pest_control_choice, delivery_plan)
root.order.add_edge(pest_control_choice, data_feedback)