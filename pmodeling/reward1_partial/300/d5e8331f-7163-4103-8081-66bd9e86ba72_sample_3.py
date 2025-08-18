import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[site_prep, seed_select, nutrient_mix, planting_rows])
xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_crop, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_sort, pack_goods])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[cold_store, market_ship])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, xor, xor2, xor3, xor4])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)

print(root)