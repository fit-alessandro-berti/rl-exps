import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Setup')
growth = Transition(label='Growth Monitoring')
climate = Transition(label='Climate Adjust')
pest = Transition(label='Pest Control')
water = Transition(label='Water Recirculate')
light = Transition(label='Light Calibration')
harvest = Transition(label='Robotic Harvest')
inspect = Transition(label='Quality Inspect')
waste = Transition(label='Waste Process')
energy = Transition(label='Energy Reuse')
inventory = Transition(label='Inventory Update')
demand = Transition(label='Demand Forecast')
dispatch = Transition(label='Order Dispatch')
event = Transition(label='Community Event')
feedback = Transition(label='Feedback Collect')
analyze = Transition(label='Data Analyze')

# Loop for continuous environmental adjustments
adjustments = StrictPartialOrder(nodes=[climate, pest, water, light])
# no order edges => they can run in parallel

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    seed, nutrient, growth,
    adjustments,
    harvest, inspect, waste, energy,
    inventory, demand, dispatch,
    event, feedback, analyze
])

# Define the control-flow dependencies
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, growth)

root.order.add_edge(growth, adjustments)
root.order.add_edge(adjustments, growth)

root.order.add_edge(growth, harvest)
root.order.add_edge(harvest, inspect)
root.order.add_edge(inspect, waste)
root.order.add_edge(waste, energy)
root.order.add_edge(energy, inventory)

root.order.add_edge(inventory, demand)
root.order.add_edge(demand, dispatch)

root.order.add_edge(dispatch, event)
root.order.add_edge(event, feedback)
root.order.add_edge(feedback, analyze)