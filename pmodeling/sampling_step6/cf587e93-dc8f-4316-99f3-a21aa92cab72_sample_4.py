import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition with its label
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

# Define the partial order where activities are concurrent but depend on each other
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

# Since there are no explicit dependencies, we can assume they are concurrent by default
# No need to add any edges explicitly as the partial order defines the concurrency

# The 'root' variable now contains the POWL model for the urban vertical farm process