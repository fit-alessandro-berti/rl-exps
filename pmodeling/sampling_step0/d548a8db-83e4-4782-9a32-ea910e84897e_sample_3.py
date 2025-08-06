from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the silent transition
skip = SilentTransition()

# Define the loops
growth_loop = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[climate_adjust, pest_control, water_recirculate, light_calibration])
harvest_loop = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[robotic_harvest, quality_inspect, waste_process, energy_reuse])
demand_loop = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[order_dispatch, community_event, feedback_collect, data_analyze])

# Define the XOR (exclusive choice) nodes
inventory_xor = OperatorPOWL(operator=OperatorPOWL.XOR, children=[inventory_update, demand_loop])
growth_xor = OperatorPOWL(operator=OperatorPOWL.XOR, children=[growth_loop, inventory_xor])

# Create the root node
root = StrictPartialOrder(nodes=[growth_xor])
root.order.add_edge(growth_xor, harvest_loop)
root.order.add_edge(growth_xor, inventory_update)
root.order.add_edge(growth_xor, demand_loop)
root.order.add_edge(harvest_loop, robotic_harvest)
root.order.add_edge(harvest_loop, quality_inspect)
root.order.add_edge(harvest_loop, waste_process)
root.order.add_edge(harvest_loop, energy_reuse)
root.order.add_edge(inventory_xor, inventory_update)
root.order.add_edge(inventory_xor, demand_loop)
root.order.add_edge(demand_loop, order_dispatch)
root.order.add_edge(demand_loop, community_event)
root.order.add_edge(demand_loop, feedback_collect)
root.order.add_edge(demand_loop, data_analyze)

print(root)