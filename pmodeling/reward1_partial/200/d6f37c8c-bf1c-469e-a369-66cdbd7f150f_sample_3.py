from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[firmware_build, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pcb_assembly, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[motor_mount, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[battery_test, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[ai_module, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[system_integrate, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[package_drone, skip])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[component_order])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulate])

# Define the root model
root = StrictPartialOrder(nodes=[
    client_brief,
    design_draft,
    component_order,
    xor,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7,
    xor8,
    xor9,
    xor10,
    xor11,
    xor12,
    loop1,
    loop2
])

# Define the dependencies
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, component_order)
root.order.add_edge(component_order, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor8)

# Print the root model
print(root)