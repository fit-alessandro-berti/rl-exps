import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
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

# Define the multi-stage testing partial order
test_nodes = [battery_test, ai_module, flight_simulate, stress_test]
test_order = StrictPartialOrder(nodes=test_nodes)
# No edges between them, they can run in parallel

# Define the main assembly partial order
main_assembly = StrictPartialOrder(nodes=[
    design_draft,
    component_order,
    firmware_build,
    pcb_assembly,
    sensor_install,
    motor_mount,
    system_integrate
])
main_order = [
    (design_draft, component_order),
    (component_order, firmware_build),
    (firmware_build, pcb_assembly),
    (pcb_assembly, sensor_install),
    (sensor_install, motor_mount),
    (motor_mount, system_integrate)
]
for src, tgt in main_order:
    main_assembly.order.add_edge(src, tgt)

# Define the overall process as a choice between the assembly and testing branches
# The choice is silent (no explicit exit), so it's implied by the loop
root = OperatorPOWL(operator=Operator.XOR, children=[main_assembly, test_order])

# Add compliance and quality audit after the choice
root.order.add_edge(root, compliance_check)
root.order.add_edge(compliance_check, quality_audit)

# Finally, add packaging and logistics after quality audit
root.order.add_edge(quality_audit, package_drone)
root.order.add_edge(package_drone, delivery_plan)