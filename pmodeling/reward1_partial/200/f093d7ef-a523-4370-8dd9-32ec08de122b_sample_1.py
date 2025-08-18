from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
module_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[module_build, skip])
data_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_sync, skip])

# Define exclusive choice nodes
sensor_deploy_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, skip])
pest_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    module_build_loop,
    system_install,
    water_prep,
    seed_selection,
    nutrient_mix,
    climate_setup,
    sensor_deploy_choice,
    pest_scan_choice,
    growth_monitor,
    data_sync_loop,
    energy_manage,
    harvest_plan,
    community_link
])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build_loop)
root.order.add_edge(module_build_loop, system_install)
root.order.add_edge(system_install, water_prep)
root.order.add_edge(water_prep, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, sensor_deploy_choice)
root.order.add_edge(sensor_deploy_choice, pest_scan_choice)
root.order.add_edge(pest_scan_choice, growth_monitor)
root.order.add_edge(growth_monitor, data_sync_loop)
root.order.add_edge(data_sync_loop, energy_manage)
root.order.add_edge(energy_manage, harvest_plan)
root.order.add_edge(harvest_plan, community_link)

print(root)