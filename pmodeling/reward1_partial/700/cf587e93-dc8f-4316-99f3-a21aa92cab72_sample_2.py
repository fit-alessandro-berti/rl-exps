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

# Define partial order nodes
initial_node = StrictPartialOrder(nodes=[seed_select, nutrient_mix, sensor_setup, env_monitor])
initial_node.order.add_edge(seed_select, nutrient_mix)
initial_node.order.add_edge(nutrient_mix, sensor_setup)
initial_node.order.add_edge(sensor_setup, env_monitor)

growth_node = StrictPartialOrder(nodes=[growth_scan, pest_control, water_cycle])
growth_node.order.add_edge(growth_scan, pest_control)
growth_node.order.add_edge(pest_control, water_cycle)

harvest_node = StrictPartialOrder(nodes=[harvest_robo, yield_assess])
harvest_node.order.add_edge(harvest_robo, yield_assess)

waste_node = StrictPartialOrder(nodes=[waste_process, energy_sync])
waste_node.order.add_edge(waste_process, energy_sync)

pack_node = StrictPartialOrder(nodes=[pack_biodeg, market_track, order_align, logistics_plan])
pack_node.order.add_edge(pack_biodeg, market_track)
pack_node.order.add_edge(market_track, order_align)
pack_node.order.add_edge(order_align, logistics_plan)

feedback_node = StrictPartialOrder(nodes=[feedback_loop])
feedback_node.order.add_edge(feedback_loop, initial_node)

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_node, growth_node, harvest_node, waste_node, pack_node, feedback_node])
root.order.add_edge(initial_node, growth_node)
root.order.add_edge(growth_node, harvest_node)
root.order.add_edge(harvest_node, waste_node)
root.order.add_edge(waste_node, pack_node)
root.order.add_edge(pack_node, feedback_node)