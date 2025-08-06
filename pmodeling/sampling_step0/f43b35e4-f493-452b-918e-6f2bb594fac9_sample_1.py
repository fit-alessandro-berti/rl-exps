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

# Define the silent transition (feedback loop)
skip = SilentTransition()

# Define the loops and exclusive choices
loop_initial_testing = OperatorPOWL(operator=Operator.LOOP, children=[initial_testing, software_upload, flight_calibrate, payload_mount, stress_testing])
loop_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, certification, post_support])
xor_part_sourcing = OperatorPOWL(operator=Operator.XOR, children=[part_sourcing, skip])
xor_circuit_assembly = OperatorPOWL(operator=Operator.XOR, children=[circuit_assembly, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[client_brief, design_draft, xor_part_sourcing, xor_circuit_assembly, loop_initial_testing, loop_quality_check])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, xor_part_sourcing)
root.order.add_edge(design_draft, xor_circuit_assembly)
root.order.add_edge(xor_part_sourcing, loop_initial_testing)
root.order.add_edge(xor_circuit_assembly, loop_initial_testing)
root.order.add_edge(loop_initial_testing, loop_quality_check)
root.order.add_edge(loop_quality_check, xor_circuit_assembly)
root.order.add_edge(xor_circuit_assembly, loop_quality_check)