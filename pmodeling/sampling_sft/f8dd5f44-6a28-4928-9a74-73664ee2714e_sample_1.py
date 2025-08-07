import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
env_setup        = Transition(label='Environment Setup')
sensor_deploy    = Transition(label='Sensor Deployment')
growth_monitor   = Transition(label='Growth Monitoring')
pest_detection   = Transition(label='Pest Detection')
auto_harvest     = Transition(label='Automated Harvest')
quality_check    = Transition(label='Quality Check')
pack_prep        = Transition(label='Packaging Prep')
biodegradable    = Transition(label='Biodegradable Pack')
inventory_sync   = Transition(label='Inventory Sync')
demand_forecast  = Transition(label='Demand Forecast')
micro_fulfill    = Transition(label='Micro Fulfillment')
local_dispatch   = Transition(label='Local Dispatch')
consumer_feedback= Transition(label='Consumer Feedback')
crop_adjustment  = Transition(label='Crop Adjustment')

# Loop for continuous monitoring and resource adjustment
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_detection]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    env_setup,
    sensor_deploy,
    monitoring_loop,
    auto_harvest,
    quality_check,
    pack_prep,
    biodegradable,
    inventory_sync,
    demand_forecast,
    micro_fulfill,
    local_dispatch,
    consumer_feedback,
    crop_adjustment
])

# Define the control-flow dependencies
root.order.add_edge(seed_selection,     nutrient_mix)
root.order.add_edge(nutrient_mix,       env_setup)
root.order.add_edge(env_setup,          sensor_deploy)
root.order.add_edge(sensor_deploy,      monitoring_loop)
root.order.add_edge(monitoring_loop,    auto_harvest)
root.order.add_edge(auto_harvest,       quality_check)
root.order.add_edge(quality_check,      pack_prep)
root.order.add_edge(pack_prep,          biodegradable)
root.order.add_edge(biodegradable,      inventory_sync)
root.order.add_edge(inventory_sync,     demand_forecast)
root.order.add_edge(demand_forecast,    micro_fulfill)
root.order.add_edge(micro_fulfill,      local_dispatch)
root.order.add_edge(local_dispatch,     consumer_feedback)
root.order.add_edge(consumer_feedback,  crop_adjustment)