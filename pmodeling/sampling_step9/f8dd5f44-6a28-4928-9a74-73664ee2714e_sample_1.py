import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, pest_detection])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[automated_harvest, quality_check, packaging_prep])
dispatch_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, demand_forecast, micro_fulfillment, local_dispatch])

# Define XOR nodes
sensor_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_deployment, skip])
monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_loop, harvest_loop])
dispatch_xor = OperatorPOWL(operator=Operator.XOR, children=[dispatch_loop, consumer_feedback])

# Define the root node
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup, sensor_xor, monitor_xor, dispatch_xor])
root.order.add_edge(seed_selection, environment_setup)
root.order.add_edge(environment_setup, sensor_xor)
root.order.add_edge(sensor_xor, monitor_xor)
root.order.add_edge(monitor_xor, dispatch_xor)

# Print the root
print(root)