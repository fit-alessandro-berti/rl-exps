import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select      = Transition(label='Seed Select')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_setup     = Transition(label='Sensor Setup')
env_monitor      = Transition(label='Env Monitor')
growth_scan      = Transition(label='Growth Scan')
pest_control     = Transition(label='Pest Control')
water_cycle      = Transition(label='Water Cycle')
harvest_robo     = Transition(label='Harvest Robo')
yield_assess     = Transition(label='Yield Assess')
waste_process    = Transition(label='Waste Process')
energy_sync      = Transition(label='Energy Sync')
pack_biodeg      = Transition(label='Pack Biodeg')
market_track     = Transition(label='Market Track')
order_align      = Transition(label='Order Align')
logistics_plan   = Transition(label='Logistics Plan')
feedback_loop    = Transition(label='Feedback Loop')

# Define the main growth cycle as a partial order
growth_cycle = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, sensor_setup, env_monitor,
    growth_scan, pest_control, water_cycle, harvest_robo,
    yield_assess, waste_process, energy_sync, pack_biodeg,
    market_track, order_align, logistics_plan
])
growth_cycle.order.add_edge(seed_select,    nutrient_mix)
growth_cycle.order.add_edge(nutrient_mix,   sensor_setup)
growth_cycle.order.add_edge(sensor_setup,   env_monitor)
growth_cycle.order.add_edge(env_monitor,    growth_scan)
growth_cycle.order.add_edge(growth_scan,    pest_control)
growth_cycle.order.add_edge(pest_control,   water_cycle)
growth_cycle.order.add_edge(water_cycle,    harvest_robo)
growth_cycle.order.add_edge(harvest_robo,   yield_assess)
growth_cycle.order.add_edge(yield_assess,   waste_process)
growth_cycle.order.add_edge(waste_process,  energy_sync)
growth_cycle.order.add_edge(energy_sync,    pack_biodeg)
growth_cycle.order.add_edge(pack_biodeg,    market_track)
growth_cycle.order.add_edge(market_track,   order_align)
growth_cycle.order.add_edge(order_align,    logistics_plan)

# Define the feedback loop: after logistics_plan, optionally do feedback_loop and repeat
feedback_loop_po = StrictPartialOrder(nodes=[feedback_loop])
feedback_loop_po.order.add_edge(feedback_loop, feedback_loop)

root = OperatorPOWL(operator=Operator.LOOP, children=[growth_cycle, feedback_loop_po])