import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define transitions
skip = SilentTransition()
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[client_brief, design_draft])
xor_component = OperatorPOWL(operator=Operator.XOR, children=[component_order, skip])
xor_firmware = OperatorPOWL(operator=Operator.XOR, children=[firmware_build, skip])
xor_pcb = OperatorPOWL(operator=Operator.XOR, children=[pcb_assembly, skip])
xor_sensor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
xor_motor = OperatorPOWL(operator=Operator.XOR, children=[motor_mount, skip])
xor_battery = OperatorPOWL(operator=Operator.XOR, children=[battery_test, skip])
xor_ai = OperatorPOWL(operator=Operator.XOR, children=[ai_module, skip])
xor_system = OperatorPOWL(operator=Operator.XOR, children=[system_integrate, skip])
xor_flight = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, skip])
xor_stress = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
xor_package = OperatorPOWL(operator=Operator.XOR, children=[package_drone, skip])
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[
    loop_design,
    xor_component,
    xor_firmware,
    xor_pcb,
    xor_sensor,
    xor_motor,
    xor_battery,
    xor_ai,
    xor_system,
    xor_flight,
    xor_stress,
    xor_compliance,
    xor_quality,
    xor_package,
    xor_delivery
])
root.order.add_edge(loop_design, xor_component)
root.order.add_edge(xor_component, xor_firmware)
root.order.add_edge(xor_firmware, xor_pcb)
root.order.add_edge(xor_pcb, xor_sensor)
root.order.add_edge(xor_sensor, xor_motor)
root.order.add_edge(xor_motor, xor_battery)
root.order.add_edge(xor_battery, xor_ai)
root.order.add_edge(xor_ai, xor_system)
root.order.add_edge(xor_system, xor_flight)
root.order.add_edge(xor_flight, xor_stress)
root.order.add_edge(xor_stress, xor_compliance)
root.order.add_edge(xor_compliance, xor_quality)
root.order.add_edge(xor_quality, xor_package)
root.order.add_edge(xor_package, xor_delivery)

print(root)