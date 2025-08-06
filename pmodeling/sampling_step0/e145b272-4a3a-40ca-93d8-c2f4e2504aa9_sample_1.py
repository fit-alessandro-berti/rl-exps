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

# Define silent transitions for empty labels
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define loops and exclusive choices
site_assessment = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, system_design, permit_filing])
module_build = OperatorPOWL(operator=Operator.LOOP, children=[modular_build, sensor_install, climate_setup, nutrient_mix, waste_setup, iot_deploy, ai_scheduling, energy_audit, compliance_check])
crop_operations = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip1, yield_monitor, data_analysis, system_upgrade])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_assessment, module_build, crop_operations])
root.order.add_edge(site_assessment, module_build)
root.order.add_edge(module_build, crop_operations)

print(root)