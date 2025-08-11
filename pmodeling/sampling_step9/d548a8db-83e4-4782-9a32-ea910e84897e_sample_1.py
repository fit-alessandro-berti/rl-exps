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

# Define exclusive choice for climate adjustments
xor_climate = OperatorPOWL(operator=Operator.XOR, children=[climate_adjust, skip])

# Define loop for nutrient setup
loop_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_setup, xor_climate])

# Define exclusive choice for pest control and water recirculation
xor_pest_water = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_recirculate])

# Define loop for light calibration
loop_light = OperatorPOWL(operator=Operator.LOOP, children=[light_calibration, xor_pest_water])

# Define exclusive choice for robotic harvest and quality inspection
xor_harvest_inspect = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, quality_inspect])

# Define loop for waste process and energy reuse
loop_waste_energy = OperatorPOWL(operator=Operator.LOOP, children=[waste_process, energy_reuse])

# Define exclusive choice for inventory update and demand forecast
xor_inventory_demand = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, demand_forecast])

# Define loop for order dispatch and community event
loop_order_event = OperatorPOWL(operator=Operator.LOOP, children=[order_dispatch, community_event])

# Define exclusive choice for feedback collection and data analysis
xor_feedback_data = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, data_analyze])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_nutrient, xor_climate, loop_light, xor_harvest_inspect, loop_waste_energy, xor_inventory_demand, loop_order_event, xor_feedback_data])

# Define the edges in the partial order
root.order.add_edge(loop_nutrient, xor_climate)
root.order.add_edge(xor_climate, loop_light)
root.order.add_edge(loop_light, xor_harvest_inspect)
root.order.add_edge(xor_harvest_inspect, loop_waste_energy)
root.order.add_edge(loop_waste_energy, xor_inventory_demand)
root.order.add_edge(xor_inventory_demand, loop_order_event)
root.order.add_edge(loop_order_event, xor_feedback_data)