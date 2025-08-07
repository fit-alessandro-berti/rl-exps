import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
seed_selection    = Transition(label='Seed Selection')
nutrient_mix      = Transition(label='Nutrient Mix')
env_setup         = Transition(label='Environment Setup')
sensor_deploy     = Transition(label='Sensor Deployment')
growth_monitor    = Transition(label='Growth Monitoring')
pest_detection    = Transition(label='Pest Detection')
automated_harvest = Transition(label='Automated Harvest')
quality_check     = Transition(label='Quality Check')
packaging_prep    = Transition(label='Packaging Prep')
biodegradable_pack= Transition(label='Biodegradable Pack')
inventory_sync    = Transition(label='Inventory Sync')
demand_forecast   = Transition(label='Demand Forecast')
micro_fulfillment = Transition(label='Micro Fulfillment')
local_dispatch    = Transition(label='Local Dispatch')
consumer_feedback = Transition(label='Consumer Feedback')
crop_adjustment   = Transition(label='Crop Adjustment')

# Define the monitoring loop: Growth Monitoring -> Pest Detection
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_detection])

# Define the production sub‐process: Nutrient Mix -> Environment Setup -> Monitoring Loop
production_subprocess = StrictPartialOrder(nodes=[
    nutrient_mix, env_setup, monitoring_loop
])
production_subprocess.order.add_edge(nutrient_mix, env_setup)
production_subprocess.order.add_edge(env_setup, monitoring_loop)

# Define the harvesting sub‐process: Automated Harvest -> Quality Check -> Packaging Prep -> Biodegradable Pack
harvest_subprocess = StrictPartialOrder(nodes=[
    automated_harvest, quality_check, packaging_prep, biodegradable_pack
])
harvest_subprocess.order.add_edge(automated_harvest, quality_check)
harvest_subprocess.order.add_edge(quality_check, packaging_prep)
harvest_subprocess.order.add_edge(packaging_prep, biodegradable_pack)

# Define the feedback loop: Consumer Feedback -> Crop Adjustment
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback, crop_adjustment])

# Define the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    production_subprocess,
    harvest_subprocess,
    inventory_sync,
    demand_forecast,
    micro_fulfillment,
    local_dispatch,
    feedback_loop
])

# Sequence: Seed Selection -> Production Sub‐Process
root.order.add_edge(seed_selection, production_subprocess)

# Sequence: Production Sub‐Process -> Harvest Sub‐Process
root.order.add_edge(production_subprocess, harvest_subprocess)

# Sequence: Harvest Sub‐Process -> Inventory Sync
root.order.add_edge(harvest_subprocess, inventory_sync)

# Sequence: Inventory Sync -> Demand Forecast
root.order.add_edge(inventory_sync, demand_forecast)

# Sequence: Demand Forecast -> Micro Fulfillment
root.order.add_edge(demand_forecast, micro_fulfillment)

# Sequence: Micro Fulfillment -> Local Dispatch
root.order.add_edge(micro_fulfillment, local_dispatch)

# Loop: Consumer Feedback -> Crop Adjustment, repeated after each harvest
root.order.add_edge(local_dispatch, feedback_loop)