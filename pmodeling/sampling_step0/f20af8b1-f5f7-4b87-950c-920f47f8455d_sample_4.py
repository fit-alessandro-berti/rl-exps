import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
modular_build = Transition(label='Modular Build')
hydroponic_setup = Transition(label='Hydroponic Setup')
seed_select = Transition(label='Seed Select')
nutrient_prep = Transition(label='Nutrient Prep')
climate_calibrate = Transition(label='Climate Calibrate')
sensor_install = Transition(label='Sensor Install')
ai_integration = Transition(label='AI Integration')
crop_monitor = Transition(label='Crop Monitor')
growth_adjust = Transition(label='Growth Adjust')
harvest_sort = Transition(label='Harvest Sort')
packaging = Transition(label='Packaging')
distribution_plan = Transition(label='Distribution Plan')
sustain_audit = Transition(label='Sustain Audit')
energy_optimize = Transition(label='Energy Optimize')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ai_integration, distribution_plan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sustain_audit, energy_optimize])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[crop_monitor, growth_adjust])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[harvest_sort, packaging])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, env_analysis, modular_build, hydroponic_setup, seed_select, nutrient_prep, climate_calibrate, sensor_install, xor1, xor2, loop1, loop2])
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, modular_build)
root.order.add_edge(modular_build, hydroponic_setup)
root.order.add_edge(hydroponic_setup, seed_select)
root.order.add_edge(seed_select, nutrient_prep)
root.order.add_edge(nutrient_prep, climate_calibrate)
root.order.add_edge(climate_calibrate, sensor_install)
root.order.add_edge(sensor_install, xor1)
root.order.add_edge(xor1, crop_monitor)
root.order.add_edge(xor1, growth_adjust)
root.order.add_edge(crop_monitor, xor2)
root.order.add_edge(growth_adjust, xor2)
root.order.add_edge(xor2, harvest_sort)
root.order.add_edge(xor2, packaging)
root.order.add_edge(harvest_sort, loop1)
root.order.add_edge(packaging, loop1)
root.order.add_edge(loop1, distribution_plan)
root.order.add_edge(distribution_plan, loop2)
root.order.add_edge(loop2, sustain_audit)
root.order.add_edge(sustain_audit, loop2)
root.order.add_edge(loop2, energy_optimize)

# Print the root
print(root)