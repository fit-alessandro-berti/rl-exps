from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
analyze_soil = Transition(label='Soil Analyze')
map_site = Transition(label='Site Mapping')
setup_bed = Transition(label='Bed Setup')
select_crop = Transition(label='Crop Select')
deploy_sensor = Transition(label='Sensor Deploy')
adjust_irrigation = Transition(label='Irrigation Adjust')
feed_nutrient = Transition(label='Nutrient Feed')
scout_pest = Transition(label='Pest Scouting')
predict_pest = Transition(label='Pest Predict')
host_workshop = Transition(label='Workshop Host')
rotate_crop = Transition(label='Crop Rotate')
compost_waste = Transition(label='Waste Compost')
recycle_water = Transition(label='Water Recycle')
analyze_data = Transition(label='Data Analyze')
refine_cycle = Transition(label='Cycle Refine')
share_resource = Transition(label='Resource Share')
report_yield = Transition(label='Yield Report')

# Define the partial order
root = StrictPartialOrder(nodes=[
    analyze_soil, map_site, setup_bed, select_crop, deploy_sensor,
    adjust_irrigation, feed_nutrient, scout_pest, predict_pest,
    host_workshop, rotate_crop, compost_waste, recycle_water,
    analyze_data, refine_cycle, share_resource, report_yield
])

# Define the dependencies
root.order.add_edge(analyze_soil, map_site)
root.order.add_edge(map_site, setup_bed)
root.order.add_edge(setup_bed, select_crop)
root.order.add_edge(select_crop, deploy_sensor)
root.order.add_edge(deploy_sensor, adjust_irrigation)
root.order.add_edge(adjust_irrigation, feed_nutrient)
root.order.add_edge(feed_nutrient, scout_pest)
root.order.add_edge(scout_pest, predict_pest)
root.order.add_edge(predict_pest, host_workshop)
root.order.add_edge(host_workshop, rotate_crop)
root.order.add_edge(rotate_crop, compost_waste)
root.order.add_edge(compost_waste, recycle_water)
root.order.add_edge(recycle_water, analyze_data)
root.order.add_edge(analyze_data, refine_cycle)
root.order.add_edge(refine_cycle, share_resource)
root.order.add_edge(share_resource, report_yield)

print(root)