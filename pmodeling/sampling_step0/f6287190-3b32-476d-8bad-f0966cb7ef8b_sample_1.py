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

# Choices
climate_iot = OperatorPOWL(operator=Operator.XOR, children=[climate_map, iot_setup])
nutrient_light = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, light_adjust])
water_sensor = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, sensor_check])
pest_growth = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, growth_audit])
harvest_plan_sync = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, demand_sync])
quality_pack = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, pack_items])
waste_data = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, data_review])

# Loops
cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_reset])

# Root
root = StrictPartialOrder(nodes=[seed_select, climate_iot, nutrient_light, water_sensor, pest_growth, harvest_plan_sync, quality_pack, waste_data, cycle_loop])
root.order.add_edge(climate_iot, nutrient_light)
root.order.add_edge(nutrient_light, water_sensor)
root.order.add_edge(water_sensor, pest_growth)
root.order.add_edge(pest_growth, harvest_plan_sync)
root.order.add_edge(harvest_plan_sync, quality_pack)
root.order.add_edge(quality_pack, waste_data)
root.order.add_edge(waste_data, cycle_loop)
root.order.add_edge(cycle_loop, seed_select)