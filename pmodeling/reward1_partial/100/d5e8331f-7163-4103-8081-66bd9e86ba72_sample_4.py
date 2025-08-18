from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
site_prep = Transition(label='Site Prep')
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
plant_rows = Transition(label='Planting Rows')
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

# Define the POWL model
root = StrictPartialOrder()

# Add activities to the root
root.nodes.add(site_prep)
root.nodes.add(seed_select)
root.nodes.add(nutrient_mix)
root.nodes.add(plant_rows)
root.nodes.add(env_monitor)
root.nodes.add(water_adjust)
root.nodes.add(pest_control)
root.nodes.add(growth_check)
root.nodes.add(light_calibrate)
root.nodes.add(energy_manage)
root.nodes.add(harvest_crop)
root.nodes.add(quality_sort)
root.nodes.add(pack_goods)
root.nodes.add(cold_store)
root.nodes.add(market_ship)
root.nodes.add(data_analyze)

# Define the flow of activities
root.order.add_edge(site_prep, seed_select)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, plant_rows)
root.order.add_edge(plant_rows, env_monitor)
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

# Ensure all nodes are connected (if necessary)
# (In this case, all nodes are connected by the defined flow)

# Final POWL model
print(root)