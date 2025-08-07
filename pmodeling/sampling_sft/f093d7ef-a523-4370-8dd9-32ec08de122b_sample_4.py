import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
module_build     = Transition(label='Module Build')
system_install   = Transition(label='System Install')
water_prep       = Transition(label='Water Prep')
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_setup    = Transition(label='Climate Setup')
sensor_deploy    = Transition(label='Sensor Deploy')
energy_manage    = Transition(label='Energy Manage')
pest_scan        = Transition(label='Pest Scan')
growth_monitor   = Transition(label='Growth Monitor')
data_sync        = Transition(label='Data Sync')
harvest_plan     = Transition(label='Harvest Plan')
community_link   = Transition(label='Community Link')

# Loop for continuous monitoring and adjustment
loop_monitor = OperatorPOWL(
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
    pest_scan,
    loop_monitor,
    harvest_plan,
    community_link
])

# Sequence: Site Survey -> Design Layout -> Module Build -> System Install -> Water Prep -> Seed Selection -> Nutrient Mix -> Climate Setup -> Sensor Deploy -> Energy Manage
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, water_prep)
root.order.add_edge(water_prep, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, energy_manage)

# After system installation, the monitoring loop starts
root.order.add_edge(system_install, loop_monitor)

# Pest Scan is concurrent with the monitoring loop
root.order.add_edge(system_install, pest_scan)

# After the loop, the harvest plan and community link can proceed
root.order.add_edge(loop_monitor, harvest_plan)
root.order.add_edge(loop_monitor, community_link)

# Final dependencies (no further edges)