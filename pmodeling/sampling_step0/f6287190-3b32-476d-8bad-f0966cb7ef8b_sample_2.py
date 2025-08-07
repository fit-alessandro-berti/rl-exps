import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_select = Transition(label='Seed Select')
climate_map = Transition(label='Climate Map')
iot_setup = Transition(label='IoT Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_check = Transition(label='Sensor Check')
light_adjust = Transition(label='Light Adjust')
water_cycle = Transition(label='Water Cycle')
pest_scan = Transition(label='Pest Scan')
growth_audit = Transition(label='Growth Audit')
harvest_plan = Transition(label='Harvest Plan')
demand_sync = Transition(label='Demand Sync')
quality_grade = Transition(label='Quality Grade')
pack_items = Transition(label='Pack Items')
waste_compost = Transition(label='Waste Compost')
data_review = Transition(label='Data Review')
cycle_reset = Transition(label='Cycle Reset')

loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, climate_map, iot_setup, nutrient_mix, sensor_check, light_adjust, water_cycle, pest_scan, growth_audit, harvest_plan, demand_sync, quality_grade, pack_items, waste_compost, data_review])
xor = OperatorPOWL(operator=Operator.XOR, children=[cycle_reset, loop])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)