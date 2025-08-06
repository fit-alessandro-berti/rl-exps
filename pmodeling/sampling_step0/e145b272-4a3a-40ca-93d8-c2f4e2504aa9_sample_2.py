import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the transitions for each activity
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
# Define the exclusive choice nodes
site_survey_and_system_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, system_design])
permit_filing_and_modular_build = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, modular_build])
sensor_install_and_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, climate_setup])
nutrient_mix_and_waste_setup = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, waste_setup])
iot_deploy_and_ai_scheduling = OperatorPOWL(operator=Operator.XOR, children=[iot_deploy, ai_scheduling])
energy_audit_and_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, compliance_check])
crop_planting_and_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, yield_monitor])
data_analysis_and_system_upgrade = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, system_upgrade])
# Define the loop nodes
yield_monitor_and_crop_planting = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, crop_planting])
# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_and_system_design, permit_filing_and_modular_build, sensor_install_and_climate_setup, nutrient_mix_and_waste_setup, iot_deploy_and_ai_scheduling, energy_audit_and_compliance_check, crop_planting_and_yield_monitor, data_analysis_and_system_upgrade, yield_monitor_and_crop_planting])
# Add the dependencies
root.order.add_edge(site_survey_and_system_design, permit_filing_and_modular_build)
root.order.add_edge(permit_filing_and_modular_build, sensor_install_and_climate_setup)
root.order.add_edge(sensor_install_and_climate_setup, nutrient_mix_and_waste_setup)
root.order.add_edge(nutrient_mix_and_waste_setup, iot_deploy_and_ai_scheduling)
root.order.add_edge(iot_deploy_and_ai_scheduling, energy_audit_and_compliance_check)
root.order.add_edge(energy_audit_and_compliance_check, crop_planting_and_yield_monitor)
root.order.add_edge(crop_planting_and_yield_monitor, data_analysis_and_system_upgrade)
root.order.add_edge(data_analysis_and_system_upgrade, yield_monitor_and_crop_planting)
root.order.add_edge(yield_monitor_and_crop_planting, yield_monitor_and_crop_planting)