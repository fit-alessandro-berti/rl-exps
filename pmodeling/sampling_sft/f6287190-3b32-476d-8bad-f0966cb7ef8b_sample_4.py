import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Loop for continuous cycle: after harvest, repeat the process
cycle_body = StrictPartialOrder(nodes=[
    nutrient_mix, sensor_check, light_adjust, water_cycle,
    pest_scan, growth_audit, harvest_plan, demand_sync,
    quality_grade, pack_items, waste_compost, data_review
])
# no order edges => all children run in parallel

# Define the loop: do the body, then optionally reset and do the body again
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, cycle_reset])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    seed_select, climate_map, iot_setup, loop
])
# main flow: setup -> IoT -> continuous cycle
root.order.add_edge(seed_select, iot_setup)
root.order.add_edge(iot_setup, loop)