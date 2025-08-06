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

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, pest_control, water_recirculate])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[light_calibration, robotic_harvest, quality_inspect])

# Define the exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, demand_forecast])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, community_event])

# Define the root POWL model
root = StrictPartialOrder(nodes=[seed_selection, nutrient_setup, growth_monitoring, xor1, xor2, loop1, loop2])
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, order_dispatch)
root.order.add_edge(xor2, community_event)

print(root)