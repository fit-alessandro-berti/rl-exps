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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_select])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[water_adjust, env_monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, growth_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[light_calibrate, energy_manage])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, harvesting])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[cold_store, market_ship])

root = StrictPartialOrder(nodes=[site_prep, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(site_prep, xor1)
root.order.add_edge(site_prep, xor2)
root.order.add_edge(site_prep, xor3)
root.order.add_edge(site_prep, xor4)
root.order.add_edge(site_prep, xor5)
root.order.add_edge(site_prep, xor6)

print(root)