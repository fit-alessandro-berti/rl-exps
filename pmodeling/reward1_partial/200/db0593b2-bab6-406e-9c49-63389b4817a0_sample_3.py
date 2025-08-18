from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_assess = Transition(label='Site Assess')
env_analysis = Transition(label='Env Analysis')
modular_install = Transition(label='Modular Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_selection = Transition(label='Crop Selection')
nutrient_mix = Transition(label='Nutrient Mix')
lighting_calibrate = Transition(label='Lighting Calibrate')
pest_monitor = Transition(label='Pest Monitor')
staff_training = Transition(label='Staff Training')
energy_integrate = Transition(label='Energy Integrate')
data_analytics = Transition(label='Data Analytics')
waste_recycle = Transition(label='Waste Recycle')
market_develop = Transition(label='Market Develop')
yield_optimize = Transition(label='Yield Optimize')
climate_simulate = Transition(label='Climate Simulate')

skip = SilentTransition()

site_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_assess, env_analysis])
modular_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_install, irrigation_setup])
crop_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, nutrient_mix])
lighting_calibrate_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_calibrate, pest_monitor])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, energy_integrate])
data_analytics_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analytics, waste_recycle])
market_develop_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_develop, yield_optimize])
climate_simulate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_simulate, skip])

root = StrictPartialOrder(nodes=[
    site_assess_loop, modular_install_loop, crop_selection_loop, lighting_calibrate_loop,
    staff_training_loop, data_analytics_loop, market_develop_loop, climate_simulate_loop
])
root.order.add_edge(site_assess_loop, modular_install_loop)
root.order.add_edge(modular_install_loop, crop_selection_loop)
root.order.add_edge(crop_selection_loop, lighting_calibrate_loop)
root.order.add_edge(lighting_calibrate_loop, staff_training_loop)
root.order.add_edge(staff_training_loop, data_analytics_loop)
root.order.add_edge(data_analytics_loop, market_develop_loop)
root.order.add_edge(market_develop_loop, climate_simulate_loop)