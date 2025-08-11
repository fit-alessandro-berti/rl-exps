import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define exclusive choice for sensor deployment
xor_sensor = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, skip])

# Define exclusive choice for pest scanning
xor_pest = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, skip])

# Define exclusive choice for growth monitoring
xor_growth = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define exclusive choice for data synchronization
xor_data = OperatorPOWL(operator=Operator.XOR, children=[data_sync, skip])

# Define exclusive choice for energy management
xor_energy = OperatorPOWL(operator=Operator.XOR, children=[energy_manage, skip])

# Define exclusive choice for harvest planning
xor_harvest = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, skip])

# Define exclusive choice for community linking
xor_community = OperatorPOWL(operator=Operator.XOR, children=[community_link, skip])

# Define the loop for water preparation and nutrient mix
loop_water = OperatorPOWL(operator=Operator.LOOP, children=[water_prep, nutrient_mix])

# Define the loop for climate setup
loop_climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, xor_sensor])

# Define the loop for pest scanning
loop_pest = OperatorPOWL(operator=Operator.LOOP, children=[xor_pest, skip])

# Define the loop for growth monitoring
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[xor_growth, skip])

# Define the loop for data synchronization
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[xor_data, skip])

# Define the loop for energy management
loop_energy = OperatorPOWL(operator=Operator.LOOP, children=[xor_energy, skip])

# Define the loop for harvest planning
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[xor_harvest, skip])

# Define the loop for community linking
loop_community = OperatorPOWL(operator=Operator.LOOP, children=[xor_community, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, module_build, system_install, loop_water, loop_climate, loop_pest, loop_growth, loop_data, loop_energy, loop_harvest, loop_community])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, loop_water)
root.order.add_edge(loop_water, loop_climate)
root.order.add_edge(loop_climate, loop_pest)
root.order.add_edge(loop_pest, loop_growth)
root.order.add_edge(loop_growth, loop_data)
root.order.add_edge(loop_data, loop_energy)
root.order.add_edge(loop_energy, loop_harvest)
root.order.add_edge(loop_harvest, loop_community)
root.order.add_edge(loop_community, system_install)