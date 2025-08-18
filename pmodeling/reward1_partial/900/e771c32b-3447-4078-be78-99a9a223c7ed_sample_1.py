import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_to_climate_plan = OperatorPOWL(operator=Operator.XOR, children=[climate_plan, skip])
climate_plan_to_system_design = OperatorPOWL(operator=Operator.XOR, children=[system_design, skip])
system_design_to_ai_setup = OperatorPOWL(operator=Operator.XOR, children=[ai_setup, skip])
ai_setup_to_seed_sourcing = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, skip])
seed_sourcing_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
nutrient_mix_to_install_hydro = OperatorPOWL(operator=Operator.XOR, children=[install_hydro, skip])
install_hydro_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
energy_audit_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
staff_training_to_trial_growth = OperatorPOWL(operator=Operator.XOR, children=[trial_growth, skip])
trial_growth_to_yield_measure = OperatorPOWL(operator=Operator.XOR, children=[yield_measure, skip])
yield_measure_to_waste_cycle = OperatorPOWL(operator=Operator.XOR, children=[waste_cycle, skip])
waste_cycle_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
compliance_check_to_market_study = OperatorPOWL(operator=Operator.XOR, children=[market_study, skip])
market_study_to_community_meet = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
community_meet_to_optimize_environment = OperatorPOWL(operator=Operator.XOR, children=[optimize_environment, skip])

root = StrictPartialOrder(nodes=[
    site_survey, climate_plan, system_design, ai_setup, seed_sourcing, nutrient_mix, install_hydro,
    energy_audit, staff_training, trial_growth, yield_measure, waste_cycle, compliance_check,
    market_study, community_meet, optimize_environment
])

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
root.order.add_edge(waste_cycle, compliance_check)
root.order.add_edge(compliance_check, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, optimize_environment)