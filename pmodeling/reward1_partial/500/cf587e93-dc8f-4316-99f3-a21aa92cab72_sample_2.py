import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = ['Seed Select', 'Nutrient Mix', 'Sensor Setup', 'Env Monitor', 'Growth Scan', 'Pest Control', 'Water Cycle', 'Harvest Robo', 'Yield Assess', 'Waste Process', 'Energy Sync', 'Pack Biodeg', 'Market Track', 'Order Align', 'Logistics Plan', 'Feedback Loop']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the workflow model
seed_select = transitions[0]
nutrient_mix = transitions[1]
sensor_setup = transitions[2]
env_monitor = transitions[3]
growth_scan = transitions[4]
pest_control = transitions[5]
water_cycle = transitions[6]
harvest_robo = transitions[7]
yield_assess = transitions[8]
waste_process = transitions[9]
energy_sync = transitions[10]
pack_biodeg = transitions[11]
market_track = transitions[12]
order_align = transitions[13]
logistics_plan = transitions[14]
feedback_loop = transitions[15]

# Define the partial order
root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, sensor_setup, env_monitor, growth_scan, pest_control, water_cycle, harvest_robo, yield_assess, waste_process, energy_sync, pack_biodeg, market_track, order_align, logistics_plan, feedback_loop])
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(seed_select, sensor_setup)
root.order.add_edge(nutrient_mix, env_monitor)
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