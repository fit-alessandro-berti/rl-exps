import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[site_prep, seed_select, nutrient_mix, planting_rows, env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crop, quality_sort, pack_goods, cold_store, market_ship])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze])
root = StrictPartialOrder(nodes=[xor, loop1, loop2])
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, loop2)