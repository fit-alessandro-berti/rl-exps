import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
climate_plan = Transition(label='Climate Plan')
system_design = Transition(label='System Design')
ai_setup = Transition(label='AI Setup')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_mix = Transition(label='Nutrient Mix')
install_hydro = Transition(label='Install Hydro')
energy_audit = Transition(label='Energy Audit')
staff_training = Transition(label='Staff Training')
trial_growth = Transition(label='Trial Growth')
yield_measure = Transition(label='Yield Measure')
waste_cycle = Transition(label='Waste Cycle')
compliance_check = Transition(label='Compliance Check')
market_study = Transition(label='Market Study')
community_meet = Transition(label='Community Meet')
optimize_environment = Transition(label='Optimize Environment')

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design, climate_plan])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[ai_setup, site_survey])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add dependencies between nodes
root.order.add_edge(site_survey, climate_plan)
root.order.add_edge(climate_plan, system_design)
root.order.add_edge(system_design, ai_setup)
root.order.add_edge(ai_setup, staff_training)
root.order.add_edge(staff_training, trial_growth)
root.order.add_edge(trial_growth, yield_measure)
root.order.add_edge(yield_measure, waste_cycle)
root.order.add_edge(waste_cycle, compliance_check)
root.order.add_edge(compliance_check, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, optimize_environment)