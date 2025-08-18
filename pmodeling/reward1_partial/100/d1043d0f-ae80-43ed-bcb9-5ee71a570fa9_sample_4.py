import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, waste_recycle])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[hydro_test, sensor_deploy])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[market_plan, data_review])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, led_install])

root = StrictPartialOrder(nodes=[site_survey, env_analysis, module_design, loop1, loop2, xor1, xor2, xor3, yield_forecast])
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, module_design)
root.order.add_edge(module_design, loop1)
root.order.add_edge(module_design, loop2)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, yield_forecast)