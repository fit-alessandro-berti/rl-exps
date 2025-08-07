import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
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

# Define the inner loop body (monitor, adjust, calibrate, manage)
inner_loop_body = StrictPartialOrder(nodes=[
    env_monitor, water_adjust, pest_control, growth_check,
    light_calibrate, energy_manage
])
# No explicit order edges; they'll be inferred by the LOOP operator

# Define the monitoring loop: Env Monitor, then optionally Water Adjust etc. repeated
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[env_monitor, inner_loop_body]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_prep, seed_select, nutrient_mix, planting_rows,
    monitor_loop,
    harvest_crop, quality_sort, pack_goods,
    cold_store, market_ship, data_analyze
])

# Add the sequential edges
root.order.add_edge(site_prep,      seed_select)
root.order.add_edge(seed_select,    nutrient_mix)
root.order.add_edge(nutrient_mix,   planting_rows)
root.order.add_edge(planting_rows,  monitor_loop)

# After harvest, the sequence continues
root.order.add_edge(harvest_crop,   quality_sort)
root.order.add_edge(quality_sort,   pack_goods)
root.order.add_edge(pack_goods,     cold_store)
root.order.add_edge(cold_store,     market_ship)
root.order.add_edge(market_ship,    data_analyze)