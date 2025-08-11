import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
sensor_deployment = Transition(label='Sensor Deployment')
growth_monitoring = Transition(label='Growth Monitoring')
pest_detection = Transition(label='Pest Detection')
automated_harvest = Transition(label='Automated Harvest')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
biodegradable_pack = Transition(label='Biodegradable Pack')
inventory_sync = Transition(label='Inventory Sync')
demand_forecast = Transition(label='Demand Forecast')
micro_fulfillment = Transition(label='Micro Fulfillment')
local_dispatch = Transition(label='Local Dispatch')
consumer_feedback = Transition(label='Consumer Feedback')
crop_adjustment = Transition(label='Crop Adjustment')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix, environment_setup, sensor_deployment, growth_monitoring, pest_detection])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[automated_harvest, quality_check, packaging_prep, biodegradable_pack])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, demand_forecast])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[micro_fulfillment, local_dispatch])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback, crop_adjustment])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4, loop_5])

# Add edges between nodes
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, loop_5)

# Print the root model
print(root)