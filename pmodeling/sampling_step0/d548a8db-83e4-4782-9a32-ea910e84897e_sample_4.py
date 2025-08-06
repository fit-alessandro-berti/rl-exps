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

# Define the silent transitions
skip = SilentTransition()

# Define the loop and exclusive choice nodes
loop_growth_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, pest_control])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[water_recirculate, light_calibration])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, quality_inspect])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[waste_process, energy_reuse])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, demand_forecast])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, community_event])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, data_analyze])

# Define the root node
root = StrictPartialOrder(nodes=[loop_growth_monitoring, exclusive_choice, exclusive_choice2, exclusive_choice3, exclusive_choice4, exclusive_choice5, exclusive_choice6])
root.order.add_edge(loop_growth_monitoring, exclusive_choice)
root.order.add_edge(loop_growth_monitoring, exclusive_choice2)
root.order.add_edge(loop_growth_monitoring, exclusive_choice3)
root.order.add_edge(loop_growth_monitoring, exclusive_choice4)
root.order.add_edge(loop_growth_monitoring, exclusive_choice5)
root.order.add_edge(loop_growth_monitoring, exclusive_choice6)

# Print the root node
print(root)