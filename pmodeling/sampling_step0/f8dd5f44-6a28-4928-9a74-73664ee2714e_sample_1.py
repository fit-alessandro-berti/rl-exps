import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow
seed_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, environment_setup])
environment_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[environment_setup, sensor_deployment])
sensor_deployment_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_deployment, growth_monitoring])
growth_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_detection])
pest_detection_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, automated_harvest])
automated_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[automated_harvest, quality_check])
quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_check, packaging_prep])
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, biodegradable_pack])
biodegradable_pack_choice = OperatorPOWL(operator=Operator.XOR, children=[biodegradable_pack, inventory_sync])
inventory_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, demand_forecast])
demand_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, micro_fulfillment])
micro_fulfillment_choice = OperatorPOWL(operator=Operator.XOR, children=[micro_fulfillment, local_dispatch])
local_dispatch_choice = OperatorPOWL(operator=Operator.XOR, children=[local_dispatch, consumer_feedback])
consumer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[consumer_feedback, crop_adjustment])
crop_adjustment_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_adjustment, seed_selection])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection_choice, nutrient_mix_choice, environment_setup_choice, sensor_deployment_choice, growth_monitoring_choice, pest_detection_choice, automated_harvest_choice, quality_check_choice, packaging_prep_choice, biodegradable_pack_choice, inventory_sync_choice, demand_forecast_choice, micro_fulfillment_choice, local_dispatch_choice, consumer_feedback_choice, crop_adjustment_choice])

# Add dependencies
root.order.add_edge(seed_selection_choice, nutrient_mix_choice)
root.order.add_edge(nutrient_mix_choice, environment_setup_choice)
root.order.add_edge(environment_setup_choice, sensor_deployment_choice)
root.order.add_edge(sensor_deployment_choice, growth_monitoring_choice)
root.order.add_edge(growth_monitoring_choice, pest_detection_choice)
root.order.add_edge(pest_detection_choice, automated_harvest_choice)
root.order.add_edge(automated_harvest_choice, quality_check_choice)
root.order.add_edge(quality_check_choice, packaging_prep_choice)
root.order.add_edge(packaging_prep_choice, biodegradable_pack_choice)
root.order.add_edge(biodegradable_pack_choice, inventory_sync_choice)
root.order.add_edge(inventory_sync_choice, demand_forecast_choice)
root.order.add_edge(demand_forecast_choice, micro_fulfillment_choice)
root.order.add_edge(micro_fulfillment_choice, local_dispatch_choice)
root.order.add_edge(local_dispatch_choice, consumer_feedback_choice)
root.order.add_edge(consumer_feedback_choice, crop_adjustment_choice)

# Print the root POWL model
print(root)