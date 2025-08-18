import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Create the POWL model
loop_pest = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, quality_inspect])
loop_light = OperatorPOWL(operator=Operator.LOOP, children=[light_calibration, inventory_update])
loop_energy = OperatorPOWL(operator=Operator.LOOP, children=[energy_reuse, waste_process])

xor_demand = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])
xor_order = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, skip])

xor_event = OperatorPOWL(operator=Operator.XOR, children=[community_event, skip])

xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])

xor_data = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])

root = StrictPartialOrder(nodes=[seed_selection, nutrient_setup, growth_monitoring, climate_adjust, loop_pest, loop_light, loop_energy, xor_demand, xor_order, xor_event, xor_feedback, xor_data])

# Add edges
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, climate_adjust)
root.order.add_edge(climate_adjust, loop_pest)
root.order.add_edge(loop_pest, loop_light)
root.order.add_edge(loop_light, loop_energy)
root.order.add_edge(loop_energy, xor_demand)
root.order.add_edge(xor_demand, xor_order)
root.order.add_edge(xor_order, xor_event)
root.order.add_edge(xor_event, xor_feedback)
root.order.add_edge(xor_feedback, xor_data)

print(root)