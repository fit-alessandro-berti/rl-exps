import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
setup = Transition(label='Environment Setup')
sensor = Transition(label='Sensor Deployment')
growth = Transition(label='Growth Monitoring')
pest = Transition(label='Pest Detection')
harvest = Transition(label='Automated Harvest')
quality = Transition(label='Quality Check')
pack = Transition(label='Packaging Prep')
biodegradable = Transition(label='Biodegradable Pack')
inventory = Transition(label='Inventory Sync')
demand = Transition(label='Demand Forecast')
micro = Transition(label='Micro Fulfillment')
dispatch = Transition(label='Local Dispatch')
feedback = Transition(label='Consumer Feedback')
adjust = Transition(label='Crop Adjustment')

# Build the growth monitoring loop: repeat Growth Monitoring then Pest Detection until exit
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, pest])

# Build the main production sequence
production_seq = StrictPartialOrder(nodes=[
    seed, nutrient, setup, sensor, growth_loop,
    harvest, quality, pack, biodegradable,
    inventory, demand, micro, dispatch
])
# Add edges to sequence
production_seq.order.add_edge(seed, nutrient)
production_seq.order.add_edge(nutrient, setup)
production_seq.order.add_edge(setup, sensor)
production_seq.order.add_edge(sensor, growth_loop)
production_seq.order.add_edge(growth_loop, harvest)
production_seq.order.add_edge(harvest, quality)
production_seq.order.add_edge(quality, pack)
production_seq.order.add_edge(pack, biodegradable)
production_seq.order.add_edge(biodegradable, inventory)
production_seq.order.add_edge(inventory, demand)
production_seq.order.add_edge(demand, micro)
production_seq.order.add_edge(micro, dispatch)

# Build the feedback loop: repeat Consumer Feedback then Crop Adjustment until exit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback, adjust])

# Assemble the complete root process
root = StrictPartialOrder(nodes=[
    production_seq, feedback_loop
])
# Add edges to root
root.order.add_edge(production_seq, feedback_loop)

print(root)