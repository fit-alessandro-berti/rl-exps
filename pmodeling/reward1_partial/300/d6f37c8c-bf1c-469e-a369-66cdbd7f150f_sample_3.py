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

# Define loop nodes
loop_component_order = OperatorPOWL(operator=Operator.LOOP, children=[component_order, firmware_build])
loop_battery_test = OperatorPOWL(operator=Operator.LOOP, children=[battery_test, sensor_install, motor_mount])

# Define partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    design_draft,
    loop_component_order,
    skip,
    loop_battery_test,
    ai_module,
    system_integrate,
    flight_simulate,
    stress_test,
    compliance_check,
    quality_audit,
    package_drone,
    delivery_plan
])

# Define dependencies
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, loop_component_order)
root.order.add_edge(loop_component_order, skip)
root.order.add_edge(skip, loop_battery_test)
root.order.add_edge(loop_battery_test, ai_module)
root.order.add_edge(ai_module, system_integrate)
root.order.add_edge(system_integrate, flight_simulate)
root.order.add_edge(flight_simulate, stress_test)
root.order.add_edge(stress_test, compliance_check)
root.order.add_edge(compliance_check, quality_audit)
root.order.add_edge(quality_audit, package_drone)
root.order.add_edge(package_drone, delivery_plan)

# Print the root node
print(root)