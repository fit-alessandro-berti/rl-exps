import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Selection')
ai = Transition(label='AI Prediction')
plant = Transition(label='Automated Planting')
calibrate = Transition(label='Sensor Calibration')
env_adjust = Transition(label='Environment Adjust')
nutrient = Transition(label='Nutrient Dosing')
hydro = Transition(label='Hydroponic Flow')
prune = Transition(label='Robotic Pruning')
monitor = Transition(label='Health Monitor')
harvest = Transition(label='Harvesting Ops')
analysis = Transition(label='Data Analysis')
predict = Transition(label='Predictive Check')
waste = Transition(label='Waste Composting')
water = Transition(label='Water Recycling')
pack = Transition(label='Eco Packaging')
carbon = Transition(label='Carbon Tracking')
dispatch = Transition(label='Logistics Dispatch')

# Loop for continuous environment adjustment and nutrient dosing
loop_env = OperatorPOWL(operator=Operator.LOOP, children=[env_adjust, nutrient])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    seed, ai, plant, calibrate, loop_env, hydro, prune, monitor,
    harvest, analysis, predict, waste, water, pack, carbon, dispatch
])

# Sequence of activities before the loop
root.order.add_edge(seed, ai)
root.order.add_edge(ai, plant)
root.order.add_edge(plant, calibrate)

# The loop for environmental adjustments and nutrient dosing
root.order.add_edge(calibrate, loop_env)

# After the loop, continue with hydroponic flow, pruning, health monitoring, harvesting
root.order.add_edge(loop_env, hydro)
root.order.add_edge(hydro, prune)
root.order.add_edge(prune, monitor)
root.order.add_edge(monitor, harvest)

# After harvesting, analysis and predictive check
root.order.add_edge(harvest, analysis)
root.order.add_edge(analysis, predict)

# Waste and recycling activities in parallel
waste_recycle = StrictPartialOrder(nodes=[waste, water])
waste_recycle.order.add_edge(waste, water)
root.order.add_edge(predict, waste_recycle)

# Packaging, carbon tracking, and logistics dispatch
root.order.add_edge(waste_recycle, pack)
root.order.add_edge(pack, carbon)
root.order.add_edge(carbon, dispatch)

# Return the root of the POWL model