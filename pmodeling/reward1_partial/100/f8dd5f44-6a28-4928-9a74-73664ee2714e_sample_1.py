import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define exclusive choice operators for decision-making processes
seed_selection_or_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
environment_setup_or_sensor_deployment = OperatorPOWL(operator=Operator.XOR, children=[environment_setup, sensor_deployment])
growth_monitoring_or_pest_detection = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_detection])
quality_check_or_biodegradable_pack = OperatorPOWL(operator=Operator.XOR, children=[quality_check, biodegradable_pack])
inventory_sync_or_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, demand_forecast])
micro_fulfillment_or_local_dispatch = OperatorPOWL(operator=Operator.XOR, children=[micro_fulfillment, local_dispatch])

# Define loop for feedback loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback, crop_adjustment])

# Define partial order structure
root = StrictPartialOrder(nodes=[seed_selection_or_nutrient_mix, environment_setup_or_sensor_deployment, growth_monitoring_or_pest_detection, automated_harvest, quality_check_or_biodegradable_pack, inventory_sync_or_demand_forecast, micro_fulfillment_or_local_dispatch, feedback_loop])
root.order.add_edge(seed_selection_or_nutrient_mix, environment_setup_or_sensor_deployment)
root.order.add_edge(environment_setup_or_sensor_deployment, growth_monitoring_or_pest_detection)
root.order.add_edge(growth_monitoring_or_pest_detection, automated_harvest)
root.order.add_edge(automated_harvest, quality_check_or_biodegradable_pack)
root.order.add_edge(quality_check_or_biodegradable_pack, inventory_sync_or_demand_forecast)
root.order.add_edge(inventory_sync_or_demand_forecast, micro_fulfillment_or_local_dispatch)
root.order.add_edge(micro_fulfillment_or_local_dispatch, feedback_loop)
root.order.add_edge(feedback_loop, consumer_feedback)