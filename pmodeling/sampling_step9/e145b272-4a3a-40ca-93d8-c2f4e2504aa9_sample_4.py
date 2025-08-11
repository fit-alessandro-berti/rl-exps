import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for climate control integration
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix, waste_setup])

# Define the exclusive choice for IoT deployment and AI scheduling
xor = OperatorPOWL(operator=Operator.XOR, children=[iot_deploy, ai_scheduling])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add the remaining activities to the partial order
root.order.add_edge(loop, nutrient_mix)
root.order.add_edge(loop, waste_setup)
root.order.add_edge(loop, climate_setup)
root.order.add_edge(xor, iot_deploy)
root.order.add_edge(xor, ai_scheduling)
root.order.add_edge(xor, system_design)
root.order.add_edge(system_design, modular_build)
root.order.add_edge(modular_build, sensor_install)
root.order.add_edge(sensor_install, system_design)
root.order.add_edge(system_design, permit_filing)
root.order.add_edge(permit_filing, site_survey)
root.order.add_edge(site_survey, crop_planting)
root.order.add_edge(crop_planting, yield_monitor)
root.order.add_edge(yield_monitor, data_analysis)
root.order.add_edge(data_analysis, system_upgrade)
root.order.add_edge(system_upgrade, energy_audit)
root.order.add_edge(energy_audit, compliance_check)