import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the process structure
# A loop node (* (A, B)): execute A, then choose to exit or execute B then A again, repeated until exit.
water_recirculate_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_recirculate, waste_process])
energy_reuse_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_reuse, inventory_update])

# Define the partial order
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_setup, growth_monitoring, climate_adjust, pest_control, 
    water_recirculate_loop, light_calibration, robotic_harvest, quality_inspect, 
    demand_forecast, order_dispatch, community_event, feedback_collect, data_analyze
])

# Define the order dependencies
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, climate_adjust)
root.order.add_edge(climate_adjust, pest_control)
root.order.add_edge(pest_control, water_recirculate_loop)
root.order.add_edge(water_recirculate_loop, light_calibration)
root.order.add_edge(light_calibration, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_inspect)
root.order.add_edge(quality_inspect, demand_forecast)
root.order.add_edge(demand_forecast, order_dispatch)
root.order.add_edge(order_dispatch, community_event)
root.order.add_edge(community_event, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)

# Print the root to see the complete process
print(root)