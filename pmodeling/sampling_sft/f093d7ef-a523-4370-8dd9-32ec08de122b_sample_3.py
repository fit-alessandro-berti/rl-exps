import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
module_build      = Transition(label='Module Build')
system_install    = Transition(label='System Install')
water_prep        = Transition(label='Water Prep')
seed_selection    = Transition(label='Seed Selection')
nutrient_mix      = Transition(label='Nutrient Mix')
climate_setup     = Transition(label='Climate Setup')
sensor_deploy     = Transition(label='Sensor Deploy')
energy_manage     = Transition(label='Energy Manage')
pest_scan         = Transition(label='Pest Scan')
growth_monitor    = Transition(label='Growth Monitor')
data_sync         = Transition(label='Data Sync')
harvest_plan      = Transition(label='Harvest Plan')
community_link    = Transition(label='Community Link')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, module_build, system_install,
    water_prep, seed_selection, nutrient_mix, climate_setup,
    sensor_deploy, energy_manage, pest_scan, growth_monitor,
    data_sync, harvest_plan, community_link
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(design_layout, system_install)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, water_prep)
root.order.add_edge(system_install, sensor_deploy)
root.order.add_edge(system_install, energy_manage)
root.order.add_edge(water_prep, seed_selection)
root.order.add_edge(water_prep, nutrient_mix)
root.order.add_edge(seed_selection, climate_setup)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, pest_scan)
root.order.add_edge(climate_setup, growth_monitor)
root.order.add_edge(climate_setup, data_sync)
root.order.add_edge(pest_scan, growth_monitor)
root.order.add_edge(growth_monitor, data_sync)
root.order.add_edge(data_sync, harvest_plan)
root.order.add_edge(harvest_plan, community_link)

# Print the root model for verification
print(root)