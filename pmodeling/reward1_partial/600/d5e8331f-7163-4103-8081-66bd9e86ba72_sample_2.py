import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define loops and choices
site_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_prep, seed_select, nutrient_mix, plant_rows, env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage])
env_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage])
data_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_prep_loop, env_monitor_loop, data_analyze_loop, harvest_crop, quality_sort, pack_goods, cold_store, market_ship])
root.order.add_edge(site_prep_loop, env_monitor_loop)
root.order.add_edge(env_monitor_loop, data_analyze_loop)
root.order.add_edge(data_analyze_loop, harvest_crop)
root.order.add_edge(harvest_crop, quality_sort)
root.order.add_edge(quality_sort, pack_goods)
root.order.add_edge(pack_goods, cold_store)
root.order.add_edge(cold_store, market_ship)