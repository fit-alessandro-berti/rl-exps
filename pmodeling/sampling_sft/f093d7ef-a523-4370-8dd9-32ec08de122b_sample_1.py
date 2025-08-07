import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
module_build    = Transition(label='Module Build')
system_install  = Transition(label='System Install')
water_prep      = Transition(label='Water Prep')
seed_selection  = Transition(label='Seed Selection')
nutrient_mix    = Transition(label='Nutrient Mix')
climate_setup   = Transition(label='Climate Setup')
sensor_deploy   = Transition(label='Sensor Deploy')
pest_scan       = Transition(label='Pest Scan')
growth_monitor  = Transition(label='Growth Monitor')
data_sync       = Transition(label='Data Sync')
energy_manage   = Transition(label='Energy Manage')
harvest_plan    = Transition(label='Harvest Plan')
community_link  = Transition(label='Community Link')

# Define the monitoring & data collection loop: Growth Monitor then optionally Data Sync and Energy Manage
loop_body = StrictPartialOrder(nodes=[growth_monitor, data_sync, energy_manage])
loop_body.order.add_edge(growth_monitor, data_sync)
loop_body.order.add_edge(data_sync, energy_manage)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, loop_body])

# Build the overall partial order
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
    pest_scan,
    monitor_loop,
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
root.order.add_edge(sensor_deploy, pest_scan)
root.order.add_edge(pest_scan, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, community_link)