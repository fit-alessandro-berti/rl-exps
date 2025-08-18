import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
client_brief = Transition(label='Client Brief')
design_draft = Transition(label='Design Draft')
part_sourcing = Transition(label='Part Sourcing')
component_fabric = Transition(label='Component Fabric')
circuit_assembly = Transition(label='Circuit Assembly')
software_upload = Transition(label='Software Upload')
initial_testing = Transition(label='Initial Testing')
flight_calibrate = Transition(label='Flight Calibrate')
payload_mount = Transition(label='Payload Mount')
stress_testing = Transition(label='Stress Testing')
feedback_loop = Transition(label='Feedback Loop')
quality_check = Transition(label='Quality Check')
certification = Transition(label='Certification')
packaging = Transition(label='Packaging')
delivery_plan = Transition(label='Delivery Plan')
post_support = Transition(label='Post Support')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[flight_calibrate, feedback_loop])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, certification])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[stress_testing, post_support])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[initial_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[payload_mount])

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    client_brief, design_draft, part_sourcing, component_fabric,
    circuit_assembly, software_upload, loop1, xor,
    xor2, xor3, loop2, feedback_loop, quality_check, stress_testing, post_support
])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, part_sourcing)
root.order.add_edge(part_sourcing, component_fabric)
root.order.add_edge(component_fabric, circuit_assembly)
root.order.add_edge(circuit_assembly, software_upload)
root.order.add_edge(software_upload, loop1)
root.order.add_edge(loop1, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop2)
root.order.add_edge(loop2, feedback_loop)
root.order.add_edge(feedback_loop, quality_check)
root.order.add_edge(quality_check, stress_testing)
root.order.add_edge(stress_testing, post_support)

print(root)