from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
module_design = Transition(label='Module Design')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
led_install = Transition(label='LED Install')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
waste_recycle = Transition(label='Waste Recycle')
hydro_test = Transition(label='Hydro Test')
staff_train = Transition(label='Staff Train')
yield_forecast = Transition(label='Yield Forecast')
market_plan = Transition(label='Market Plan')
data_review = Transition(label='Data Review')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    env_analysis,
    module_design,
    seed_selection,
    nutrient_mix,
    climate_setup,
    led_install,
    sensor_deploy,
    pest_control,
    waste_recycle,
    hydro_test,
    staff_train,
    yield_forecast,
    market_plan,
    data_review
])

# Since there are no dependencies between the activities, we don't need to define any order edges.
# If there were dependencies, we would add them like this:
# root.order.add_edge(site_survey, env_analysis)
# root.order.add_edge(site_survey, module_design)
# ...

# Save the final result in the variable 'root'
print(root)