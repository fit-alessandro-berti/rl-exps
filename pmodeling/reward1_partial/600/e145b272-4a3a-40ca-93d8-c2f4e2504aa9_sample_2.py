import pm4py.objects.powl.obj as powl

# Define transitions
site_survey = powl.Transition(label='Site Survey')
system_design = powl.Transition(label='System Design')
permit_filing = powl.Transition(label='Permit Filing')
modular_build = powl.Transition(label='Modular Build')
sensor_install = powl.Transition(label='Sensor Install')
climate_setup = powl.Transition(label='Climate Setup')
nutrient_mix = powl.Transition(label='Nutrient Mix')
waste_setup = powl.Transition(label='Waste Setup')
iot_deploy = powl.Transition(label='IoT Deploy')
ai_scheduling = powl.Transition(label='AI Scheduling')
energy_audit = powl.Transition(label='Energy Audit')
compliance_check = powl.Transition(label='Compliance Check')
crop_planting = powl.Transition(label='Crop Planting')
yield_monitor = powl.Transition(label='Yield Monitor')
data_analysis = powl.Transition(label='Data Analysis')
system_upgrade = powl.Transition(label='System Upgrade')

# Define the partial order
root = powl.StrictPartialOrder(
    nodes=[site_survey, system_design, permit_filing, modular_build, sensor_install, climate_setup, nutrient_mix,
           waste_setup, iot_deploy, ai_scheduling, energy_audit, compliance_check, crop_planting, yield_monitor,
           data_analysis, system_upgrade],
    order={})
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, permit_filing)
root.order.add_edge(permit_filing, modular_build)
root.order.add_edge(modular_build, sensor_install)
root.order.add_edge(sensor_install, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, waste_setup)
root.order.add_edge(waste_setup, iot_deploy)
root.order.add_edge(iot_deploy, ai_scheduling)
root.order.add_edge(ai_scheduling, energy_audit)
root.order.add_edge(energy_audit, compliance_check)
root.order.add_edge(compliance_check, crop_planting)
root.order.add_edge(crop_planting, yield_monitor)
root.order.add_edge(yield_monitor, data_analysis)
root.order.add_edge(data_analysis, system_upgrade)