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

# Define partial order and loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_setup, growth_monitoring, climate_adjust, pest_control, water_recirculate, light_calibration])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[robotic_harvest, quality_inspect, waste_process, energy_reuse])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, demand_forecast, order_dispatch, community_event, feedback_collect, data_analyze])

# Define XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])

# Define root node
root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, xor2)

print(root)