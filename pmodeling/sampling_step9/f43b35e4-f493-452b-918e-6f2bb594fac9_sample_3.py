import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip = SilentTransition()

# Define loop nodes
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_calibrate, feedback_loop])
payload_loop = OperatorPOWL(operator=Operator.LOOP, children=[payload_mount, feedback_loop])
stress_loop = OperatorPOWL(operator=Operator.LOOP, children=[stress_testing, feedback_loop])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, feedback_loop])

# Define exclusive choice nodes
initial_choice = OperatorPOWL(operator=Operator.XOR, children=[initial_testing, skip])
payload_choice = OperatorPOWL(operator=Operator.XOR, children=[payload_mount, skip])
stress_choice = OperatorPOWL(operator=Operator.XOR, children=[stress_testing, skip])
quality_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])

# Define the root model
root = StrictPartialOrder(nodes=[client_brief, design_draft, part_sourcing, component_fabric, circuit_assembly, software_upload, initial_choice, payload_choice, stress_choice, quality_choice, flight_loop, payload_loop, stress_loop, quality_loop, packaging, delivery_plan, post_support])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, part_sourcing)
root.order.add_edge(part_sourcing, component_fabric)
root.order.add_edge(component_fabric, circuit_assembly)
root.order.add_edge(circuit_assembly, software_upload)
root.order.add_edge(software_upload, initial_choice)
root.order.add_edge(initial_choice, flight_loop)
root.order.add_edge(flight_loop, feedback_loop)
root.order.add_edge(feedback_loop, payload_choice)
root.order.add_edge(payload_choice, payload_loop)
root.order.add_edge(payload_loop, feedback_loop)
root.order.add_edge(feedback_loop, stress_choice)
root.order.add_edge(stress_choice, stress_loop)
root.order.add_edge(stress_loop, feedback_loop)
root.order.add_edge(feedback_loop, quality_choice)
root.order.add_edge(quality_choice, quality_loop)
root.order.add_edge(quality_loop, feedback_loop)
root.order.add_edge(feedback_loop, packaging)
root.order.add_edge(packaging, delivery_plan)
root.order.add_edge(delivery_plan, post_support)

# Save the result in the variable 'root'