import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions (if any)
skip = SilentTransition()

# Create operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[climate_simulate, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, nutrient_mix, lighting_calibrate, pest_monitor, data_analytics, waste_recycle, market_develop, yield_optimize])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[energy_integrate, skip])

# Construct the partial order
root = StrictPartialOrder(nodes=[site_assess, env_analysis, modular_install, xor1, xor2, loop, xor3])
root.order.add_edge(site_assess, env_analysis)
root.order.add_edge(env_analysis, modular_install)
root.order.add_edge(modular_install, xor1)
root.order.add_edge(xor1, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, yield_optimize)