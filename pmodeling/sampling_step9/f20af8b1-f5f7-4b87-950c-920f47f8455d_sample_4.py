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

# Define loop activities
loop_activities = [seed_select, nutrient_prep, climate_calibrate, sensor_install, ai_integration, crop_monitor, growth_adjust, harvest_sort, packaging, distribution_plan, sustain_audit, energy_optimize]

loop = OperatorPOWL(operator=Operator.LOOP, children=loop_activities)

# Define XOR activities
xor_activities = [modular_build, hydroponic_setup]

xor = OperatorPOWL(operator=Operator.XOR, children=xor_activities)

# Define root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)