import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, nutrient_mix, sensor_setup, env_monitor, growth_scan, pest_control, water_cycle, harvest_robo, yield_assess, waste_process, energy_sync])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pack_biodeg, market_track, order_align, logistics_plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)