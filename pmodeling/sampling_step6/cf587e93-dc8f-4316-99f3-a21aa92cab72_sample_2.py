import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
env_monitor = Transition(label='Env Monitor')
growth_scan = Transition(label='Growth Scan')
pest_control = Transition(label='Pest Control')
water_cycle = Transition(label='Water Cycle')
harvest_robo = Transition(label='Harvest Robo')
yield_assess = Transition(label='Yield Assess')
waste_process = Transition(label='Waste Process')
energy_sync = Transition(label='Energy Sync')
pack_biodeg = Transition(label='Pack Biodeg')
market_track = Transition(label='Market Track')
order_align = Transition(label='Order Align')
logistics_plan = Transition(label='Logistics Plan')
feedback_loop = Transition(label='Feedback Loop')

# Define the root POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, sensor_setup, env_monitor, growth_scan, pest_control,
    water_cycle, harvest_robo, yield_assess, waste_process, energy_sync, pack_biodeg,
    market_track, order_align, logistics_plan, feedback_loop
])
# The order is defined by the sequence of activities as per the problem description
# Since the problem doesn't specify dependencies, we assume they are all concurrent
# If there were dependencies, they would be added here as edges in the partial order

# Print the root POWL model
print(root)