import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
structure_build  = Transition(label='Structure Build')
system_install   = Transition(label='System Install')
climate_setup    = Transition(label='Climate Setup')
nutrient_prep    = Transition(label='Nutrient Prep')
seed_germinate   = Transition(label='Seed Germinate')
planting_phase   = Transition(label='Planting Phase')
sensor_deploy    = Transition(label='Sensor Deploy')
water_monitor    = Transition(label='Water Monitor')
data_analyze     = Transition(label='Data Analyze')
pest_control     = Transition(label='Pest Control')
staff_train      = Transition(label='Staff Train')
community_meet   = Transition(label='Community Meet')
yield_forecast   = Transition(label='Yield Forecast')

# Build the main production phase as a partial order
production_phase = StrictPartialOrder(nodes=[
    climate_setup, nutrient_prep, seed_germinate, planting_phase,
    sensor_deploy, water_monitor, data_analyze, pest_control
])
# Define the control-flow dependencies for the production phase
production_phase.order.add_edge(climate_setup, nutrient_prep)
production_phase.order.add_edge(nutrient_prep, seed_germinate)
production_phase.order.add_edge(seed_germinate, planting_phase)
production_phase.order.add_edge(planting_phase, sensor_deploy)
production_phase.order.add_edge(sensor_deploy, water_monitor)
production_phase.order.add_edge(water_monitor, data_analyze)
production_phase.order.add_edge(data_analyze, pest_control)

# Define the root partial order, which includes the setup and the production phase
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, structure_build, system_install,
    production_phase, staff_train, community_meet, yield_forecast
])
# Add edges to connect the setup with the production phase
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, production_phase)
root.order.add_edge(production_phase, staff_train)
root.order.add_edge(staff_train, community_meet)
root.order.add_edge(community_meet, yield_forecast)