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

# Define the partial order
root = StrictPartialOrder(nodes=[seed_select, climate_map, iot_setup, nutrient_mix, sensor_check, light_adjust, water_cycle, pest_scan, growth_audit, harvest_plan, demand_sync, quality_grade, pack_items, waste_compost, data_review, cycle_reset])

# Define the dependencies
root.order.add_edge(seed_select, climate_map)
root.order.add_edge(climate_map, iot_setup)
root.order.add_edge(iot_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_check)
root.order.add_edge(sensor_check, light_adjust)
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