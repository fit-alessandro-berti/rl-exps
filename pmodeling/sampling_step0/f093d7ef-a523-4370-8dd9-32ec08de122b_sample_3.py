import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Survey, Design Layout, Module Build, System Install, Water Prep
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, module_build, system_install, water_prep])

# Seed Selection, Nutrient Mix, Climate Setup
xor1 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix, climate_setup])

# Sensor Deploy, Pest Scan, Growth Monitor
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, pest_scan, growth_monitor])

# Data Sync, Energy Manage
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_sync, energy_manage])

# Harvest Plan, Community Link
xor4 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, community_link])

# Create root
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

print(root)