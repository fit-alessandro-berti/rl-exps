import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the root Partial Order
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_mix,
    climate_adjust,
    planting_robotic,
    growth_monitor,
    pest_control,
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

# Since there are no explicit dependencies given, we assume all activities are concurrent
# If there were dependencies, they would be added using root.order.add_edge(source, target)

print(root)