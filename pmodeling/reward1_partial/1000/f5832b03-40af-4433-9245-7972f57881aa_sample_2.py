import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
legal_review = Transition(label='Legal Review')
tech_sourcing = Transition(label='Tech Sourcing')
structural_build = Transition(label='Structural Build')
climate_setup = Transition(label='Climate Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
crop_select = Transition(label='Crop Select')
nutrient_prep = Transition(label='Nutrient Prep')
waste_system = Transition(label='Waste System')
automation_config = Transition(label='Automation Config')
trial_growth = Transition(label='Trial Growth')
data_analysis = Transition(label='Data Analysis')
quality_audit = Transition(label='Quality Audit')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')

skip = SilentTransition()

# Define the process structure
site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[design_layout, legal_review])
legal_review_to_tech_sourcing = OperatorPOWL(operator=Operator.XOR, children=[legal_review, tech_sourcing])
tech_sourcing_to_structural_build = OperatorPOWL(operator=Operator.XOR, children=[tech_sourcing, structural_build])
structural_build_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[structural_build, climate_setup])
climate_setup_to_irrigation_install = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, irrigation_install])
irrigation_install_to_sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[irrigation_install, sensor_deploy])
sensor_deploy_to_crop_select = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, crop_select])
crop_select_to_nutrient_prep = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_prep])
nutrient_prep_to_waste_system = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, waste_system])
waste_system_to_automation_config = OperatorPOWL(operator=Operator.XOR, children=[waste_system, automation_config])
automation_config_to_trial_growth = OperatorPOWL(operator=Operator.XOR, children=[automation_config, trial_growth])
trial_growth_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[trial_growth, data_analysis])
data_analysis_to_quality_audit = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, quality_audit])
quality_audit_to_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, stakeholder_meet])
stakeholder_meet_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, compliance_check])

# Define the order of execution
root = StrictPartialOrder(nodes=[
    site_survey_to_design_layout,
    design_layout_to_legal_review,
    legal_review_to_tech_sourcing,
    tech_sourcing_to_structural_build,
    structural_build_to_climate_setup,
    climate_setup_to_irrigation_install,
    irrigation_install_to_sensor_deploy,
    sensor_deploy_to_crop_select,
    crop_select_to_nutrient_prep,
    nutrient_prep_to_waste_system,
    waste_system_to_automation_config,
    automation_config_to_trial_growth,
    trial_growth_to_data_analysis,
    data_analysis_to_quality_audit,
    quality_audit_to_stakeholder_meet,
    stakeholder_meet_to_compliance_check
])

root.order.add_edge(site_survey_to_design_layout, design_layout_to_legal_review)
root.order.add_edge(design_layout_to_legal_review, legal_review_to_tech_sourcing)
root.order.add_edge(legal_review_to_tech_sourcing, tech_sourcing_to_structural_build)
root.order.add_edge(tech_sourcing_to_structural_build, structural_build_to_climate_setup)
root.order.add_edge(structural_build_to_climate_setup, climate_setup_to_irrigation_install)
root.order.add_edge(climate_setup_to_irrigation_install, irrigation_install_to_sensor_deploy)
root.order.add_edge(irrigation_install_to_sensor_deploy, sensor_deploy_to_crop_select)
root.order.add_edge(sensor_deploy_to_crop_select, crop_select_to_nutrient_prep)
root.order.add_edge(crop_select_to_nutrient_prep, nutrient_prep_to_waste_system)
root.order.add_edge(nutrient_prep_to_waste_system, waste_system_to_automation_config)
root.order.add_edge(waste_system_to_automation_config, automation_config_to_trial_growth)
root.order.add_edge(automation_config_to_trial_growth, trial_growth_to_data_analysis)
root.order.add_edge(trial_growth_to_data_analysis, data_analysis_to_quality_audit)
root.order.add_edge(data_analysis_to_quality_audit, quality_audit_to_stakeholder_meet)
root.order.add_edge(quality_audit_to_stakeholder_meet, stakeholder_meet_to_compliance_check)

print(root)