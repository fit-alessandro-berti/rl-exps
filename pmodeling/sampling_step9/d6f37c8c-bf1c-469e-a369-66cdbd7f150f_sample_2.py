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

# Define silent transitions (if any)
skip = SilentTransition()

# Define loops and choices
component_loop = OperatorPOWL(operator=Operator.LOOP, children=[component_order, firmware_build, pcb_assembly])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, motor_mount, battery_test])
ai_module_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_module, system_integrate, flight_simulate])
stress_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[stress_test, compliance_check, quality_audit])
package_delivery = OperatorPOWL(operator=Operator.LOOP, children=[package_drone, delivery_plan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    client_brief, design_draft, component_loop, sensor_loop, ai_module_loop, stress_test_loop, package_delivery
])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, component_loop)
root.order.add_edge(component_loop, sensor_loop)
root.order.add_edge(sensor_loop, ai_module_loop)
root.order.add_edge(ai_module_loop, stress_test_loop)
root.order.add_edge(stress_test_loop, package_delivery)

print(root)