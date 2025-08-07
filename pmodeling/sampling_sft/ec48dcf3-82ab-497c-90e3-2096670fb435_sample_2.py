import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
system_install  = Transition(label='System Install')
climate_setup   = Transition(label='Climate Setup')
nutrient_prep   = Transition(label='Nutrient Prep')
seed_germinate  = Transition(label='Seed Germinate')
planting_phase  = Transition(label='Planting Phase')
sensor_deploy   = Transition(label='Sensor Deploy')
water_monitor   = Transition(label='Water Monitor')
data_analyze    = Transition(label='Data Analyze')
pest_control    = Transition(label='Pest Control')
staff_train     = Transition(label='Staff Train')
community_meet  = Transition(label='Community Meet')
yield_forecast  = Transition(label='Yield Forecast')

# Build the core production loop: Sensor Deploy -> Water Monitor -> Data Analyze -> Pest Control
loop_body = StrictPartialOrder(nodes=[water_monitor, data_analyze, pest_control])
loop_body.order.add_edge(water_monitor, data_analyze)
loop_body.order.add_edge(data_analyze, pest_control)

# Loop operator: repeat Sensor Deploy followed by the loop_body until exit
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, loop_body])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, structure_build, system_install,
    climate_setup, nutrient_prep, seed_germinate, planting_phase,
    production_loop, staff_train, community_meet, yield_forecast
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, planting_phase)
root.order.add_edge(planting_phase, production_loop)
root.order.add_edge(production_loop, staff_train)
root.order.add_edge(staff_train, community_meet)
root.order.add_edge(community_meet, yield_forecast)