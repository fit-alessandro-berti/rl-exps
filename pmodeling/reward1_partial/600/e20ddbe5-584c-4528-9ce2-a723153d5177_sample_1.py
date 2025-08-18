import pm4py

# Define each activity as a Transition object
site_analysis = pm4py.objects.powl.obj.Transition(label='Site Analysis')
load_test = pm4py.objects.powl.obj.Transition(label='Load Test')
sunlight_map = pm4py.objects.powl.obj.Transition(label='Sunlight Map')
medium_select = pm4py.objects.powl.obj.Transition(label='Medium Select')
hydro_design = pm4py.objects.powl.obj.Transition(label='Hydro Design')
procure_seeds = pm4py.objects.powl.obj.Transition(label='Procure Seeds')
install_irrigation = pm4py.objects.powl.obj.Transition(label='Install Irrigation')
setup_climate = pm4py.objects.powl.obj.Transition(label='Setup Climate')
create_schedule = pm4py.objects.powl.obj.Transition(label='Create Schedule')
pest_control = pm4py.objects.powl.obj.Transition(label='Pest Control')
monitor_growth = pm4py.objects.powl.obj.Transition(label='Monitor Growth')
adjust_systems = pm4py.objects.powl.obj.Transition(label='Adjust Systems')
harvest_crops = pm4py.objects.powl.obj.Transition(label='Harvest Crops')
package_produce = pm4py.objects.powl.obj.Transition(label='Package Produce')
engage_community = pm4py.objects.powl.obj.Transition(label='Engage Community')
host_workshops = pm4py.objects.powl.obj.Transition(label='Host Workshops')

# Define the partial order structure
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[
    site_analysis, load_test, sunlight_map, medium_select, hydro_design,
    procure_seeds, install_irrigation, setup_climate, create_schedule,
    pest_control, monitor_growth, adjust_systems, harvest_crops,
    package_produce, engage_community, host_workshops
])

# Add dependencies
root.order.add_edge(site_analysis, load_test)
root.order.add_edge(load_test, sunlight_map)
root.order.add_edge(sunlight_map, medium_select)
root.order.add_edge(medium_select, hydro_design)
root.order.add_edge(hydro_design, procure_seeds)
root.order.add_edge(procure_seeds, install_irrigation)
root.order.add_edge(install_irrigation, setup_climate)
root.order.add_edge(setup_climate, create_schedule)
root.order.add_edge(create_schedule, pest_control)
root.order.add_edge(pest_control, monitor_growth)
root.order.add_edge(monitor_growth, adjust_systems)
root.order.add_edge(adjust_systems, harvest_crops)
root.order.add_edge(harvest_crops, package_produce)
root.order.add_edge(package_produce, engage_community)
root.order.add_edge(engage_community, host_workshops)

print(root)