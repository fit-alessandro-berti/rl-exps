import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

# Site Preparation
site_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_prep, seed_select, nutrient_mix, plant_rows])

# Seed Selection
seed_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, nutrient_mix, plant_rows])

# Nutrient Management
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, plant_rows])

# Planting Rows
plant_rows_loop = OperatorPOWL(operator=Operator.LOOP, children=[plant_rows, env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage, harvest_crop])

# Environmental Monitoring
env_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage, harvest_crop])

# Water Adjust
water_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_adjust, pest_control, growth_check, light_calibrate, energy_manage, harvest_crop])

# Pest Control
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, growth_check, light_calibrate, energy_manage, harvest_crop])

# Growth Check
growth_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_check, light_calibrate, energy_manage, harvest_crop])

# Light Calibration
light_calibrate_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_calibrate, energy_manage, harvest_crop])

# Energy Management
energy_manage_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_manage, harvest_crop])

# Harvest Crop
harvest_crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crop, quality_sort, pack_goods, cold_store, market_ship])

# Quality Sorting
quality_sort_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_sort, pack_goods, cold_store, market_ship])

# Packing Goods
pack_goods_loop = OperatorPOWL(operator=Operator.LOOP, children=[pack_goods, cold_store, market_ship])

# Cold Storage
cold_store_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_store, market_ship])

# Market Shipping
market_ship_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_ship, data_analyze])

# Data Analysis
data_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze])

# Main Workflow
root = StrictPartialOrder(nodes=[site_prep_loop, seed_select_loop, nutrient_mix_loop, plant_rows_loop, env_monitor_loop, water_adjust_loop, pest_control_loop, growth_check_loop, light_calibrate_loop, energy_manage_loop, harvest_crop_loop, quality_sort_loop, pack_goods_loop, cold_store_loop, market_ship_loop, data_analyze_loop])
root.order.add_edge(site_prep_loop, seed_select_loop)
root.order.add_edge(seed_select_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, plant_rows_loop)
root.order.add_edge(plant_rows_loop, env_monitor_loop)
root.order.add_edge(env_monitor_loop, water_adjust_loop)
root.order.add_edge(water_adjust_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, growth_check_loop)
root.order.add_edge(growth_check_loop, light_calibrate_loop)
root.order.add_edge(light_calibrate_loop, energy_manage_loop)
root.order.add_edge(energy_manage_loop, harvest_crop_loop)
root.order.add_edge(harvest_crop_loop, quality_sort_loop)
root.order.add_edge(quality_sort_loop, pack_goods_loop)
root.order.add_edge(pack_goods_loop, cold_store_loop)
root.order.add_edge(cold_store_loop, market_ship_loop)
root.order.add_edge(market_ship_loop, data_analyze_loop)