import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
seed_selection = Transition(label='Seed Selection')
nutrient_setup = Transition(label='Nutrient Setup')
growth_monitoring = Transition(label='Growth Monitoring')
climate_adjust = Transition(label='Climate Adjust')
pest_control = Transition(label='Pest Control')
water_recirculate = Transition(label='Water Recirculate')
light_calibration = Transition(label='Light Calibration')
robotic_harvest = Transition(label='Robotic Harvest')
quality_inspect = Transition(label='Quality Inspect')
waste_process = Transition(label='Waste Process')
energy_reuse = Transition(label='Energy Reuse')
inventory_update = Transition(label='Inventory Update')
demand_forecast = Transition(label='Demand Forecast')
order_dispatch = Transition(label='Order Dispatch')
community_event = Transition(label='Community Event')
feedback_collect = Transition(label='Feedback Collect')
data_analyze = Transition(label='Data Analyze')

# Define the loop for continuous environmental adjustments
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, pest_control, water_recirculate, light_calibration])

# Define the exclusive choice for quality inspection and waste processing
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, waste_process])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection, nutrient_setup, growth_monitoring, loop, xor, inventory_update, demand_forecast, order_dispatch, community_event, feedback_collect, data_analyze])

# Add edges to define the dependencies
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, inventory_update)
root.order.add_edge(inventory_update, demand_forecast)
root.order.add_edge(demand_forecast, order_dispatch)
root.order.add_edge(order_dispatch, community_event)
root.order.add_edge(community_event, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)

print(root)