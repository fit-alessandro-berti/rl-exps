from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each transition/transition with empty label as a silent transition
site_survey = SilentTransition(label='Site Survey')
env_analysis = SilentTransition(label='Env Analysis')
module_design = SilentTransition(label='Module Design')
seed_selection = SilentTransition(label='Seed Selection')
nutrient_mix = SilentTransition(label='Nutrient Mix')
climate_setup = SilentTransition(label='Climate Setup')
led_install = SilentTransition(label='LED Install')
sensor_deploy = SilentTransition(label='Sensor Deploy')
pest_control = SilentTransition(label='Pest Control')
waste_recycle = SilentTransition(label='Waste Recycle')
hydro_test = SilentTransition(label='Hydro Test')
staff_train = SilentTransition(label='Staff Train')
yield_forecast = SilentTransition(label='Yield Forecast')
market_plan = SilentTransition(label='Market Plan')
data_review = SilentTransition(label='Data Review')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_survey, env_analysis, module_design, seed_selection, nutrient_mix, climate_setup, led_install,
    sensor_deploy, pest_control, waste_recycle, hydro_test, staff_train, yield_forecast, market_plan, data_review
])

# Define the dependencies (POWL graph)
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, module_design)
root.order.add_edge(module_design, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, led_install)
root.order.add_edge(led_install, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_control)
root.order.add_edge(pest_control, waste_recycle)
root.order.add_edge(waste_recycle, hydro_test)
root.order.add_edge(hydro_test, staff_train)
root.order.add_edge(staff_train, yield_forecast)
root.order.add_edge(yield_forecast, market_plan)
root.order.add_edge(market_plan, data_review)

# Print the final result
print(root)