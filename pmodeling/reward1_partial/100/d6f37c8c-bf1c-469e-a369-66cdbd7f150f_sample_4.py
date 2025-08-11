import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Client Brief', 'Design Draft', 'Component Order', 'Firmware Build', 'PCB Assembly', 'Sensor Install', 'Motor Mount', 'Battery Test', 'AI Module', 'System Integrate', 'Flight Simulate', 'Stress Test', 'Compliance Check', 'Quality Audit', 'Package Drone', 'Delivery Plan']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the process steps
client_brief = transitions[0]
design_draft = transitions[1]
component_order = transitions[2]
firmware_build = transitions[3]
pcb_assembly = transitions[4]
sensor_install = transitions[5]
motor_mount = transitions[6]
battery_test = transitions[7]
ai_module = transitions[8]
system_integrate = transitions[9]
flight_simulate = transitions[10]
stress_test = transitions[11]
compliance_check = transitions[12]
quality_audit = transitions[13]
package_drone = transitions[14]
delivery_plan = transitions[15]

# Define the workflow model
root = StrictPartialOrder(nodes=[client_brief, design_draft, component_order, firmware_build, pcb_assembly, sensor_install, motor_mount, battery_test, ai_module, system_integrate, flight_simulate, stress_test, compliance_check, quality_audit, package_drone, delivery_plan])

# Define the dependencies between activities
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(client_brief, component_order)
root.order.add_edge(design_draft, firmware_build)
root.order.add_edge(design_draft, pcb_assembly)
root.order.add_edge(component_order, firmware_build)
root.order.add_edge(component_order, pcb_assembly)
root.order.add_edge(firmware_build, pcb_assembly)
root.order.add_edge(pcb_assembly, sensor_install)
root.order.add_edge(pcb_assembly, motor_mount)
root.order.add_edge(pcb_assembly, battery_test)
root.order.add_edge(sensor_install, system_integrate)
root.order.add_edge(motor_mount, system_integrate)
root.order.add_edge(battery_test, system_integrate)
root.order.add_edge(system_integrate, flight_simulate)
root.order.add_edge(flight_simulate, stress_test)
root.order.add_edge(stress_test, compliance_check)
root.order.add_edge(compliance_check, quality_audit)
root.order.add_edge(quality_audit, package_drone)
root.order.add_edge(package_drone, delivery_plan)

# Print the POWL model
print(root)