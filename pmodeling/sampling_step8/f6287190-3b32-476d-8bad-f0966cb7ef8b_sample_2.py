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

skip = SilentTransition()

climate_map_or_iot_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_map, iot_setup])
sensor_check_or_light_adjust = OperatorPOWL(operator=Operator.XOR, children=[sensor_check, light_adjust])
water_cycle_or_sensor_check = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, sensor_check])
pest_scan_or_sensor_check = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, sensor_check])
growth_audit_or_pest_scan = OperatorPOWL(operator=Operator.XOR, children=[growth_audit, pest_scan])
harvest_plan_or_growth_audit = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, growth_audit])
demand_sync_or_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[demand_sync, harvest_plan])
quality_grade_or_demand_sync = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, demand_sync])
pack_items_or_quality_grade = OperatorPOWL(operator=Operator.XOR, children=[pack_items, quality_grade])
waste_compost_or_pack_items = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, pack_items])
data_review_or_waste_compost = OperatorPOWL(operator=Operator.XOR, children=[data_review, waste_compost])
cycle_reset_or_data_review = OperatorPOWL(operator=Operator.XOR, children=[cycle_reset, data_review])

root = StrictPartialOrder(nodes=[
    seed_select,
    climate_map_or_iot_setup,
    sensor_check_or_light_adjust,
    water_cycle_or_sensor_check,
    pest_scan_or_sensor_check,
    growth_audit_or_pest_scan,
    harvest_plan_or_growth_audit,
    demand_sync_or_harvest_plan,
    quality_grade_or_demand_sync,
    pack_items_or_quality_grade,
    waste_compost_or_pack_items,
    data_review_or_waste_compost,
    cycle_reset_or_data_review
])

root.order.add_edge(climate_map_or_iot_setup, sensor_check_or_light_adjust)
root.order.add_edge(sensor_check_or_light_adjust, water_cycle_or_sensor_check)
root.order.add_edge(water_cycle_or_sensor_check, pest_scan_or_sensor_check)
root.order.add_edge(pest_scan_or_sensor_check, growth_audit_or_pest_scan)
root.order.add_edge(growth_audit_or_pest_scan, harvest_plan_or_growth_audit)
root.order.add_edge(harvest_plan_or_growth_audit, demand_sync_or_harvest_plan)
root.order.add_edge(demand_sync_or_harvest_plan, quality_grade_or_demand_sync)
root.order.add_edge(quality_grade_or_demand_sync, pack_items_or_quality_grade)
root.order.add_edge(pack_items_or_quality_grade, waste_compost_or_pack_items)
root.order.add_edge(waste_compost_or_pack_items, data_review_or_waste_compost)
root.order.add_edge(data_review_or_waste_compost, cycle_reset_or_data_review)