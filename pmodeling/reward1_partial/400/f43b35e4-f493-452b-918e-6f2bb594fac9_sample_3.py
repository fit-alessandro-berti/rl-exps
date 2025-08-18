import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
part_loop = OperatorPOWL(operator=Operator.LOOP, children=[part_sourcing, component_fabric])
circuit_loop = OperatorPOWL(operator=Operator.LOOP, children=[circuit_assembly, software_upload])
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_testing, flight_calibrate])
stress_loop = OperatorPOWL(operator=Operator.LOOP, children=[stress_testing, feedback_loop])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, certification])

# Define root partial order
root = StrictPartialOrder(nodes=[client_brief, design_draft, part_loop, circuit_loop, flight_loop, stress_loop, quality_loop, payload_mount, packaging, delivery_plan, post_support])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, part_loop)
root.order.add_edge(part_loop, circuit_loop)
root.order.add_edge(circuit_loop, flight_loop)
root.order.add_edge(flight_loop, stress_loop)
root.order.add_edge(stress_loop, quality_loop)
root.order.add_edge(quality_loop, payload_mount)
root.order.add_edge(payload_mount, packaging)
root.order.add_edge(packaging, delivery_plan)
root.order.add_edge(delivery_plan, post_support)