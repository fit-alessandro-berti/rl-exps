import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
setup = Transition(label='Environment Setup')
sensor = Transition(label='Sensor Deployment')
monitor = Transition(label='Growth Monitoring')
detect = Transition(label='Pest Detection')
harvest = Transition(label='Automated Harvest')
quality = Transition(label='Quality Check')
pack = Transition(label='Packaging Prep')
biodegradable = Transition(label='Biodegradable Pack')
inventory = Transition(label='Inventory Sync')
forecast = Transition(label='Demand Forecast')
micro = Transition(label='Micro Fulfillment')
dispatch = Transition(label='Local Dispatch')
feedback = Transition(label='Consumer Feedback')
adjust = Transition(label='Crop Adjustment')

# Build the feedback loop: after Consumer Feedback, either adjust Crop or exit silently
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[adjust, feedback])

# Build the core farming sequence as a partial order
core_farm = StrictPartialOrder(nodes=[
    seed, nutrient, setup, sensor, monitor, detect,
    harvest, quality, pack, biodegradable, inventory,
    forecast, micro, dispatch
])
core_farm.order.add_edge(seed, nutrient)
core_farm.order.add_edge(nutrient, setup)
core_farm.order.add_edge(setup, sensor)
core_farm.order.add_edge(sensor, monitor)
core_farm.order.add_edge(monitor, detect)
core_farm.order.add_edge(detect, harvest)
core_farm.order.add_edge(harvest, quality)
core_farm.order.add_edge(quality, pack)
core_farm.order.add_edge(pack, biodegradable)
core_farm.order.add_edge(biodegradable, inventory)
core_farm.order.add_edge(inventory, forecast)
core_farm.order.add_edge(forecast, micro)
core_farm.order.add_edge(micro, dispatch)

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    seed, nutrient, setup, sensor, monitor, detect,
    harvest, quality, pack, biodegradable, inventory,
    forecast, micro, dispatch, feedback_loop
])
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, setup)
root.order.add_edge(setup, sensor)
root.order.add_edge(sensor, monitor)
root.order.add_edge(monitor, detect)
root.order.add_edge(detect, harvest)
root.order.add_edge(harvest, quality)
root.order.add_edge(quality, pack)
root.order.add_edge(pack, biodegradable)
root.order.add_edge(biodegradable, inventory)
root.order.add_edge(inventory, forecast)
root.order.add_edge(forecast, micro)
root.order.add_edge(micro, dispatch)
root.order.add_edge(dispatch, feedback_loop)