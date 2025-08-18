import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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
loop_water_prep = OperatorPOWL(operator=Operator.LOOP, children=[water_prep, seed_selection, nutrient_mix, climate_setup, sensor_deploy])
loop_growth_monitor = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, growth_monitor, data_sync, energy_manage, harvest_plan])

# Define XOR nodes
xor_community_link = OperatorPOWL(operator=Operator.XOR, children=[community_link])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, module_build, system_install, loop_water_prep, loop_growth_monitor, xor_community_link])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, loop_water_prep)
root.order.add_edge(loop_water_prep, loop_growth_monitor)
root.order.add_edge(loop_growth_monitor, xor_community_link)

# Print the root POWL model
print(root)