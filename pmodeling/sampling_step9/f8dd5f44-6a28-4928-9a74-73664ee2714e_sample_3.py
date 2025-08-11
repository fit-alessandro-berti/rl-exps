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

skip = SilentTransition()

# Loop for automated harvest and quality check
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[automated_harvest, quality_check])

# XOR for packaging and inventory sync
packaging_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, inventory_sync])

# XOR for local dispatch and micro fulfillment
dispatch_xor = OperatorPOWL(operator=Operator.XOR, children=[local_dispatch, micro_fulfillment])

# Loop for consumer feedback and crop adjustment
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback, crop_adjustment])

# Define the root POWL model
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup, sensor_deployment, growth_monitoring, pest_detection, harvest_loop, packaging_xor, dispatch_xor, feedback_loop])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, environment_setup)
root.order.add_edge(seed_selection, sensor_deployment)
root.order.add_edge(nutrient_mix, environment_setup)
root.order.add_edge(environment_setup, growth_monitoring)
root.order.add_edge(environment_setup, pest_detection)
root.order.add_edge(pest_detection, automated_harvest)
root.order.add_edge(pest_detection, quality_check)
root.order.add_edge(automated_harvest, harvest_loop)
root.order.add_edge(quality_check, harvest_loop)
root.order.add_edge(harvest_loop, packaging_xor)
root.order.add_edge(packaging_xor, dispatch_xor)
root.order.add_edge(dispatch_xor, feedback_loop)
root.order.add_edge(feedback_loop, crop_adjustment)