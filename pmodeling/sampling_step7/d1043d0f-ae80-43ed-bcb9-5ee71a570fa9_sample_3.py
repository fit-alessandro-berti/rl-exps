import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, env_analysis, module_design, seed_selection, nutrient_mix, climate_setup, led_install, sensor_deploy, pest_control, waste_recycle, hydro_test, staff_train, yield_forecast, market_plan, data_review])

# Add edges to represent the dependencies between activities
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

print(root)