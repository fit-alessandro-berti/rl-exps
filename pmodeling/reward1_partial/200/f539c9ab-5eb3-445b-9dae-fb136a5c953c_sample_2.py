from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config = Transition(label='Climate Config')
nutrient_mix = Transition(label='Nutrient Mix')
pest_detect = Transition(label='Pest Detect')
lighting_setup = Transition(label='Lighting Setup')
energy_audit = Transition(label='Energy Audit')
automation_install = Transition(label='Automation Install')
staff_training = Transition(label='Staff Training')
market_analysis = Transition(label='Market Analysis')
regulation_check = Transition(label='Regulation Check')
yield_monitor = Transition(label='Yield Monitor')
waste_manage = Transition(label='Waste Manage')
data_analytics = Transition(label='Data Analytics')

skip = SilentTransition()

site_survey_xor_structural_audit = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit])
modular_design_xor_hydroponic_setup = OperatorPOWL(operator=Operator.XOR, children=[modular_design, hydroponic_setup])
climate_config_xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[climate_config, nutrient_mix])
pest_detect_xor_lighting_setup = OperatorPOWL(operator=Operator.XOR, children=[pest_detect, lighting_setup])
energy_audit_xor_automation_install = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, automation_install])
staff_training_xor_market_analysis = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_analysis])
regulation_check_xor_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, yield_monitor])
waste_manage_xor_data_analytics = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, data_analytics])

root = StrictPartialOrder(nodes=[
    site_survey_xor_structural_audit,
    modular_design_xor_hydroponic_setup,
    climate_config_xor_nutrient_mix,
    pest_detect_xor_lighting_setup,
    energy_audit_xor_automation_install,
    staff_training_xor_market_analysis,
    regulation_check_xor_yield_monitor,
    waste_manage_xor_data_analytics
])

root.order.add_edge(site_survey_xor_structural_audit, modular_design_xor_hydroponic_setup)
root.order.add_edge(modular_design_xor_hydroponic_setup, climate_config_xor_nutrient_mix)
root.order.add_edge(climate_config_xor_nutrient_mix, pest_detect_xor_lighting_setup)
root.order.add_edge(pest_detect_xor_lighting_setup, energy_audit_xor_automation_install)
root.order.add_edge(energy_audit_xor_automation_install, staff_training_xor_market_analysis)
root.order.add_edge(staff_training_xor_market_analysis, regulation_check_xor_yield_monitor)
root.order.add_edge(regulation_check_xor_yield_monitor, waste_manage_xor_data_analytics)