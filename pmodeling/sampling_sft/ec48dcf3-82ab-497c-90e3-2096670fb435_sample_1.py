import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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
pest_control    = Transition(label='Pest Control')
data_analyze    = Transition(label='Data Analyze')
yield_forecast  = Transition(label='Yield Forecast')
community_meet  = Transition(label='Community Meet')
staff_train     = Transition(label='Staff Train')

# Loop for continuous monitoring: Water Monitor -> Pest Control -> Data Analyze
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_monitor, pest_control])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_build,
    system_install,
    climate_setup,
    nutrient_prep,
    seed_germinate,
    planting_phase,
    sensor_deploy,
    monitor_loop,
    data_analyze,
    yield_forecast,
    community_meet,
    staff_train
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, planting_phase)
root.order.add_edge(planting_phase, sensor_deploy)
root.order.add_edge(sensor_deploy, monitor_loop)
root.order.add_edge(monitor_loop, data_analyze)
root.order.add_edge(data_analyze, yield_forecast)
root.order.add_edge(yield_forecast, community_meet)
root.order.add_edge(community_meet, staff_train)

# Final edge from the last activity to the end (silently)
root.order.add_edge(staff_train, Transition(label='End'))