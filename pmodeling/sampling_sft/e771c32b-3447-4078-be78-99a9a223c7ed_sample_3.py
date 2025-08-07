import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the loop body (trial growth, yield measure, waste cycle, compliance check)
body = StrictPartialOrder(nodes=[trial_growth, yield_measure, waste_cycle, compliance_check])
body.order.add_edge(trial_growth, yield_measure)
body.order.add_edge(yield_measure, waste_cycle)
body.order.add_edge(waste_cycle, compliance_check)

# Define the loop: do the trial growth, then repeatedly do the body (trial growth -> yield -> waste -> compliance) until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_growth, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_plan, system_design, ai_setup,
    seed_sourcing, nutrient_mix, install_hydro, energy_audit,
    staff_training, loop,
    market_study, community_meet, optimize_env
])

# Define the control-flow edges
root.order.add_edge(site_survey, climate_plan)
root.order.add_edge(climate_plan, system_design)
root.order.add_edge(system_design, ai_setup)
root.order.add_edge(ai_setup, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_mix)
root.order.add_edge(nutrient_mix, install_hydro)
root.order.add_edge(install_hydro, energy_audit)
root.order.add_edge(energy_audit, staff_training)
root.order.add_edge(staff_training, loop)
root.order.add_edge(loop, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, optimize_env)