import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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
root = StrictPartialOrder(nodes=[
    seed_select, climate_map, iot_setup, nutrient_mix, sensor_check,
    light_adjust, water_cycle, pest_scan, growth_audit, harvest_plan,
    demand_sync, quality_grade, pack_items, waste_compost, data_review, cycle_reset
])

# Define the dependencies (partial order edges)
root.order.add_edge(seed_select, climate_map)
root.order.add_edge(seed_select, iot_setup)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(seed_select, sensor_check)
root.order.add_edge(seed_select, light_adjust)
root.order.add_edge(seed_select, water_cycle)
root.order.add_edge(seed_select, pest_scan)
root.order.add_edge(seed_select, growth_audit)
root.order.add_edge(seed_select, harvest_plan)
root.order.add_edge(seed_select, demand_sync)
root.order.add_edge(seed_select, quality_grade)
root.order.add_edge(seed_select, pack_items)
root.order.add_edge(seed_select, waste_compost)
root.order.add_edge(seed_select, data_review)
root.order.add_edge(seed_select, cycle_reset)

# Now, 'root' contains the POWL model for the urban vertical farm process.