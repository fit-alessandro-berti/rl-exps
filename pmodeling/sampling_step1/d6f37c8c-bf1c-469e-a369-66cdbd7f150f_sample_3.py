import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
client_brief = Transition(label='Client Brief')
design_draft = Transition(label='Design Draft')
component_order = Transition(label='Component Order')
firmware_build = Transition(label='Firmware Build')
pcb_assembly = Transition(label='PCB Assembly')
sensor_install = Transition(label='Sensor Install')
motor_mount = Transition(label='Motor Mount')
battery_test = Transition(label='Battery Test')
ai_module = Transition(label='AI Module')
system_integrate = Transition(label='System Integrate')
flight_simulate = Transition(label='Flight Simulate')
stress_test = Transition(label='Stress Test')
compliance_check = Transition(label='Compliance Check')
quality_audit = Transition(label='Quality Audit')
package_drone = Transition(label='Package Drone')
delivery_plan = Transition(label='Delivery Plan')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[client_brief, design_draft])
loop = OperatorPOWL(operator=Operator.LOOP, children=[component_order, firmware_build, pcb_assembly, sensor_install, motor_mount, battery_test, ai_module, system_integrate, flight_simulate, stress_test, compliance_check, quality_audit, package_drone, delivery_plan])
xor.order.add_edge(client_brief, component_order)
xor.order.add_edge(design_draft, component_order)

root = StrictPartialOrder(nodes=[xor, loop])
root.order.add_edge(xor, loop)

# Print the root POWL model
print(root)