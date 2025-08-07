import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, module_build, system_install, water_prep, seed_selection, nutrient_mix, climate_setup, sensor_deploy, pest_scan, growth_monitor, data_sync, energy_manage, harvest_plan, community_link])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, module_build)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(site_survey, water_prep)
root.order.add_edge(site_survey, seed_selection)
root.order.add_edge(site_survey, nutrient_mix)
root.order.add_edge(site_survey, climate_setup)
root.order.add_edge(site_survey, sensor_deploy)
root.order.add_edge(site_survey, pest_scan)
root.order.add_edge(site_survey, growth_monitor)
root.order.add_edge(site_survey, data_sync)
root.order.add_edge(site_survey, energy_manage)
root.order.add_edge(site_survey, harvest_plan)
root.order.add_edge(site_survey, community_link)

# Save the root of the POWL model
# No explicit saving is required in this context as the 'root' object is the final result.