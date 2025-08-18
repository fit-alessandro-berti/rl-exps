import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define partial order nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[system_design, permit_filing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[modular_build, sensor_install])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[waste_setup, iot_deploy])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[ai_scheduling, energy_audit])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, crop_planting])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, data_analysis])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[system_upgrade, skip])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, yield_monitor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, data_analysis])

# Create root partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, xor1, xor2])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, xor1)
root.order.add_edge(loop8, xor2)
root.order.add_edge(xor1, xor2)

# Print the root
print(root)