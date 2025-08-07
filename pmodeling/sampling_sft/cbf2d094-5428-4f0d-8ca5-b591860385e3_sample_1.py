import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select   = Transition(label='Seed Select')
nutrient_mix  = Transition(label='Nutrient Mix')
climate_adj   = Transition(label='Climate Adjust')
planting      = Transition(label='Planting Robotic')
growth_monitor= Transition(label='Growth Monitor')
pest_control  = Transition(label='Pest Control')
water_recycle = Transition(label='Water Recycle')
light_opt     = Transition(label='Light Optimize')
growth_analyze= Transition(label='Growth Analyze')
harvest_sync  = Transition(label='Harvest Sync')
sterilize     = Transition(label='Sterilize Crop')
package       = Transition(label='Package Fresh')
demand_fore   = Transition(label='Demand Forecast')
delivery      = Transition(label='Delivery Plan')
data_feedback = Transition(label='Data Feedback')

# Loop for continuous growth monitoring and adjustments
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control, water_recycle, light_opt, growth_analyze]
)

# Exclusive choice between harvest and feedback
harvest_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[harvest_sync, data_feedback]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, climate_adj, planting,
    growth_loop, demand_fore, harvest_choice,
    sterilize, package, delivery
])

# Define the control‐flow dependencies
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_adj)
root.order.add_edge(climate_adj, planting)
root.order.add_edge(planting, growth_loop)

# After growth loop, either harvest or do data feedback
root.order.add_edge(growth_loop, demand_fore)
root.order.add_edge(demand_fore, harvest_choice)

# Harvest or feedback then do sterilize, package, and delivery
for next_activity in [sterilize, package, delivery]:
    root.order.add_edge(harvest_choice, next_activity)

# No other dependencies, so all nodes are concurrent at the end