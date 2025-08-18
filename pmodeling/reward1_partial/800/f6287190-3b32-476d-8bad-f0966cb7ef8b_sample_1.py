import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process tree
iot_setup_to_sensor_check = OperatorPOWL(operator=Operator.XOR, children=[sensor_check, cycle_reset])
climate_map_to_iot_setup = OperatorPOWL(operator=Operator.XOR, children=[iot_setup, cycle_reset])
nutrient_mix_to_light_adjust = OperatorPOWL(operator=Operator.XOR, children=[light_adjust, cycle_reset])
light_adjust_to_water_cycle = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, cycle_reset])
water_cycle_to_pest_scan = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, cycle_reset])
pest_scan_to_growth_audit = OperatorPOWL(operator=Operator.XOR, children=[growth_audit, cycle_reset])
growth_audit_to_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, cycle_reset])
harvest_plan_to_demand_sync = OperatorPOWL(operator=Operator.XOR, children=[demand_sync, cycle_reset])
demand_sync_to_quality_grade = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, cycle_reset])
quality_grade_to_pack_items = OperatorPOWL(operator=Operator.XOR, children=[pack_items, cycle_reset])
pack_items_to_waste_compost = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, cycle_reset])
waste_compost_to_data_review = OperatorPOWL(operator=Operator.XOR, children=[data_review, cycle_reset])
data_review_to_cycle_reset = OperatorPOWL(operator=Operator.XOR, children=[cycle_reset, cycle_reset])

# Define the root
root = StrictPartialOrder(nodes=[
    seed_select, climate_map, iot_setup, nutrient_mix, sensor_check, light_adjust, water_cycle, pest_scan, growth_audit, harvest_plan, demand_sync, quality_grade, pack_items, waste_compost, data_review, cycle_reset
])
root.order.add_edge(climate_map, iot_setup)
root.order.add_edge(iot_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, light_adjust)
root.order.add_edge(light_adjust, water_cycle)
root.order.add_edge(water_cycle, pest_scan)
root.order.add_edge(pest_scan, growth_audit)
root.order.add_edge(growth_audit, harvest_plan)
root.order.add_edge(harvest_plan, demand_sync)
root.order.add_edge(demand_sync, quality_grade)
root.order.add_edge(quality_grade, pack_items)
root.order.add_edge(pack_items, waste_compost)
root.order.add_edge(waste_compost, data_review)
root.order.add_edge(data_review, cycle_reset)