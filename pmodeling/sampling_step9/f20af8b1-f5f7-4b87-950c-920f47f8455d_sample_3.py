import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[env_analysis, modular_build, hydroponic_setup])
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_select, nutrient_prep, climate_calibrate, sensor_install, ai_integration])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[crop_monitor, growth_adjust])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[harvest_sort, packaging, distribution_plan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[sustain_audit, energy_optimize])

root = StrictPartialOrder(nodes=[loop, xor, loop2, xor2, loop3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)

# Save the final result in the variable 'root'