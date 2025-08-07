import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    client_brief, 
    design_draft, 
    part_sourcing, 
    component_fabric, 
    circuit_assembly, 
    software_upload, 
    initial_testing, 
    flight_calibrate, 
    payload_mount, 
    stress_testing, 
    feedback_loop, 
    quality_check, 
    certification, 
    packaging, 
    delivery_plan, 
    post_support
])

# Define the workflow dependencies
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, part_sourcing)
root.order.add_edge(part_sourcing, component_fabric)
root.order.add_edge(component_fabric, circuit_assembly)
root.order.add_edge(circuit_assembly, software_upload)
root.order.add_edge(software_upload, initial_testing)
root.order.add_edge(initial_testing, flight_calibrate)
root.order.add_edge(flight_calibrate, payload_mount)
root.order.add_edge(payload_mount, stress_testing)
root.order.add_edge(stress_testing, feedback_loop)
root.order.add_edge(feedback_loop, quality_check)
root.order.add_edge(quality_check, certification)
root.order.add_edge(certification, packaging)
root.order.add_edge(packaging, delivery_plan)
root.order.add_edge(delivery_plan, post_support)

# Print the POWL model
print(root)