from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL models for each activity
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    environment_setup,
    sensor_deployment,
    growth_monitoring,
    pest_detection,
    automated_harvest,
    quality_check,
    packaging_prep,
    biodegradable_pack,
    inventory_sync,
    demand_forecast,
    micro_fulfillment,
    local_dispatch,
    consumer_feedback,
    crop_adjustment
])

# Define the dependencies between activities
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, environment_setup)
root.order.add_edge(seed_selection, sensor_deployment)
root.order.add_edge(nutrient_mix, growth_monitoring)
root.order.add_edge(nutrient_mix, pest_detection)
root.order.add_edge(environment_setup, growth_monitoring)
root.order.add_edge(environment_setup, pest_detection)
root.order.add_edge(sensor_deployment, growth_monitoring)
root.order.add_edge(sensor_deployment, pest_detection)
root.order.add_edge(growth_monitoring, automated_harvest)
root.order.add_edge(pest_detection, automated_harvest)
root.order.add_edge(automated_harvest, quality_check)
root.order.add_edge(quality_check, packaging_prep)
root.order.add_edge(packaging_prep, biodegradable_pack)
root.order.add_edge(biodegradable_pack, inventory_sync)
root.order.add_edge(inventory_sync, demand_forecast)
root.order.add_edge(demand_forecast, micro_fulfillment)
root.order.add_edge(micro_fulfillment, local_dispatch)
root.order.add_edge(local_dispatch, consumer_feedback)
root.order.add_edge(consumer_feedback, crop_adjustment)

# Save the final result in the variable 'root'
print("POWL model for urban vertical farming supply chain generated successfully.")