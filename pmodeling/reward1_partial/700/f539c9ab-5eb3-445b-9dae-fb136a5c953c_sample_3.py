import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process steps
site_survey_to_structural_audit = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
structural_audit_to_modular_design = OperatorPOWL(operator=Operator.LOOP, children=[structural_audit, modular_design])
modular_design_to_hydroponic_setup = OperatorPOWL(operator=Operator.LOOP, children=[modular_design, hydroponic_setup])
hydroponic_setup_to_climate_config = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, climate_config])
climate_config_to_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[climate_config, nutrient_mix])
nutrient_mix_to_pest_detect = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, pest_detect])
pest_detect_to_lighting_setup = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect, lighting_setup])
lighting_setup_to_energy_audit = OperatorPOWL(operator=Operator.LOOP, children=[lighting_setup, energy_audit])
energy_audit_to_automation_install = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, automation_install])
automation_install_to_staff_training = OperatorPOWL(operator=Operator.LOOP, children=[automation_install, staff_training])
staff_training_to_market_analysis = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, market_analysis])
market_analysis_to_regulation_check = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis, regulation_check])
regulation_check_to_yield_monitor = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, yield_monitor])
yield_monitor_to_waste_manage = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, waste_manage])
waste_manage_to_data_analytics = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage, data_analytics])

# Define the root node
root = StrictPartialOrder(nodes=[site_survey_to_structural_audit, structural_audit_to_modular_design, modular_design_to_hydroponic_setup, hydroponic_setup_to_climate_config, climate_config_to_nutrient_mix, nutrient_mix_to_pest_detect, pest_detect_to_lighting_setup, lighting_setup_to_energy_audit, energy_audit_to_automation_install, automation_install_to_staff_training, staff_training_to_market_analysis, market_analysis_to_regulation_check, regulation_check_to_yield_monitor, yield_monitor_to_waste_manage, waste_manage_to_data_analytics])
root.order.add_edge(site_survey_to_structural_audit, structural_audit_to_modular_design)
root.order.add_edge(structural_audit_to_modular_design, modular_design_to_hydroponic_setup)
root.order.add_edge(modular_design_to_hydroponic_setup, hydroponic_setup_to_climate_config)
root.order.add_edge(hydroponic_setup_to_climate_config, climate_config_to_nutrient_mix)
root.order.add_edge(climate_config_to_nutrient_mix, nutrient_mix_to_pest_detect)
root.order.add_edge(nutrient_mix_to_pest_detect, pest_detect_to_lighting_setup)
root.order.add_edge(pest_detect_to_lighting_setup, lighting_setup_to_energy_audit)
root.order.add_edge(lighting_setup_to_energy_audit, energy_audit_to_automation_install)
root.order.add_edge(energy_audit_to_automation_install, automation_install_to_staff_training)
root.order.add_edge(automation_install_to_staff_training, staff_training_to_market_analysis)
root.order.add_edge(staff_training_to_market_analysis, market_analysis_to_regulation_check)
root.order.add_edge(market_analysis_to_regulation_check, regulation_check_to_yield_monitor)
root.order.add_edge(regulation_check_to_yield_monitor, yield_monitor_to_waste_manage)
root.order.add_edge(yield_monitor_to_waste_manage, waste_manage_to_data_analytics)

# Print the root node
print(root)