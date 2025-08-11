import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop for AI module integration
ai_module_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_module])

# Define XOR for testing and compliance
xor = OperatorPOWL(operator=Operator.XOR, children=[stress_test, compliance_check])

# Define XOR for quality and delivery
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, delivery_plan])

# Define partial order for the process
root = StrictPartialOrder(nodes=[client_brief, design_draft, component_order, firmware_build, pcb_assembly, sensor_install, motor_mount, battery_test, ai_module_loop, system_integrate, flight_simulate, xor, xor2])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, component_order)
root.order.add_edge(component_order, firmware_build)
root.order.add_edge(firmware_build, pcb_assembly)
root.order.add_edge(pcb_assembly, sensor_install)
root.order.add_edge(sensor_install, motor_mount)
root.order.add_edge(motor_mount, battery_test)
root.order.add_edge(battery_test, ai_module_loop)
root.order.add_edge(ai_module_loop, system_integrate)
root.order.add_edge(system_integrate, flight_simulate)
root.order.add_edge(flight_simulate, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, quality_audit)
root.order.add_edge(xor2, delivery_plan)