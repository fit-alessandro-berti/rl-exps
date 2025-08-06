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

# Loop for continuous environmental adjustments
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, pest_control, water_recirculate, light_calibration])

# XOR for quality inspection and waste processing
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, waste_process])

# XOR for energy reuse and inventory update
xor2 = OperatorPOWL(operator=Operator.XOR, children=[energy_reuse, inventory_update])

# XOR for demand forecast and order dispatch
xor3 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, order_dispatch])

# XOR for community event and feedback collection
xor4 = OperatorPOWL(operator=Operator.XOR, children=[community_event, feedback_collect])

# XOR for data analysis and feedback collection
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, feedback_collect])

root = StrictPartialOrder(nodes=[seed_selection, nutrient_setup, growth_monitoring, loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, feedback_collect)