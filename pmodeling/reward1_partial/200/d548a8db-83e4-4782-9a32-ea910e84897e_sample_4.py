from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder()

# Define the transitions (activities)
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[water_recirculate, light_calibration])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, climate_adjust])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, inventory_update])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, community_event])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, data_analyze])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_setup])

# Connect the POWL model
root.nodes = [loop, xor1, xor2, xor3, xor4, xor5]
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Return the root of the POWL model
return root