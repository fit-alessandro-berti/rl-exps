from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
permit_filing = Transition(label='Permit Filing')
modular_build = Transition(label='Modular Build')
sensor_install = Transition(label='Sensor Install')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
waste_setup = Transition(label='Waste Setup')
iot_deploy = Transition(label='IoT Deploy')
ai_scheduling = Transition(label='AI Scheduling')
energy_audit = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
crop_planting = Transition(label='Crop Planting')
yield_monitor = Transition(label='Yield Monitor')
data_analysis = Transition(label='Data Analysis')
system_upgrade = Transition(label='System Upgrade')

site_survey_to_system_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, system_design])
system_design_to_permit_filing = OperatorPOWL(operator=Operator.XOR, children=[system_design, permit_filing])
permit_filing_to_modular_build = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, modular_build])
modular_build_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[modular_build, sensor_install])
sensor_install_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, climate_setup])
climate_setup_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
nutrient_mix_to_waste_setup = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, waste_setup])
waste_setup_to_iot_deploy = OperatorPOWL(operator=Operator.XOR, children=[waste_setup, iot_deploy])
iot_deploy_to_ai_scheduling = OperatorPOWL(operator=Operator.XOR, children=[iot_deploy, ai_scheduling])
ai_scheduling_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[ai_scheduling, energy_audit])
energy_audit_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, compliance_check])
compliance_check_to_crop_planting = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, crop_planting])
crop_planting_to_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, yield_monitor])
yield_monitor_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, data_analysis])
data_analysis_to_system_upgrade = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, system_upgrade])

root = StrictPartialOrder(nodes=[
    site_survey_to_system_design,
    system_design_to_permit_filing,
    permit_filing_to_modular_build,
    modular_build_to_sensor_install,
    sensor_install_to_climate_setup,
    climate_setup_to_nutrient_mix,
    nutrient_mix_to_waste_setup,
    waste_setup_to_iot_deploy,
    iot_deploy_to_ai_scheduling,
    ai_scheduling_to_energy_audit,
    energy_audit_to_compliance_check,
    compliance_check_to_crop_planting,
    crop_planting_to_yield_monitor,
    yield_monitor_to_data_analysis,
    data_analysis_to_system_upgrade
])

root.order.add_edge(site_survey_to_system_design, system_design_to_permit_filing)
root.order.add_edge(system_design_to_permit_filing, permit_filing_to_modular_build)
root.order.add_edge(permit_filing_to_modular_build, modular_build_to_sensor_install)
root.order.add_edge(modular_build_to_sensor_install, sensor_install_to_climate_setup)
root.order.add_edge(sensor_install_to_climate_setup, climate_setup_to_nutrient_mix)
root.order.add_edge(climate_setup_to_nutrient_mix, nutrient_mix_to_waste_setup)
root.order.add_edge(nutrient_mix_to_waste_setup, waste_setup_to_iot_deploy)
root.order.add_edge(waste_setup_to_iot_deploy, iot_deploy_to_ai_scheduling)
root.order.add_edge(iot_deploy_to_ai_scheduling, ai_scheduling_to_energy_audit)
root.order.add_edge(ai_scheduling_to_energy_audit, energy_audit_to_compliance_check)
root.order.add_edge(energy_audit_to_compliance_check, compliance_check_to_crop_planting)
root.order.add_edge(compliance_check_to_crop_planting, crop_planting_to_yield_monitor)
root.order.add_edge(crop_planting_to_yield_monitor, yield_monitor_to_data_analysis)
root.order.add_edge(yield_monitor_to_data_analysis, data_analysis_to_system_upgrade)