import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transition for skipping certain activities
skip = SilentTransition()

# Define partial order for the process
root = StrictPartialOrder(nodes=[
    site_survey,
    system_design,
    permit_filing,
    modular_build,
    sensor_install,
    climate_setup,
    nutrient_mix,
    waste_setup,
    iot_deploy,
    ai_scheduling,
    energy_audit,
    compliance_check,
    crop_planting,
    yield_monitor,
    data_analysis,
    system_upgrade
])

# Define dependencies between activities
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

print(root)