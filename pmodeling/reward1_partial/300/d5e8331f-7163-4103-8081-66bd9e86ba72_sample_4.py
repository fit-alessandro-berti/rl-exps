from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for no operations
skip = SilentTransition()

# Define loops and choices for the process
site_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_prep, seed_select])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, planting_rows])
env_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_monitor, water_adjust])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, growth_check])
light_calibrate_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_calibrate, energy_manage])
harvest_crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crop, quality_sort])
pack_goods_loop = OperatorPOWL(operator=Operator.LOOP, children=[pack_goods, cold_store])
market_ship_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_ship, data_analyze])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_prep_loop, nutrient_mix_loop, env_monitor_loop, pest_control_loop, light_calibrate_loop, harvest_crop_loop, pack_goods_loop, market_ship_loop])
root.order.add_edge(site_prep_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, planting_rows)
root.order.add_edge(planting_rows, env_monitor_loop)
root.order.add_edge(env_monitor_loop, water_adjust)
root.order.add_edge(water_adjust, pest_control_loop)
root.order.add_edge(pest_control_loop, growth_check)
root.order.add_edge(growth_check, light_calibrate_loop)
root.order.add_edge(light_calibrate_loop, energy_manage)
root.order.add_edge(energy_manage, harvest_crop_loop)
root.order.add_edge(harvest_crop_loop, quality_sort)
root.order.add_edge(quality_sort, pack_goods_loop)
root.order.add_edge(pack_goods_loop, cold_store)
root.order.add_edge(cold_store, market_ship_loop)
root.order.add_edge(market_ship_loop, data_analyze)