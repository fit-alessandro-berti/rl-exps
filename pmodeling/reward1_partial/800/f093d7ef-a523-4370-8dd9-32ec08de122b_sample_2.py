import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Module Build': Transition(label='Module Build'),
    'System Install': Transition(label='System Install'),
    'Water Prep': Transition(label='Water Prep'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Sensor Deploy': Transition(label='Sensor Deploy'),
    'Pest Scan': Transition(label='Pest Scan'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Data Sync': Transition(label='Data Sync'),
    'Energy Manage': Transition(label='Energy Manage'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Community Link': Transition(label='Community Link')
}

# Define the process using the defined activities
site_survey = activities['Site Survey']
design_layout = activities['Design Layout']
module_build = activities['Module Build']
system_install = activities['System Install']
water_prep = activities['Water Prep']
seed_selection = activities['Seed Selection']
nutrient_mix = activities['Nutrient Mix']
climate_setup = activities['Climate Setup']
sensor_deploy = activities['Sensor Deploy']
pest_scan = activities['Pest Scan']
growth_monitor = activities['Growth Monitor']
data_sync = activities['Data Sync']
energy_manage = activities['Energy Manage']
harvest_plan = activities['Harvest Plan']
community_link = activities['Community Link']

# Construct the Partial Order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, module_build, system_install,
    water_prep, seed_selection, nutrient_mix, climate_setup,
    sensor_deploy, pest_scan, growth_monitor, data_sync,
    energy_manage, harvest_plan, community_link
])

# Define dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, water_prep)
root.order.add_edge(water_prep, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_scan)
root.order.add_edge(pest_scan, growth_monitor)
root.order.add_edge(growth_monitor, data_sync)
root.order.add_edge(data_sync, energy_manage)
root.order.add_edge(energy_manage, harvest_plan)
root.order.add_edge(harvest_plan, community_link)

print(root)