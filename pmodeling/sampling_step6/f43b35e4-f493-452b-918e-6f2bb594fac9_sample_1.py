import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) using the given names
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

# Define the partial order with the defined transitions
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

# Define dependencies between activities
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(client_brief, part_sourcing)
root.order.add_edge(client_brief, component_fabric)
root.order.add_edge(client_brief, circuit_assembly)
root.order.add_edge(client_brief, software_upload)
root.order.add_edge(client_brief, initial_testing)
root.order.add_edge(client_brief, flight_calibrate)
root.order.add_edge(client_brief, payload_mount)
root.order.add_edge(client_brief, stress_testing)
root.order.add_edge(client_brief, feedback_loop)
root.order.add_edge(client_brief, quality_check)
root.order.add_edge(client_brief, certification)
root.order.add_edge(client_brief, packaging)
root.order.add_edge(client_brief, delivery_plan)
root.order.add_edge(client_brief, post_support)

# The final POWL model is defined in the 'root' variable