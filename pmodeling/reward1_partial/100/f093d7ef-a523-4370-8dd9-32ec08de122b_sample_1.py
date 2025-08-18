from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the exclusive choices
water_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[water_prep, silent_transition])

# Define the loops
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, water_prep_xor])

# Define the strict partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, module_build, system_install, climate_loop, data_sync, energy_manage, harvest_plan, community_link])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, climate_loop)
root.order.add_edge(climate_loop, data_sync)
root.order.add_edge(data_sync, energy_manage)
root.order.add_edge(energy_manage, harvest_plan)
root.order.add_edge(harvest_plan, community_link)

print(root)