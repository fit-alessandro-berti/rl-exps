import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select   = Transition(label='Seed Select')
nutrient_mix  = Transition(label='Nutrient Mix')
climate_adjust= Transition(label='Climate Adjust')
planting_robotic = Transition(label='Planting Robotic')
growth_monitor= Transition(label='Growth Monitor')
pest_control  = Transition(label='Pest Control')
water_recycle = Transition(label='Water Recycle')
light_optimize= Transition(label='Light Optimize')
growth_analyze= Transition(label='Growth Analyze')
demand_forecast= Transition(label='Demand Forecast')
harvest_sync  = Transition(label='Harvest Sync')
sterilize_crop= Transition(label='Sterilize Crop')
package_fresh = Transition(label='Package Fresh')
delivery_plan = Transition(label='Delivery Plan')
data_feedback = Transition(label='Data Feedback')

# Define the loop body (monitoring and control adjustments)
body = StrictPartialOrder(nodes=[
    growth_monitor,
    pest_control,
    water_recycle,
    light_optimize,
    growth_analyze
])
body.order.add_edge(growth_monitor, pest_control)
body.order.add_edge(pest_control, water_recycle)
body.order.add_edge(water_recycle, light_optimize)
body.order.add_edge(light_optimize, growth_analyze)

# Loop: repeat monitoring/control until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, data_feedback])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_mix,
    climate_adjust,
    planting_robotic,
    loop,
    demand_forecast,
    harvest_sync,
    sterilize_crop,
    package_fresh,
    delivery_plan
])

# Sequence edges
root.order.add_edge(seed_select,   nutrient_mix)
root.order.add_edge(nutrient_mix,  climate_adjust)
root.order.add_edge(climate_adjust, planting_robotic)
root.order.add_edge(planting_robotic, loop)
root.order.add_edge(loop, demand_forecast)
root.order.add_edge(demand_forecast, harvest_sync)
root.order.add_edge(harvest_sync, sterilize_crop)
root.order.add_edge(sterilize_crop, package_fresh)
root.order.add_edge(package_fresh, delivery_plan)