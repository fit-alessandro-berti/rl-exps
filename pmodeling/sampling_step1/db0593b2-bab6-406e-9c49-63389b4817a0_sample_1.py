import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define the dependencies
root.order.add_edge(site_assess, env_analysis)
root.order.add_edge(env_analysis, modular_install)
root.order.add_edge(modular_install, irrigation_setup)
root.order.add_edge(irrigation_setup, crop_selection)
root.order.add_edge(crop_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, lighting_calibrate)
root.order.add_edge(lighting_calibrate, pest_monitor)
root.order.add_edge(pest_monitor, staff_training)
root.order.add_edge(staff_training, energy_integrate)
root.order.add_edge(energy_integrate, data_analytics)
root.order.add_edge(data_analytics, waste_recycle)
root.order.add_edge(waste_recycle, market_develop)
root.order.add_edge(market_develop, yield_optimize)
root.order.add_edge(yield_optimize, climate_simulate)

# Print the root to check the model
print(root)