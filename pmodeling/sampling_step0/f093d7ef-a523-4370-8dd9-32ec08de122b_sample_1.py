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

# Step 1: Site Survey
# Step 2: Design Layout
# Step 3: Module Build
# Step 4: System Install
# Step 5: Water Prep
# Step 6: Seed Selection
# Step 7: Nutrient Mix
# Step 8: Climate Setup
# Step 9: Sensor Deploy
# Step 10: Pest Scan
# Step 11: Growth Monitor
# Step 12: Data Sync
# Step 13: Energy Manage
# Step 14: Harvest Plan
# Step 15: Community Link

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    site_survey, design_layout, module_build, system_install, water_prep, seed_selection, nutrient_mix, climate_setup, sensor_deploy, pest_scan, growth_monitor, data_sync, energy_manage, harvest_plan, community_link
])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, loop)

print(root)