import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice nodes
env_and_modular = OperatorPOWL(operator=Operator.XOR, children=[env_analysis, modular_build])
hydro_and_seed = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, seed_select])
nutrient_and_calibrate = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, climate_calibrate])
sensor_and_ai = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, ai_integration])
monitor_and_growth = OperatorPOWL(operator=Operator.XOR, children=[crop_monitor, growth_adjust])
sort_and_packaging = OperatorPOWL(operator=Operator.XOR, children=[harvest_sort, packaging])
plan_and_distribution = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, packaging])
audit_and_optimize = OperatorPOWL(operator=Operator.XOR, children=[sustain_audit, energy_optimize])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[env_and_modular, hydro_and_seed])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_and_ai, monitor_and_growth])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[sort_and_packaging, plan_and_distribution])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[audit_and_optimize, energy_optimize])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, skip)