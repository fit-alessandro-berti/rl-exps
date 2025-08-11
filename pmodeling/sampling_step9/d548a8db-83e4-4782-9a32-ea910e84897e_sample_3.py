import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop nodes
water_recirculate_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_recirculate])
energy_reuse_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_reuse])
inventory_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update])
demand_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast])

# Define choice nodes
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
light_calibration_choice = OperatorPOWL(operator=Operator.XOR, children=[light_calibration, skip])
inventory_update_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip])
demand_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])

# Define partial order
root = StrictPartialOrder(nodes=[seed_selection, nutrient_setup, growth_monitoring, climate_adjust, pest_control_choice, light_calibration_choice, robotic_harvest, quality_inspect, waste_process, energy_reuse_loop, inventory_update_loop, demand_forecast_loop, order_dispatch, community_event, feedback_collect, data_analyze])
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, climate_adjust)
root.order.add_edge(climate_adjust, pest_control_choice)
root.order.add_edge(climate_adjust, light_calibration_choice)
root.order.add_edge(pest_control_choice, robotic_harvest)
root.order.add_edge(pest_control_choice, quality_inspect)
root.order.add_edge(pest_control_choice, waste_process)
root.order.add_edge(light_calibration_choice, robotic_harvest)
root.order.add_edge(light_calibration_choice, quality_inspect)
root.order.add_edge(light_calibration_choice, waste_process)
root.order.add_edge(robotic_harvest, energy_reuse_loop)
root.order.add_edge(quality_inspect, inventory_update_choice)
root.order.add_edge(waste_process, inventory_update_choice)
root.order.add_edge(inventory_update_choice, inventory_update_loop)
root.order.add_edge(inventory_update_loop, order_dispatch)
root.order.add_edge(order_dispatch, community_event)
root.order.add_edge(community_event, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)

print(root)