import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
site_assess    = Transition(label='Site Assess')
env_analysis   = Transition(label='Env Analysis')
modular_install= Transition(label='Modular Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_selection = Transition(label='Crop Selection')
nutrient_mix   = Transition(label='Nutrient Mix')
lighting_cal   = Transition(label='Lighting Calibrate')
pest_monitor   = Transition(label='Pest Monitor')
staff_train    = Transition(label='Staff Training')
energy_integrate = Transition(label='Energy Integrate')
data_analytics = Transition(label='Data Analytics')
waste_recycle  = Transition(label='Waste Recycle')
market_dev     = Transition(label='Market Develop')
yield_optimize = Transition(label='Yield Optimize')
climate_sim    = Transition(label='Climate Simulate')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_assess, env_analysis, modular_install,
    irrigation_setup, crop_selection, nutrient_mix, lighting_cal,
    pest_monitor, staff_train, energy_integrate,
    data_analytics, waste_recycle, market_dev,
    yield_optimize, climate_sim
])

# Sequential dependencies
root.order.add_edge(site_assess, env_analysis)
root.order.add_edge(env_analysis, modular_install)
root.order.add_edge(modular_install, irrigation_setup)
root.order.add_edge(irrigation_setup, crop_selection)
root.order.add_edge(crop_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, lighting_cal)
root.order.add_edge(lighting_cal, pest_monitor)
root.order.add_edge(pest_monitor, staff_train)
root.order.add_edge(staff_train, energy_integrate)
root.order.add_edge(energy_integrate, data_analytics)
root.order.add_edge(data_analytics, waste_recycle)
root.order.add_edge(waste_recycle, market_dev)
root.order.add_edge(market_dev, yield_optimize)
root.order.add_edge(yield_optimize, climate_sim)