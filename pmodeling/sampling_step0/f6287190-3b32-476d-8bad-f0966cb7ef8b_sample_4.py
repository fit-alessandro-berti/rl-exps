import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop for the IoT Setup and Sensor Check activities
iot_setup_check = OperatorPOWL(operator=Operator.LOOP, children=[iot_setup, sensor_check])
iot_setup_check.order.add_edge(iot_setup, sensor_check)

# Define choice for the Pest Scan and Light Adjust activities
pest_scan_light_adjust = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, light_adjust])

# Define choice for the Water Cycle and Waste Compost activities
water_cycle_waste_compost = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, waste_compost])

# Define loop for the Water Cycle and Waste Compost activities
water_cycle_waste_compost_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle_waste_compost])

# Define choice for the Nutrient Mix and Data Review activities
nutrient_mix_data_review = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, data_review])

# Define loop for the Nutrient Mix and Data Review activities
nutrient_mix_data_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix_data_review])

# Define choice for the Harvest Plan and Quality Grade activities
harvest_plan_quality_grade = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, quality_grade])

# Define loop for the Harvest Plan and Quality Grade activities
harvest_plan_quality_grade_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan_quality_grade])

# Define choice for the Growth Audit and Cycle Reset activities
growth_audit_cycle_reset = OperatorPOWL(operator=Operator.XOR, children=[growth_audit, cycle_reset])

# Define loop for the Growth Audit and Cycle Reset activities
growth_audit_cycle_reset_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_audit_cycle_reset])

# Define root for the process
root = StrictPartialOrder(nodes=[iot_setup_check, pest_scan_light_adjust, water_cycle_waste_compost_loop, nutrient_mix_data_review_loop, harvest_plan_quality_grade_loop, growth_audit_cycle_reset_loop])
root.order.add_edge(iot_setup_check, pest_scan_light_adjust)
root.order.add_edge(pest_scan_light_adjust, water_cycle_waste_compost_loop)
root.order.add_edge(water_cycle_waste_compost_loop, nutrient_mix_data_review_loop)
root.order.add_edge(nutrient_mix_data_review_loop, harvest_plan_quality_grade_loop)
root.order.add_edge(harvest_plan_quality_grade_loop, growth_audit_cycle_reset_loop)
root.order.add_edge(growth_audit_cycle_reset_loop, iot_setup_check)