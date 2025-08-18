import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban vertical farming supply chain process
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

# Define the POWL operators for the process
sensor_deployment_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deployment])
pest_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detection])
growth_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring])
quality_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check])
packaging_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])
biodegradable_pack_loop = OperatorPOWL(operator=Operator.LOOP, children=[biodegradable_pack])
inventory_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync])
demand_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast])
micro_fulfillment_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_fulfillment])
local_dispatch_loop = OperatorPOWL(operator=Operator.LOOP, children=[local_dispatch])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup, sensor_deployment_loop, pest_detection_loop, growth_monitoring_loop, quality_check_loop, packaging_prep_loop, biodegradable_pack_loop, inventory_sync_loop, demand_forecast_loop, micro_fulfillment_loop, local_dispatch_loop, consumer_feedback, crop_adjustment])

# Add edges to define the partial order
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, environment_setup)
root.order.add_edge(environment_setup, sensor_deployment_loop)
root.order.add_edge(sensor_deployment_loop, pest_detection_loop)
root.order.add_edge(pest_detection_loop, growth_monitoring_loop)
root.order.add_edge(growth_monitoring_loop, quality_check_loop)
root.order.add_edge(quality_check_loop, packaging_prep_loop)
root.order.add_edge(packaging_prep_loop, biodegradable_pack_loop)
root.order.add_edge(biodegradable_pack_loop, inventory_sync_loop)
root.order.add_edge(inventory_sync_loop, demand_forecast_loop)
root.order.add_edge(demand_forecast_loop, micro_fulfillment_loop)
root.order.add_edge(micro_fulfillment_loop, local_dispatch_loop)
root.order.add_edge(local_dispatch_loop, consumer_feedback)
root.order.add_edge(consumer_feedback, crop_adjustment)

print(root)