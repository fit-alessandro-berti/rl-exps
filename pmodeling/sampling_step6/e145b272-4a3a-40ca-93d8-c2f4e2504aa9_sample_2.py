import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) based on the given description
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, system_design, permit_filing, modular_build, sensor_install, climate_setup, nutrient_mix, waste_setup, iot_deploy, ai_scheduling, energy_audit, compliance_check, crop_planting, yield_monitor, data_analysis, system_upgrade])
root.order.add_edge(site_survey, system_design)
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, modular_build)
root.order.add_edge(site_survey, sensor_install)
root.order.add_edge(site_survey, climate_setup)
root.order.add_edge(site_survey, nutrient_mix)
root.order.add_edge(site_survey, waste_setup)
root.order.add_edge(site_survey, iot_deploy)
root.order.add_edge(site_survey, ai_scheduling)
root.order.add_edge(site_survey, energy_audit)
root.order.add_edge(site_survey, compliance_check)
root.order.add_edge(site_survey, crop_planting)
root.order.add_edge(site_survey, yield_monitor)
root.order.add_edge(site_survey, data_analysis)
root.order.add_edge(site_survey, system_upgrade)

# The final result is stored in 'root'