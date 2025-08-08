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

client_brief_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_brief, design_draft, part_sourcing, component_fabric, circuit_assembly, software_upload, initial_testing, flight_calibrate, payload_mount, stress_testing, feedback_loop])
quality_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, certification, packaging, delivery_plan])
post_support_loop = OperatorPOWL(operator=Operator.LOOP, children=[post_support])

root = StrictPartialOrder(nodes=[client_brief_loop, quality_check_loop, post_support_loop])
root.order.add_edge(client_brief_loop, quality_check_loop)
root.order.add_edge(quality_check_loop, post_support_loop)