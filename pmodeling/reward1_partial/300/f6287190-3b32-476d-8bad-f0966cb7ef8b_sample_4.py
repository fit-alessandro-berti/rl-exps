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

skip = SilentTransition()

climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_map, iot_setup, nutrient_mix, sensor_check, light_adjust, water_cycle])
pest_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, skip])
growth_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_audit, skip])
demand_sync_xor = OperatorPOWL(operator=Operator.XOR, children=[demand_sync, skip])
quality_grade_xor = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, skip])
pack_items_xor = OperatorPOWL(operator=Operator.XOR, children=[pack_items, skip])
waste_compost_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, skip])
data_review_xor = OperatorPOWL(operator=Operator.XOR, children=[data_review, skip])
cycle_reset_xor = OperatorPOWL(operator=Operator.XOR, children=[cycle_reset, skip])

root = StrictPartialOrder(nodes=[
    seed_select,
    climate_loop,
    pest_scan_xor,
    growth_audit_xor,
    demand_sync_xor,
    quality_grade_xor,
    pack_items_xor,
    waste_compost_xor,
    data_review_xor,
    cycle_reset_xor
])
root.order.add_edge(climate_loop, pest_scan_xor)
root.order.add_edge(climate_loop, growth_audit_xor)
root.order.add_edge(pest_scan_xor, demand_sync_xor)
root.order.add_edge(growth_audit_xor, quality_grade_xor)
root.order.add_edge(demand_sync_xor, pack_items_xor)
root.order.add_edge(quality_grade_xor, waste_compost_xor)
root.order.add_edge(pack_items_xor, data_review_xor)
root.order.add_edge(data_review_xor, cycle_reset_xor)