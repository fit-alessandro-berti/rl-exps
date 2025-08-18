import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the dependencies
root = StrictPartialOrder(nodes=[site_assess, env_analysis, modular_install, irrigation_setup, crop_selection, nutrient_mix, lighting_calibrate, pest_monitor, staff_training, energy_integrate, data_analytics, waste_recycle, market_develop, yield_optimize, climate_simulate])
root.order.add_edge(site_assess, env_analysis)
root.order.add_edge(site_assess, modular_install)
root.order.add_edge(site_assess, irrigation_setup)
root.order.add_edge(site_assess, crop_selection)
root.order.add_edge(site_assess, nutrient_mix)
root.order.add_edge(site_assess, lighting_calibrate)
root.order.add_edge(site_assess, pest_monitor)
root.order.add_edge(site_assess, staff_training)
root.order.add_edge(site_assess, energy_integrate)
root.order.add_edge(site_assess, data_analytics)
root.order.add_edge(site_assess, waste_recycle)
root.order.add_edge(site_assess, market_develop)
root.order.add_edge(site_assess, yield_optimize)
root.order.add_edge(site_assess, climate_simulate)