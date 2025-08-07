import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
seed_select   = Transition(label='Seed Select')
climate_map   = Transition(label='Climate Map')
iot_setup     = Transition(label='IoT Setup')
nutrient_mix  = Transition(label='Nutrient Mix')
sensor_check  = Transition(label='Sensor Check')
light_adjust  = Transition(label='Light Adjust')
water_cycle   = Transition(label='Water Cycle')
pest_scan     = Transition(label='Pest Scan')
growth_audit  = Transition(label='Growth Audit')
harvest_plan  = Transition(label='Harvest Plan')
demand_sync   = Transition(label='Demand Sync')
quality_grade = Transition(label='Quality Grade')
pack_items    = Transition(label='Pack Items')
waste_compost = Transition(label='Waste Compost')
data_review   = Transition(label='Data Review')
cycle_reset   = Transition(label='Cycle Reset')

# Define the monitoring & optimization sub-process: Sensor Check -> [Light Adjust, Water Cycle, Pest Scan] -> Growth Audit
monitoring = StrictPartialOrder(nodes=[sensor_check, light_adjust, water_cycle, pest_scan, growth_audit])
monitoring.order.add_edge(sensor_check, light_adjust)
monitoring.order.add_edge(sensor_check, water_cycle)
monitoring.order.add_edge(sensor_check, pest_scan)
monitoring.order.add_edge(light_adjust, growth_audit)
monitoring.order.add_edge(water_cycle, growth_audit)
monitoring.order.add_edge(pest_scan, growth_audit)

# Define the cycle‐reset sub-process: Harvest Plan -> Demand Sync -> Quality Grade -> Pack Items -> Waste Compost
cycle_reset_sub = StrictPartialOrder(nodes=[harvest_plan, demand_sync, quality_grade, pack_items, waste_compost])
cycle_reset_sub.order.add_edge(harvest_plan, demand_sync)
cycle_reset_sub.order.add_edge(demand_sync, quality_grade)
cycle_reset_sub.order.add_edge(quality_grade, pack_items)
cycle_reset_sub.order.add_edge(pack_items, waste_compost)

# Define the main loop: cycle‐reset sub-process repeated until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_reset_sub, cycle_reset])

# Assemble the overall root partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    climate_map,
    iot_setup,
    nutrient_mix,
    monitoring,
    data_review,
    loop
])

# Define the control‐flow dependencies
root.order.add_edge(seed_select, climate_map)
root.order.add_edge(climate_map, iot_setup)
root.order.add_edge(iot_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, monitoring)
root.order.add_edge(monitoring, data_review)
root.order.add_edge(data_review, loop)