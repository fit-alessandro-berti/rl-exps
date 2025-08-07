import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_select     = Transition(label='Seed Select')
climate_map     = Transition(label='Climate Map')
iot_setup       = Transition(label='IoT Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
sensor_check    = Transition(label='Sensor Check')
light_adjust    = Transition(label='Light Adjust')
water_cycle     = Transition(label='Water Cycle')
pest_scan       = Transition(label='Pest Scan')
growth_audit    = Transition(label='Growth Audit')
harvest_plan    = Transition(label='Harvest Plan')
demand_sync     = Transition(label='Demand Sync')
quality_grade   = Transition(label='Quality Grade')
pack_items      = Transition(label='Pack Items')
waste_compost   = Transition(label='Waste Compost')
data_review     = Transition(label='Data Review')
cycle_reset     = Transition(label='Cycle Reset')

# Define the main production cycle as a strict partial order
main_cycle = StrictPartialOrder(nodes=[
    seed_select, climate_map, iot_setup, nutrient_mix,
    sensor_check, light_adjust, water_cycle, pest_scan,
    growth_audit, harvest_plan, demand_sync, quality_grade,
    pack_items, waste_compost, data_review, cycle_reset
])

# Define the control-flow dependencies for the main cycle
main_cycle.order.add_edge(seed_select, climate_map)
main_cycle.order.add_edge(climate_map, iot_setup)
main_cycle.order.add_edge(iot_setup, nutrient_mix)
main_cycle.order.add_edge(nutrient_mix, sensor_check)
main_cycle.order.add_edge(sensor_check, light_adjust)
main_cycle.order.add_edge(light_adjust, water_cycle)
main_cycle.order.add_edge(water_cycle, pest_scan)
main_cycle.order.add_edge(pest_scan, growth_audit)
main_cycle.order.add_edge(growth_audit, harvest_plan)
main_cycle.order.add_edge(harvest_plan, demand_sync)
main_cycle.order.add_edge(demand_sync, quality_grade)
main_cycle.order.add_edge(quality_grade, pack_items)
main_cycle.order.add_edge(pack_items, waste_compost)
main_cycle.order.add_edge(waste_compost, data_review)
main_cycle.order.add_edge(data_review, cycle_reset)

# Define the loop: execute the main cycle, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[main_cycle, cycle_reset])

# The final root POWL model is the adaptive cycle loop
root = loop