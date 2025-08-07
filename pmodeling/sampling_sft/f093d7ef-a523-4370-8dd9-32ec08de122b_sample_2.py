import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
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
growth_monitor    = Transition(label='Growth Monitor')
data_sync         = Transition(label='Data Sync')
pest_scan         = Transition(label='Pest Scan')
harvest_plan      = Transition(label='Harvest Plan')
community_link    = Transition(label='Community Link')

# Define the data sync loop: monitor growth data, then optionally sync data and repeat
data_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, data_sync]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    module_build,
    system_install,
    water_prep,
    seed_selection,
    nutrient_mix,
    climate_setup,
    sensor_deploy,
    energy_manage,
    data_loop,
    pest_scan,
    harvest_plan,
    community_link
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, water_prep)
root.order.add_edge(water_prep, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, energy_manage)
root.order.add_edge(energy_manage, data_loop)
root.order.add_edge(data_loop, pest_scan)
root.order.add_edge(pest_scan, harvest_plan)
root.order.add_edge(harvest_plan, community_link)

# Add optional pest scan → data sync loop edge
root.order.add_edge(pest_scan, data_loop)

# Run the model to verify its structure
# pm4py.view_powl(root, format='svg', show_labels=True)