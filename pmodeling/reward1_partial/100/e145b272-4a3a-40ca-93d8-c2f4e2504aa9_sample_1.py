import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the relationships between the activities
site_survey_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[site_survey, system_design])
system_design_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[system_design, permit_filing])
permit_filing_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[permit_filing, modular_build])
modular_build_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[modular_build, sensor_install])
sensor_install_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[sensor_install, climate_setup])
climate_setup_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[climate_setup, nutrient_mix])
nutrient_mix_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[nutrient_mix, waste_setup])
waste_setup_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[waste_setup, iot_deploy])
iot_deploy_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[iot_deploy, ai_scheduling])
ai_scheduling_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[ai_scheduling, energy_audit])
energy_audit_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[energy_audit, compliance_check])
compliance_check_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[compliance_check, crop_planting])
crop_planting_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[crop_planting, yield_monitor])
yield_monitor_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[yield_monitor, data_analysis])
data_analysis_next = OperatorPOWL(operator=Operator.SEQUENCE, children=[data_analysis, system_upgrade])

# Define the root node
root = StrictPartialOrder(nodes=[site_survey_next, system_design_next, permit_filing_next, modular_build_next, sensor_install_next, climate_setup_next, nutrient_mix_next, waste_setup_next, iot_deploy_next, ai_scheduling_next, energy_audit_next, compliance_check_next, crop_planting_next, yield_monitor_next, data_analysis_next, system_upgrade])
root.order.add_edge(site_survey_next, system_design_next)
root.order.add_edge(system_design_next, permit_filing_next)
root.order.add_edge(permit_filing_next, modular_build_next)
root.order.add_edge(modular_build_next, sensor_install_next)
root.order.add_edge(sensor_install_next, climate_setup_next)
root.order.add_edge(climate_setup_next, nutrient_mix_next)
root.order.add_edge(nutrient_mix_next, waste_setup_next)
root.order.add_edge(waste_setup_next, iot_deploy_next)
root.order.add_edge(iot_deploy_next, ai_scheduling_next)
root.order.add_edge(ai_scheduling_next, energy_audit_next)
root.order.add_edge(energy_audit_next, compliance_check_next)
root.order.add_edge(compliance_check_next, crop_planting_next)
root.order.add_edge(crop_planting_next, yield_monitor_next)
root.order.add_edge(yield_monitor_next, data_analysis_next)
root.order.add_edge(data_analysis_next, system_upgrade)

# Print the root node
print(root)