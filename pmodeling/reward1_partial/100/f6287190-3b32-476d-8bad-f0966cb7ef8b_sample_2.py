import pm4py

# Define the activities
seed_select = pm4py.objects.powl.obj.Transition(label='Seed Select')
climate_map = pm4py.objects.powl.obj.Transition(label='Climate Map')
iot_setup = pm4py.objects.powl.obj.Transition(label='IoT Setup')
nutrient_mix = pm4py.objects.powl.obj.Transition(label='Nutrient Mix')
sensor_check = pm4py.objects.powl.obj.Transition(label='Sensor Check')
light_adjust = pm4py.objects.powl.obj.Transition(label='Light Adjust')
water_cycle = pm4py.objects.powl.obj.Transition(label='Water Cycle')
pest_scan = pm4py.objects.powl.obj.Transition(label='Pest Scan')
growth_audit = pm4py.objects.powl.obj.Transition(label='Growth Audit')
harvest_plan = pm4py.objects.powl.obj.Transition(label='Harvest Plan')
demand_sync = pm4py.objects.powl.obj.Transition(label='Demand Sync')
quality_grade = pm4py.objects.powl.obj.Transition(label='Quality Grade')
pack_items = pm4py.objects.powl.obj.Transition(label='Pack Items')
waste_compost = pm4py.objects.powl.obj.Transition(label='Waste Compost')
data_review = pm4py.objects.powl.obj.Transition(label='Data Review')
cycle_reset = pm4py.objects.powl.obj.Transition(label='Cycle Reset')

# Define the partial order
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[
    seed_select, climate_map, iot_setup, nutrient_mix, sensor_check,
    light_adjust, water_cycle, pest_scan, growth_audit, harvest_plan,
    demand_sync, quality_grade, pack_items, waste_compost, data_review,
    cycle_reset
])

# Define the order edges
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

print(root)