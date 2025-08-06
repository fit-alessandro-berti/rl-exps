import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_setup, growth_monitoring, climate_adjust, pest_control, water_recirculate, light_calibration, robotic_harvest, quality_inspect])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[waste_process, energy_reuse])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, demand_forecast, order_dispatch, community_event, feedback_collect, data_analyze])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3])

# Define the dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

# Print the result
print(root)