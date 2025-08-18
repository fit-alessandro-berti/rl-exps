import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the process flow
iot_setup_then_check = OperatorPOWL(operator=Operator.LOOP, children=[iot_setup, sensor_check])
nutrient_mix_then_audit = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, growth_audit])
pest_scan_then_adjust = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, light_adjust])
water_cycle_then_plan = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle, harvest_plan])
demand_sync_then_grade = OperatorPOWL(operator=Operator.LOOP, children=[demand_sync, quality_grade])
pack_items_then_compost = OperatorPOWL(operator=Operator.LOOP, children=[pack_items, waste_compost])
data_review_then_reset = OperatorPOWL(operator=Operator.LOOP, children=[data_review, cycle_reset])

# Define the final loop
root = StrictPartialOrder(nodes=[iot_setup_then_check, nutrient_mix_then_audit, pest_scan_then_adjust, water_cycle_then_plan, demand_sync_then_grade, pack_items_then_compost, data_review_then_reset])
root.order.add_edge(iot_setup_then_check, nutrient_mix_then_audit)
root.order.add_edge(nutrient_mix_then_audit, pest_scan_then_adjust)
root.order.add_edge(pest_scan_then_adjust, water_cycle_then_plan)
root.order.add_edge(water_cycle_then_plan, demand_sync_then_grade)
root.order.add_edge(demand_sync_then_grade, pack_items_then_compost)
root.order.add_edge(pack_items_then_compost, data_review_then_reset)