import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
modular_design = Transition(label='Modular Design')
material_sourcing = Transition(label='Material Sourcing')
energy_integration = Transition(label='Energy Integration')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
system_assembly = Transition(label='System Assembly')
automation_config = Transition(label='Automation Config')
crop_seeding = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
waste_handling = Transition(label='Waste Handling')
community_meet = Transition(label='Community Meet')
data_analysis = Transition(label='Data Analysis')
feedback_loop = Transition(label='Feedback Loop')
yield_forecast = Transition(label='Yield Forecast')

skip = SilentTransition()

site_survey_to_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[site_survey, regulation_check])
regulation_check_to_modular_design = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, modular_design])
modular_design_to_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[modular_design, material_sourcing])
material_sourcing_to_energy_integration = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, energy_integration])
energy_integration_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[energy_integration, climate_setup])
climate_setup_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
nutrient_mix_to_system_assembly = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, system_assembly])
system_assembly_to_automation_config = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, automation_config])
automation_config_to_crop_seeding = OperatorPOWL(operator=Operator.XOR, children=[automation_config, crop_seeding])
crop_seeding_to_growth_monitoring = OperatorPOWL(operator=Operator.XOR, children=[crop_seeding, growth_monitoring])
growth_monitoring_to_waste_handling = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, waste_handling])
waste_handling_to_community_meet = OperatorPOWL(operator=Operator.XOR, children=[waste_handling, community_meet])
community_meet_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[community_meet, data_analysis])
data_analysis_to_feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, feedback_loop])
feedback_loop_to_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, yield_forecast])

root = StrictPartialOrder(nodes=[
    site_survey_to_regulation_check,
    regulation_check_to_modular_design,
    modular_design_to_material_sourcing,
    material_sourcing_to_energy_integration,
    energy_integration_to_climate_setup,
    climate_setup_to_nutrient_mix,
    nutrient_mix_to_system_assembly,
    system_assembly_to_automation_config,
    automation_config_to_crop_seeding,
    crop_seeding_to_growth_monitoring,
    growth_monitoring_to_waste_handling,
    waste_handling_to_community_meet,
    community_meet_to_data_analysis,
    data_analysis_to_feedback_loop,
    feedback_loop_to_yield_forecast
])

root.order.add_edge(site_survey_to_regulation_check, regulation_check_to_modular_design)
root.order.add_edge(regulation_check_to_modular_design, modular_design_to_material_sourcing)
root.order.add_edge(modular_design_to_material_sourcing, material_sourcing_to_energy_integration)
root.order.add_edge(material_sourcing_to_energy_integration, energy_integration_to_climate_setup)
root.order.add_edge(energy_integration_to_climate_setup, climate_setup_to_nutrient_mix)
root.order.add_edge(climate_setup_to_nutrient_mix, nutrient_mix_to_system_assembly)
root.order.add_edge(nutrient_mix_to_system_assembly, system_assembly_to_automation_config)
root.order.add_edge(system_assembly_to_automation_config, automation_config_to_crop_seeding)
root.order.add_edge(automation_config_to_crop_seeding, crop_seeding_to_growth_monitoring)
root.order.add_edge(crop_seeding_to_growth_monitoring, growth_monitoring_to_waste_handling)
root.order.add_edge(growth_monitoring_to_waste_handling, waste_handling_to_community_meet)
root.order.add_edge(waste_handling_to_community_meet, community_meet_to_data_analysis)
root.order.add_edge(community_meet_to_data_analysis, data_analysis_to_feedback_loop)
root.order.add_edge(data_analysis_to_feedback_loop, feedback_loop_to_yield_forecast)