import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, automated_harvest, quality_check])
loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, biodegradable_pack, inventory_sync, demand_forecast])
partial_order = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup, sensor_deployment, growth_monitoring, exclusive_choice, loop, micro_fulfillment, local_dispatch, consumer_feedback, crop_adjustment])
partial_order.order.add_edge(seed_selection, nutrient_mix)
partial_order.order.add_edge(nutrient_mix, environment_setup)
partial_order.order.add_edge(environment_setup, sensor_deployment)
partial_order.order.add_edge(sensor_deployment, growth_monitoring)
partial_order.order.add_edge(growth_monitoring, exclusive_choice)
partial_order.order.add_edge(exclusive_choice, packaging_prep)
partial_order.order.add_edge(packaging_prep, biodegradable_pack)
partial_order.order.add_edge(biodegradable_pack, inventory_sync)
partial_order.order.add_edge(inventory_sync, demand_forecast)
partial_order.order.add_edge(demand_forecast, micro_fulfillment)
partial_order.order.add_edge(micro_fulfillment, local_dispatch)
partial_order.order.add_edge(local_dispatch, consumer_feedback)
partial_order.order.add_edge(consumer_feedback, crop_adjustment)

# Save the final result in the variable 'root'
root = partial_order