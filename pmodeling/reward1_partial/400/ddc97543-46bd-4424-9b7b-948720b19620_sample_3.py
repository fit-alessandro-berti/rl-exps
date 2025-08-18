import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
env_control = Transition(label='Env Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_select = Transition(label='Crop Select')
ai_setup = Transition(label='AI Setup')
worker_train = Transition(label='Worker Train')
pest_control = Transition(label='Pest Control')
irrigation_plan = Transition(label='Irrigation Plan')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
market_setup = Transition(label='Market Setup')
logistics_plan = Transition(label='Logistics Plan')
waste_manage = Transition(label='Waste Manage')

loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
loop_structure_prep = OperatorPOWL(operator=Operator.LOOP, children=[structure_prep])
loop_system_install = OperatorPOWL(operator=Operator.LOOP, children=[system_install])
loop_env_control = OperatorPOWL(operator=Operator.LOOP, children=[env_control])
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
loop_crop_select = OperatorPOWL(operator=Operator.LOOP, children=[crop_select])
loop_ai_setup = OperatorPOWL(operator=Operator.LOOP, children=[ai_setup])
loop_worker_train = OperatorPOWL(operator=Operator.LOOP, children=[worker_train])
loop_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
loop_irrigation_plan = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_plan])
loop_data_monitor = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor])
loop_yield_forecast = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast])
loop_energy_audit = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])
loop_market_setup = OperatorPOWL(operator=Operator.LOOP, children=[market_setup])
loop_logistics_plan = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan])
loop_waste_manage = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage])

root = StrictPartialOrder(nodes=[
    loop_site_survey,
    loop_structure_prep,
    loop_system_install,
    loop_env_control,
    loop_nutrient_mix,
    loop_crop_select,
    loop_ai_setup,
    loop_worker_train,
    loop_pest_control,
    loop_irrigation_plan,
    loop_data_monitor,
    loop_yield_forecast,
    loop_energy_audit,
    loop_market_setup,
    loop_logistics_plan,
    loop_waste_manage
])
root.order.add_edge(loop_site_survey, loop_structure_prep)
root.order.add_edge(loop_structure_prep, loop_system_install)
root.order.add_edge(loop_system_install, loop_env_control)
root.order.add_edge(loop_env_control, loop_nutrient_mix)
root.order.add_edge(loop_nutrient_mix, loop_crop_select)
root.order.add_edge(loop_crop_select, loop_ai_setup)
root.order.add_edge(loop_ai_setup, loop_worker_train)
root.order.add_edge(loop_worker_train, loop_pest_control)
root.order.add_edge(loop_pest_control, loop_irrigation_plan)
root.order.add_edge(loop_irrigation_plan, loop_data_monitor)
root.order.add_edge(loop_data_monitor, loop_yield_forecast)
root.order.add_edge(loop_yield_forecast, loop_energy_audit)
root.order.add_edge(loop_energy_audit, loop_market_setup)
root.order.add_edge(loop_market_setup, loop_logistics_plan)
root.order.add_edge(loop_logistics_plan, loop_waste_manage)