from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    env_analysis,
    modular_install,
    irrigation_setup,
    crop_selection,
    nutrient_mix,
    lighting_calibrate,
    pest_monitor,
    staff_training,
    energy_integrate,
    data_analytics,
    waste_recycle,
    market_develop,
    yield_optimize,
    climate_simulate
])

# Define the dependencies between activities
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

root.order.add_edge(env_analysis, modular_install)
root.order.add_edge(env_analysis, irrigation_setup)
root.order.add_edge(env_analysis, crop_selection)
root.order.add_edge(env_analysis, nutrient_mix)
root.order.add_edge(env_analysis, lighting_calibrate)
root.order.add_edge(env_analysis, pest_monitor)
root.order.add_edge(env_analysis, staff_training)
root.order.add_edge(env_analysis, energy_integrate)
root.order.add_edge(env_analysis, data_analytics)
root.order.add_edge(env_analysis, waste_recycle)
root.order.add_edge(env_analysis, market_develop)
root.order.add_edge(env_analysis, yield_optimize)
root.order.add_edge(env_analysis, climate_simulate)

root.order.add_edge(modular_install, irrigation_setup)
root.order.add_edge(modular_install, crop_selection)
root.order.add_edge(modular_install, nutrient_mix)
root.order.add_edge(modular_install, lighting_calibrate)
root.order.add_edge(modular_install, pest_monitor)
root.order.add_edge(modular_install, staff_training)
root.order.add_edge(modular_install, energy_integrate)
root.order.add_edge(modular_install, data_analytics)
root.order.add_edge(modular_install, waste_recycle)
root.order.add_edge(modular_install, market_develop)
root.order.add_edge(modular_install, yield_optimize)
root.order.add_edge(modular_install, climate_simulate)

root.order.add_edge(irrigation_setup, crop_selection)
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(irrigation_setup, lighting_calibrate)
root.order.add_edge(irrigation_setup, pest_monitor)
root.order.add_edge(irrigation_setup, staff_training)
root.order.add_edge(irrigation_setup, energy_integrate)
root.order.add_edge(irrigation_setup, data_analytics)
root.order.add_edge(irrigation_setup, waste_recycle)
root.order.add_edge(irrigation_setup, market_develop)
root.order.add_edge(irrigation_setup, yield_optimize)
root.order.add_edge(irrigation_setup, climate_simulate)

root.order.add_edge(crop_selection, nutrient_mix)
root.order.add_edge(crop_selection, lighting_calibrate)
root.order.add_edge(crop_selection, pest_monitor)
root.order.add_edge(crop_selection, staff_training)
root.order.add_edge(crop_selection, energy_integrate)
root.order.add_edge(crop_selection, data_analytics)
root.order.add_edge(crop_selection, waste_recycle)
root.order.add_edge(crop_selection, market_develop)
root.order.add_edge(crop_selection, yield_optimize)
root.order.add_edge(crop_selection, climate_simulate)

root.order.add_edge(nutrient_mix, lighting_calibrate)
root.order.add_edge(nutrient_mix, pest_monitor)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(nutrient_mix, energy_integrate)
root.order.add_edge(nutrient_mix, data_analytics)
root.order.add_edge(nutrient_mix, waste_recycle)
root.order.add_edge(nutrient_mix, market_develop)
root.order.add_edge(nutrient_mix, yield_optimize)
root.order.add_edge(nutrient_mix, climate_simulate)

root.order.add_edge(lighting_calibrate, pest_monitor)
root.order.add_edge(lighting_calibrate, staff_training)
root.order.add_edge(lighting_calibrate, energy_integrate)
root.order.add_edge(lighting_calibrate, data_analytics)
root.order.add_edge(lighting_calibrate, waste_recycle)
root.order.add_edge(lighting_calibrate, market_develop)
root.order.add_edge(lighting_calibrate, yield_optimize)
root.order.add_edge(lighting_calibrate, climate_simulate)

root.order.add_edge(pest_monitor, staff_training)
root.order.add_edge(pest_monitor, energy_integrate)
root.order.add_edge(pest_monitor, data_analytics)
root.order.add_edge(pest_monitor, waste_recycle)
root.order.add_edge(pest_monitor, market_develop)
root.order.add_edge(pest_monitor, yield_optimize)
root.order.add_edge(pest_monitor, climate_simulate)

root.order.add_edge(staff_training, energy_integrate)
root.order.add_edge(staff_training, data_analytics)
root.order.add_edge(staff_training, waste_recycle)
root.order.add_edge(staff_training, market_develop)
root.order.add_edge(staff_training, yield_optimize)
root.order.add_edge(staff_training, climate_simulate)

root.order.add_edge(energy_integrate, data_analytics)
root.order.add_edge(energy_integrate, waste_recycle)
root.order.add_edge(energy_integrate, market_develop)
root.order.add_edge(energy_integrate, yield_optimize)
root.order.add_edge(energy_integrate, climate_simulate)

root.order.add_edge(data_analytics, waste_recycle)
root.order.add_edge(data_analytics, market_develop)
root.order.add_edge(data_analytics, yield_optimize)
root.order.add_edge(data_analytics, climate_simulate)

root.order.add_edge(waste_recycle, market_develop)
root.order.add_edge(waste_recycle, yield_optimize)
root.order.add_edge(waste_recycle, climate_simulate)

root.order.add_edge(market_develop, yield_optimize)
root.order.add_edge(market_develop, climate_simulate)

root.order.add_edge(yield_optimize, climate_simulate)

# Return the final root model
return root