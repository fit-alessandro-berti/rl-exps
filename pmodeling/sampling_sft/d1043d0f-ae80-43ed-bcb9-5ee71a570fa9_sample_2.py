import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey   = Transition(label='Site Survey')
env_analysis  = Transition(label='Env Analysis')
module_design = Transition(label='Module Design')
seed_selection= Transition(label='Seed Selection')
nutrient_mix  = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
led_install   = Transition(label='LED Install')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control  = Transition(label='Pest Control')
waste_recycle = Transition(label='Waste Recycle')
hydro_test    = Transition(label='Hydro Test')
staff_train   = Transition(label='Staff Train')
yield_forecast= Transition(label='Yield Forecast')
market_plan   = Transition(label='Market Plan')
data_review   = Transition(label='Data Review')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, env_analysis, module_design,
    seed_selection, nutrient_mix, climate_setup, led_install,
    sensor_deploy, pest_control, waste_recycle, hydro_test,
    staff_train, yield_forecast, market_plan, data_review
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, module_design)

root.order.add_edge(module_design, seed_selection)
root.order.add_edge(module_design, nutrient_mix)
root.order.add_edge(module_design, climate_setup)
root.order.add_edge(module_design, led_install)

root.order.add_edge(seed_selection, hydro_test)
root.order.add_edge(nutrient_mix, hydro_test)
root.order.add_edge(climate_setup, hydro_test)
root.order.add_edge(led_install, hydro_test)

root.order.add_edge(hydro_test, pest_control)
root.order.add_edge(hydro_test, waste_recycle)
root.order.add_edge(hydro_test, staff_train)

# Loop for continuous data review and improvement
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, data_review])
root.order.add_edge(hydro_test, loop)

# Final sequential activities
root.order.add_edge(loop, yield_forecast)
root.order.add_edge(yield_forecast, market_plan)

# Print the root model for verification
print(root)