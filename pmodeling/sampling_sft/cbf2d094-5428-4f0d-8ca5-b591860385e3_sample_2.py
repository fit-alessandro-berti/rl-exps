import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_select    = Transition(label='Seed Select')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_adjust = Transition(label='Climate Adjust')
planting_robot = Transition(label='Planting Robotic')
growth_monitor = Transition(label='Growth Monitor')
pest_control   = Transition(label='Pest Control')
water_recycle  = Transition(label='Water Recycle')
light_optimize = Transition(label='Light Optimize')
growth_analyze = Transition(label='Growth Analyze')
harvest_sync   = Transition(label='Harvest Sync')
sterilize_crop = Transition(label='Sterilize Crop')
package_fresh  = Transition(label='Package Fresh')
demand_forecast= Transition(label='Demand Forecast')
delivery_plan  = Transition(label='Delivery Plan')
data_feedback  = Transition(label='Data Feedback')

# Loop for continuous growth monitoring
loop_growth = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control, water_recycle, light_optimize, growth_analyze]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, climate_adjust, planting_robot,
    loop_growth,
    harvest_sync, sterilize_crop, package_fresh,
    demand_forecast, delivery_plan, data_feedback
])

# Define the control-flow dependencies
root.order.add_edge(seed_select,     nutrient_mix)
root.order.add_edge(nutrient_mix,    climate_adjust)
root.order.add_edge(climate_adjust,  planting_robot)
root.order.add_edge(planting_robot,  loop_growth)

# Harvest and packaging must happen after growth analysis
root.order.add_edge(loop_growth, harvest_sync)
root.order.add_edge(loop_growth, sterilize_crop)
root.order.add_edge(harvest_sync, package_fresh)

# Demand forecast and delivery plan must happen concurrently after harvest
root.order.add_edge(harvest_sync, demand_forecast)
root.order.add_edge(harvest_sync, delivery_plan)

# Data feedback loop should follow the harvest‐packaging‐demand‐delivery cycle
root.order.add_edge(harvest_sync, data_feedback)
root.order.add_edge(sterilize_crop, data_feedback)
root.order.add_edge(package_fresh, data_feedback)
root.order.add_edge(demand_forecast, data_feedback)
root.order.add_edge(delivery_plan, data_feedback)