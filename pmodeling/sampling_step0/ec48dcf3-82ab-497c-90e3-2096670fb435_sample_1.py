import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
seed_germinate = Transition(label='Seed Germinate')
planting_phase = Transition(label='Planting Phase')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
water_monitor = Transition(label='Water Monitor')
data_analyze = Transition(label='Data Analyze')
staff_train = Transition(label='Staff Train')
yield_forecast = Transition(label='Yield Forecast')
community_meet = Transition(label='Community Meet')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, data_analyze])
water_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_monitor, climate_control_loop])
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, climate_control_loop])

pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])

# Define the root node with partial order
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
    pest_control_choice,
    water_monitor_loop,
    yield_forecast_loop,
    community_meet
])

# Define the order of dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, planting_phase)
root.order.add_edge(planting_phase, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_control_choice)
root.order.add_edge(pest_control_choice, water_monitor_loop)
root.order.add_edge(water_monitor_loop, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, climate_control_loop)
root.order.add_edge(climate_control_loop, data_analyze)
root.order.add_edge(data_analyze, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, yield_forecast)
root.order.add_edge(yield_forecast, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, community_meet)

# Print the root
print(root)