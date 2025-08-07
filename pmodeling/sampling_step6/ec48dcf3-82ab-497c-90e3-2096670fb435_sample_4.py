from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
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
    pest_control,
    water_monitor,
    data_analyze,
    staff_train,
    yield_forecast,
    community_meet
])

# Define the dependencies (partial order relationships)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, structure_build)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(site_survey, climate_setup)
root.order.add_edge(site_survey, nutrient_prep)
root.order.add_edge(site_survey, seed_germinate)
root.order.add_edge(site_survey, planting_phase)
root.order.add_edge(site_survey, sensor_deploy)
root.order.add_edge(site_survey, pest_control)
root.order.add_edge(site_survey, water_monitor)
root.order.add_edge(site_survey, data_analyze)
root.order.add_edge(site_survey, staff_train)
root.order.add_edge(site_survey, yield_forecast)
root.order.add_edge(site_survey, community_meet)

print("POWL model for urban vertical farm setup:")
print(root)