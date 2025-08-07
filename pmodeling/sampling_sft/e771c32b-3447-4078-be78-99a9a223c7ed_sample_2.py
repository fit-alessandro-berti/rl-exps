import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
climate_plan   = Transition(label='Climate Plan')
system_design  = Transition(label='System Design')
ai_setup       = Transition(label='AI Setup')
seed_sourcing  = Transition(label='Seed Sourcing')
nutrient_mix   = Transition(label='Nutrient Mix')
install_hydro  = Transition(label='Install Hydro')
energy_audit   = Transition(label='Energy Audit')
staff_training = Transition(label='Staff Training')
trial_growth   = Transition(label='Trial Growth')
yield_measure  = Transition(label='Yield Measure')
waste_cycle    = Transition(label='Waste Cycle')
compliance_chk = Transition(label='Compliance Check')
market_study   = Transition(label='Market Study')
community_meet = Transition(label='Community Meet')
optimize_env   = Transition(label='Optimize Environment')

# Define the loop for continuous optimization
# A = optimize_environment, B = compliance_check
loop_optimize = OperatorPOWL(
    operator=Operator.LOOP,
    children=[optimize_env, compliance_chk]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    climate_plan,
    system_design,
    ai_setup,
    seed_sourcing,
    nutrient_mix,
    install_hydro,
    energy_audit,
    staff_training,
    trial_growth,
    yield_measure,
    waste_cycle,
    loop_optimize,
    market_study,
    community_meet
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, climate_plan)
root.order.add_edge(climate_plan, system_design)
root.order.add_edge(system_design, ai_setup)
root.order.add_edge(ai_setup, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_mix)
root.order.add_edge(nutrient_mix, install_hydro)
root.order.add_edge(install_hydro, energy_audit)
root.order.add_edge(energy_audit, staff_training)
root.order.add_edge(staff_training, trial_growth)
root.order.add_edge(trial_growth, yield_measure)
root.order.add_edge(yield_measure, waste_cycle)
root.order.add_edge(waste_cycle, loop_optimize)
root.order.add_edge(loop_optimize, market_study)
root.order.add_edge(market_study, community_meet)