import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Create a strict partial order with all activities
root = StrictPartialOrder(nodes=[site_survey, design_layout, module_build, system_install, water_prep, seed_selection, nutrient_mix, climate_setup, sensor_deploy, pest_scan, growth_monitor, data_sync, energy_manage, harvest_plan, community_link])

# Add dependencies as needed
# For example, 'Site Survey' should happen before 'Design Layout'
root.order.add_edge(site_survey, design_layout)
# Add more dependencies as per the process flow

# The 'root' variable now contains the POWL model for the urban vertical farm process