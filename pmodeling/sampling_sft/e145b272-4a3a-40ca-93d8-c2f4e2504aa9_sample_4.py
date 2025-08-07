import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
permit_filing    = Transition(label='Permit Filing')
system_design    = Transition(label='System Design')
modular_build    = Transition(label='Modular Build')
climate_setup    = Transition(label='Climate Setup')
sensor_install   = Transition(label='Sensor Install')
nutrient_mix     = Transition(label='Nutrient Mix')
waste_setup      = Transition(label='Waste Setup')
iot_deploy       = Transition(label='IoT Deploy')
energy_audit     = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
crop_planting    = Transition(label='Crop Planting')
ai_scheduling    = Transition(label='AI Scheduling')
yield_monitor    = Transition(label='Yield Monitor')
data_analysis    = Transition(label='Data Analysis')
system_upgrade   = Transition(label='System Upgrade')

# Define the loop for continuous yield monitoring and analysis
loop_body = StrictPartialOrder(nodes=[yield_monitor, data_analysis, system_upgrade])
loop_body.order.add_edge(yield_monitor, data_analysis)
loop_body.order.add_edge(data_analysis, system_upgrade)

# Define the loop: repeat AI scheduling and loop_body until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_scheduling, loop_body])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_filing, system_design, modular_build,
    climate_setup, sensor_install, nutrient_mix, waste_setup,
    iot_deploy, energy_audit, compliance_check,
    crop_planting, loop
])

# Add the control-flow dependencies
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, system_design)
root.order.add_edge(system_design, modular_build)
root.order.add_edge(modular_build, climate_setup)
root.order.add_edge(climate_setup, sensor_install)
root.order.add_edge(sensor_install, nutrient_mix)
root.order.add_edge(nutrient_mix, waste_setup)
root.order.add_edge(waste_setup, iot_deploy)
root.order.add_edge(iot_deploy, energy_audit)
root.order.add_edge(energy_audit, compliance_check)
root.order.add_edge(compliance_check, crop_planting)
root.order.add_edge(crop_planting, loop)