import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_prep       = Transition(label='Site Prep')
seed_select     = Transition(label='Seed Select')
nutrient_mix    = Transition(label='Nutrient Mix')
planting_rows   = Transition(label='Planting Rows')
env_monitor     = Transition(label='Env Monitor')
water_adjust    = Transition(label='Water Adjust')
pest_control    = Transition(label='Pest Control')
growth_check    = Transition(label='Growth Check')
light_calibrate = Transition(label='Light Calibrate')
energy_manage   = Transition(label='Energy Manage')
harvest_crop    = Transition(label='Harvest Crop')
quality_sort    = Transition(label='Quality Sort')
pack_goods      = Transition(label='Pack Goods')
cold_store      = Transition(label='Cold Store')
market_ship     = Transition(label='Market Ship')
data_analyze    = Transition(label='Data Analyze')

# Define the core growth sequence as a partial order
growth_seq = StrictPartialOrder(nodes=[
    env_monitor, water_adjust, pest_control, growth_check,
    light_calibrate, energy_manage
])
growth_seq.order.add_edge(env_monitor, water_adjust)
growth_seq.order.add_edge(water_adjust, pest_control)
growth_seq.order.add_edge(pest_control, growth_check)
growth_seq.order.add_edge(growth_check, light_calibrate)
growth_seq.order.add_edge(light_calibrate, energy_manage)

# Define the post-harvest sequence as a partial order
post_seq = StrictPartialOrder(nodes=[
    harvest_crop, quality_sort, pack_goods, cold_store, market_ship
])
post_seq.order.add_edge(harvest_crop, quality_sort)
post_seq.order.add_edge(quality_sort, pack_goods)
post_seq.order.add_edge(pack_goods, cold_store)
post_seq.order.add_edge(cold_store, market_ship)

# Define the loop: continuously monitor and adjust environment
# until exit, then execute the growth sequence and repeat
loop_growth = OperatorPOWL(
    operator=Operator.LOOP,
    children=[env_monitor, growth_seq]
)

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_prep, seed_select, nutrient_mix, planting_rows,
    loop_growth, post_seq, data_analyze
])

# Add the control-flow edges
root.order.add_edge(site_prep, seed_select)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_rows)
root.order.add_edge(planting_rows, loop_growth)
root.order.add_edge(loop_growth, post_seq)
root.order.add_edge(post_seq, data_analyze)