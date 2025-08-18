import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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

# Define the loop for nutrient mix and climate setup
loop_nutrient_climate = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, climate_setup])

# Define the XOR for pest control and staff training
xor_pest_staff = OperatorPOWL(operator=Operator.XOR, children=[pest_control, staff_train])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, env_analysis, module_design, seed_selection, loop_nutrient_climate, xor_pest_staff, yield_forecast, market_plan, data_review])
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, module_design)
root.order.add_edge(module_design, seed_selection)
root.order.add_edge(seed_selection, loop_nutrient_climate)
root.order.add_edge(loop_nutrient_climate, xor_pest_staff)
root.order.add_edge(xor_pest_staff, yield_forecast)
root.order.add_edge(yield_forecast, market_plan)
root.order.add_edge(market_plan, data_review)