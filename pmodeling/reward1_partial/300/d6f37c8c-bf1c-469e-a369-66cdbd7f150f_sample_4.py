from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for component sourcing, firmware customization, and assembly
component_loop = OperatorPOWL(operator=Operator.LOOP, children=[component_order, firmware_build, pcb_assembly])

# Define the XOR for sensor installation, motor mounting, and battery testing
sensor_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, motor_mount, battery_test])

# Define the XOR for AI module integration and system integration
ai_xor = OperatorPOWL(operator=Operator.XOR, children=[ai_module, system_integrate])

# Define the loop for stress testing and compliance verification
stress_loop = OperatorPOWL(operator=Operator.LOOP, children=[stress_test, compliance_check])

# Define the XOR for quality audit and final packaging
quality_xor = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, package_drone])

# Define the XOR for delivery plan and final logistics coordination
delivery_xor = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan, package_drone])

# Define the root POWL model
root = StrictPartialOrder(nodes=[client_brief, component_loop, sensor_xor, ai_xor, stress_loop, quality_xor, delivery_xor])
root.order.add_edge(client_brief, component_loop)
root.order.add_edge(component_loop, sensor_xor)
root.order.add_edge(sensor_xor, ai_xor)
root.order.add_edge(ai_xor, stress_loop)
root.order.add_edge(stress_loop, quality_xor)
root.order.add_edge(quality_xor, delivery_xor)