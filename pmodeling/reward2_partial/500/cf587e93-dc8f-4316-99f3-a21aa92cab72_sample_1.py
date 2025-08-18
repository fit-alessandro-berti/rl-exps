import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
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

# Define the order dependencies
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, env_monitor)
root.order.add_edge(env_monitor, growth_scan)
root.order.add_edge(growth_scan, pest_control)
root.order.add_edge(pest_control, water_cycle)
root.order.add_edge(water_cycle, harvest_robo)
root.order.add_edge(harvest_robo, yield_assess)
root.order.add_edge(yield_assess, waste_process)
root.order.add_edge(waste_process, energy_sync)
root.order.add_edge(energy_sync, pack_biodeg)
root.order.add_edge(pack_biodeg, market_track)
root.order.add_edge(market_track, order_align)
root.order.add_edge(order_align, logistics_plan)
root.order.add_edge(logistics_plan, feedback_loop)

# Print the root model
print(root)