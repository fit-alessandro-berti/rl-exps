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

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, env_analysis])
module_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[module_design, seed_selection])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, climate_setup])
led_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[led_install, sensor_deploy])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, waste_recycle])
hydro_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydro_test, staff_train])
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, market_plan])
data_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, yield_forecast])

root = StrictPartialOrder(nodes=[
    site_survey_loop,
    module_design_loop,
    nutrient_mix_loop,
    led_install_loop,
    pest_control_loop,
    hydro_test_loop,
    staff_train,
    yield_forecast,
    market_plan,
    data_review_loop
])

root.order.add_edge(site_survey_loop, module_design_loop)
root.order.add_edge(module_design_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, climate_setup_loop)
root.order.add_edge(climate_setup_loop, led_install_loop)
root.order.add_edge(led_install_loop, sensor_deploy_loop)
root.order.add_edge(sensor_deploy_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, waste_recycle_loop)
root.order.add_edge(waste_recycle_loop, hydro_test_loop)
root.order.add_edge(hydro_test_loop, staff_train)
root.order.add_edge(staff_train, yield_forecast)
root.order.add_edge(yield_forecast, market_plan)
root.order.add_edge(market_plan, data_review_loop)