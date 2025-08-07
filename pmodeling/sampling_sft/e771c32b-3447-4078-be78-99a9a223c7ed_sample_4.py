import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
climate_plan      = Transition(label='Climate Plan')
system_design     = Transition(label='System Design')
ai_setup          = Transition(label='AI Setup')
seed_sourcing     = Transition(label='Seed Sourcing')
nutrient_mix      = Transition(label='Nutrient Mix')
install_hydro     = Transition(label='Install Hydro')
energy_audit      = Transition(label='Energy Audit')
staff_training    = Transition(label='Staff Training')
trial_growth      = Transition(label='Trial Growth')
yield_measure     = Transition(label='Yield Measure')
waste_cycle       = Transition(label='Waste Cycle')
compliance_check  = Transition(label='Compliance Check')
market_study      = Transition(label='Market Study')
community_meet    = Transition(label='Community Meet')
optimize_env      = Transition(label='Optimize Environment')

# Loop for continuous optimization: do Optimize Environment, then either exit or repeat
loop_optimize = OperatorPOWL(
    operator=Operator.LOOP,
    children=[optimize_env, optimize_env]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_plan, system_design, ai_setup,
    seed_sourcing, nutrient_mix, install_hydro, energy_audit,
    staff_training, trial_growth, yield_measure, waste_cycle,
    compliance_check, market_study, community_meet, loop_optimize
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, climate_plan)
root.order.add_edge(site_survey, system_design)
root.order.add_edge(climate_plan, ai_setup)
root.order.add_edge(system_design, ai_setup)
root.order.add_edge(climate_plan, seed_sourcing)
root.order.add_edge(system_design, seed_sourcing)
root.order.add_edge(climate_plan, nutrient_mix)
root.order.add_edge(system_design, nutrient_mix)
root.order.add_edge(seed_sourcing, install_hydro)
root.order.add_edge(nutrient_mix, install_hydro)
root.order.add_edge(install_hydro, energy_audit)
root.order.add_edge(energy_audit, staff_training)
root.order.add_edge(staff_training, trial_growth)
root.order.add_edge(trial_growth, yield_measure)
root.order.add_edge(yield_measure, waste_cycle)
root.order.add_edge(waste_cycle, compliance_check)
root.order.add_edge(compliance_check, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, loop_optimize)

# Close the loop: after community meet, either exit or repeat optimization
root.order.add_edge(community_meet, loop_optimize)

# Print the root model for verification
print(root)