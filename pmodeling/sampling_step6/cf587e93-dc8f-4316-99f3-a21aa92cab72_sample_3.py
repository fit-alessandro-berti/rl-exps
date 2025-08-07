import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
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

# Define the Partial Order structure
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_mix,
    sensor_setup,
    env_monitor,
    growth_scan,
    pest_control,
    water_cycle,
    harvest_robo,
    yield_assess,
    waste_process,
    energy_sync,
    pack_biodeg,
    market_track,
    order_align,
    logistics_plan,
    feedback_loop
])

# The order of execution is not explicitly defined in the question, so we assume they are concurrent
# If you want to define a specific order, you can uncomment and modify the following line:
# root.order.add_edge(...)

# Save the final result in the variable 'root'