from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
site_prep = Transition(label='Site Prep')
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
planting_rows = Transition(label='Planting Rows')
env_monitor = Transition(label='Env Monitor')
water_adjust = Transition(label='Water Adjust')
pest_control = Transition(label='Pest Control')
growth_check = Transition(label='Growth Check')
light_calibrate = Transition(label='Light Calibrate')
energy_manage = Transition(label='Energy Manage')
harvest_crop = Transition(label='Harvest Crop')
quality_sort = Transition(label='Quality Sort')
pack_goods = Transition(label='Pack Goods')
cold_store = Transition(label='Cold Store')
market_ship = Transition(label='Market Ship')
data_analyze = Transition(label='Data Analyze')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_prep,
    seed_select,
    nutrient_mix,
    planting_rows,
    env_monitor,
    water_adjust,
    pest_control,
    growth_check,
    light_calibrate,
    energy_manage,
    harvest_crop,
    quality_sort,
    pack_goods,
    cold_store,
    market_ship,
    data_analyze
])

# Define the dependencies
root.order.add_edge(site_prep, seed_select)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_rows)
root.order.add_edge(planting_rows, env_monitor)
root.order.add_edge(env_monitor, water_adjust)
root.order.add_edge(water_adjust, pest_control)
root.order.add_edge(pest_control, growth_check)
root.order.add_edge(growth_check, light_calibrate)
root.order.add_edge(light_calibrate, energy_manage)
root.order.add_edge(energy_manage, harvest_crop)
root.order.add_edge(harvest_crop, quality_sort)
root.order.add_edge(quality_sort, pack_goods)
root.order.add_edge(pack_goods, cold_store)
root.order.add_edge(cold_store, market_ship)
root.order.add_edge(market_ship, data_analyze)

# Now, 'root' contains the POWL model for the described process