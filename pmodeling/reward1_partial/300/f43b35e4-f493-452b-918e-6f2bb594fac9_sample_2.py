import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[flight_calibrate, feedback_loop])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[stress_testing, feedback_loop])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, feedback_loop])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[certification, feedback_loop])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[delivery_plan, feedback_loop])

root = StrictPartialOrder(nodes=[
    client_brief,
    design_draft,
    part_sourcing,
    component_fabric,
    circuit_assembly,
    software_upload,
    initial_testing,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    packaging,
    post_support
])
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, part_sourcing)
root.order.add_edge(part_sourcing, component_fabric)
root.order.add_edge(component_fabric, circuit_assembly)
root.order.add_edge(circuit_assembly, software_upload)
root.order.add_edge(software_upload, initial_testing)
root.order.add_edge(initial_testing, xor1)
root.order.add_edge(initial_testing, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, packaging)
root.order.add_edge(xor5, post_support)