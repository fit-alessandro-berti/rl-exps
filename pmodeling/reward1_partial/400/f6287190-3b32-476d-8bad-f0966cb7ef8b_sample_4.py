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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[climate_map, iot_setup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, sensor_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[light_adjust, water_cycle])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, growth_audit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, demand_sync])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, pack_items])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, data_review])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6, xor7])

root = StrictPartialOrder(nodes=[loop1, loop2, seed_select])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, seed_select)