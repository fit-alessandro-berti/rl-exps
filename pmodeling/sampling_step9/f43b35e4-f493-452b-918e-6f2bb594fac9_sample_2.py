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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_calibrate, feedback_loop])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, feedback_loop])

# Define exclusive choice nodes
pre_assembly_choice = OperatorPOWL(operator=Operator.XOR, children=[client_brief, design_draft])
assembly_choice = OperatorPOWL(operator=Operator.XOR, children=[part_sourcing, circuit_assembly])

# Define the root POWL model
root = StrictPartialOrder(nodes=[pre_assembly_choice, assembly_choice, flight_loop, quality_loop, packaging, delivery_plan, post_support])
root.order.add_edge(pre_assembly_choice, assembly_choice)
root.order.add_edge(assembly_choice, flight_loop)
root.order.add_edge(assembly_choice, quality_loop)
root.order.add_edge(flight_loop, packaging)
root.order.add_edge(quality_loop, packaging)
root.order.add_edge(packaging, delivery_plan)
root.order.add_edge(delivery_plan, post_support)

print(root)