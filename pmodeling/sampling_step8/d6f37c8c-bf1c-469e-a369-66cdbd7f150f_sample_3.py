from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

skip = SilentTransition()

# Define the workflow
client_brief_to_design_draft = OperatorPOWL(operator=Operator.XOR, children=[client_brief, skip])
design_draft_to_component_order = OperatorPOWL(operator=Operator.XOR, children=[design_draft, skip])
component_order_to_firmware_build = OperatorPOWL(operator=Operator.XOR, children=[component_order, skip])
firmware_build_to_pcb_assembly = OperatorPOWL(operator=Operator.XOR, children=[firmware_build, skip])
pcb_assembly_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[pcb_assembly, skip])
sensor_install_to_motor_mount = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
motor_mount_to_battery_test = OperatorPOWL(operator=Operator.XOR, children=[motor_mount, skip])
battery_test_to_ai_module = OperatorPOWL(operator=Operator.XOR, children=[battery_test, skip])
ai_module_to_system_integrate = OperatorPOWL(operator=Operator.XOR, children=[ai_module, skip])
system_integrate_to_flight_simulate = OperatorPOWL(operator=Operator.XOR, children=[system_integrate, skip])
flight_simulate_to_stress_test = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, skip])
stress_test_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
compliance_check_to_quality_audit = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
quality_audit_to_package_drone = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
package_drone_to_delivery_plan = OperatorPOWL(operator=Operator.XOR, children=[package_drone, skip])

# Connect the nodes
root = StrictPartialOrder(nodes=[
    client_brief_to_design_draft,
    design_draft_to_component_order,
    component_order_to_firmware_build,
    firmware_build_to_pcb_assembly,
    pcb_assembly_to_sensor_install,
    sensor_install_to_motor_mount,
    motor_mount_to_battery_test,
    battery_test_to_ai_module,
    ai_module_to_system_integrate,
    system_integrate_to_flight_simulate,
    flight_simulate_to_stress_test,
    stress_test_to_compliance_check,
    compliance_check_to_quality_audit,
    quality_audit_to_package_drone,
    package_drone_to_delivery_plan
])
root.order.add_edge(client_brief_to_design_draft, design_draft_to_component_order)
root.order.add_edge(design_draft_to_component_order, component_order_to_firmware_build)
root.order.add_edge(component_order_to_firmware_build, firmware_build_to_pcb_assembly)
root.order.add_edge(firmware_build_to_pcb_assembly, pcb_assembly_to_sensor_install)
root.order.add_edge(pcb_assembly_to_sensor_install, sensor_install_to_motor_mount)
root.order.add_edge(sensor_install_to_motor_mount, motor_mount_to_battery_test)
root.order.add_edge(motor_mount_to_battery_test, battery_test_to_ai_module)
root.order.add_edge(battery_test_to_ai_module, ai_module_to_system_integrate)
root.order.add_edge(ai_module_to_system_integrate, system_integrate_to_flight_simulate)
root.order.add_edge(system_integrate_to_flight_simulate, flight_simulate_to_stress_test)
root.order.add_edge(flight_simulate_to_stress_test, stress_test_to_compliance_check)
root.order.add_edge(stress_test_to_compliance_check, compliance_check_to_quality_audit)
root.order.add_edge(compliance_check_to_quality_audit, quality_audit_to_package_drone)
root.order.add_edge(quality_audit_to_package_drone, package_drone_to_delivery_plan)