import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
module_build = Transition(label='Module Build')
system_install = Transition(label='System Install')
water_prep = Transition(label='Water Prep')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
sensor_deploy = Transition(label='Sensor Deploy')
pest_scan = Transition(label='Pest Scan')
growth_monitor = Transition(label='Growth Monitor')
data_sync = Transition(label='Data Sync')
energy_manage = Transition(label='Energy Manage')
harvest_plan = Transition(label='Harvest Plan')
community_link = Transition(label='Community Link')

# Define the control flow
root.add_node(site_survey)
root.add_node(design_layout)
root.add_node(module_build)
root.add_node(system_install)
root.add_node(water_prep)
root.add_node(seed_selection)
root.add_node(nutrient_mix)
root.add_node(climate_setup)
root.add_node(sensor_deploy)
root.add_node(pest_scan)
root.add_node(growth_monitor)
root.add_node(data_sync)
root.add_node(energy_manage)
root.add_node(harvest_plan)
root.add_node(community_link)

# Define the dependencies
root.add_edge(site_survey, design_layout)
root.add_edge(design_layout, module_build)
root.add_edge(module_build, system_install)
root.add_edge(system_install, water_prep)
root.add_edge(water_prep, seed_selection)
root.add_edge(seed_selection, nutrient_mix)
root.add_edge(nutrient_mix, climate_setup)
root.add_edge(climate_setup, sensor_deploy)
root.add_edge(sensor_deploy, pest_scan)
root.add_edge(pest_scan, growth_monitor)
root.add_edge(growth_monitor, data_sync)
root.add_edge(data_sync, energy_manage)
root.add_edge(energy_manage, harvest_plan)
root.add_edge(harvest_plan, community_link)

# Print the final POWL model
print(root)