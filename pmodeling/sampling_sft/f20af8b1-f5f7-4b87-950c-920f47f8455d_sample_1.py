import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey    = Transition(label='Site Survey')
env_analysis   = Transition(label='Env Analysis')
modular_build  = Transition(label='Modular Build')
hydroponic_setup = Transition(label='Hydroponic Setup')
seed_select    = Transition(label='Seed Select')
nutrient_prep  = Transition(label='Nutrient Prep')
climate_calibrate = Transition(label='Climate Calibrate')
sensor_install = Transition(label='Sensor Install')
ai_integration = Transition(label='AI Integration')
crop_monitor   = Transition(label='Crop Monitor')
growth_adjust  = Transition(label='Growth Adjust')
harvest_sort   = Transition(label='Harvest Sort')
packaging      = Transition(label='Packaging')
distribution_plan = Transition(label='Distribution Plan')
sustain_audit  = Transition(label='Sustain Audit')
energy_optimize = Transition(label='Energy Optimize')

# Define the monitoring and adjustment loop
# Body A: Crop Monitor -> Growth Adjust
body_A = StrictPartialOrder(nodes=[crop_monitor, growth_adjust])
body_A.order.add_edge(crop_monitor, growth_adjust)

# Body B: Sustain Audit -> Energy Optimize
body_B = StrictPartialOrder(nodes=[sustain_audit, energy_optimize])
body_B.order.add_edge(sustain_audit, energy_optimize)

# Loop: do Body A, then either exit or do Body B and repeat Body A
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_A, body_B])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    env_analysis,
    modular_build,
    hydroponic_setup,
    seed_select,
    nutrient_prep,
    climate_calibrate,
    sensor_install,
    ai_integration,
    monitor_loop,
    harvest_sort,
    packaging,
    distribution_plan
])

# Define the control-flow edges
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, modular_build)
root.order.add_edge(modular_build, hydroponic_setup)
root.order.add_edge(hydroponic_setup, seed_select)
root.order.add_edge(seed_select, nutrient_prep)
root.order.add_edge(nutrient_prep, climate_calibrate)
root.order.add_edge(climate_calibrate, sensor_install)
root.order.add_edge(sensor_install, ai_integration)
root.order.add_edge(ai_integration, monitor_loop)
root.order.add_edge(monitor_loop, harvest_sort)
root.order.add_edge(harvest_sort, packaging)
root.order.add_edge(packaging, distribution_plan)