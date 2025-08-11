import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the workflow
client_brief -> design_draft
design_draft -> component_order
component_order -> firmware_build
firmware_build -> pcb_assembly
pcb_assembly -> sensor_install
sensor_install -> motor_mount
motor_mount -> battery_test
battery_test -> ai_module
ai_module -> system_integrate
system_integrate -> flight_simulate
flight_simulate -> stress_test
stress_test -> compliance_check
compliance_check -> quality_audit
quality_audit -> package_drone
package_drone -> delivery_plan

root = StrictPartialOrder(nodes=[client_brief, design_draft, component_order, firmware_build, pcb_assembly, sensor_install, motor_mount, battery_test, ai_module, system_integrate, flight_simulate, stress_test, compliance_check, quality_audit, package_drone, delivery_plan])