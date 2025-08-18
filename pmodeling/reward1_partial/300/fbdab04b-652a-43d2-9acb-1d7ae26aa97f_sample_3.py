from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
client_consult = Transition(label='Client Consult')
spec_analysis = Transition(label='Spec Analysis')
module_select = Transition(label='Module Select')
component_order = Transition(label='Component Order')
parts_inspect = Transition(label='Parts Inspect')
frame_assemble = Transition(label='Frame Assemble')
sensor_install = Transition(label='Sensor Install')
motor_attach = Transition(label='Motor Attach')
wiring_connect = Transition(label='Wiring Connect')
software_upload = Transition(label='Software Upload')
calibration_test = Transition(label='Calibration Test')
flight_simulate = Transition(label='Flight Simulate')
quality_review = Transition(label='Quality Review')
user_train = Transition(label='User Train')
remote_setup = Transition(label='Remote Setup')
feedback_collect = Transition(label='Feedback Collect')
support_schedule = Transition(label='Support Schedule')

# Define the loop for iterative testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[calibration_test, flight_simulate, quality_review])

# Define the exclusive choice for user training and remote setup
xor = OperatorPOWL(operator=Operator.XOR, children=[user_train, remote_setup])

# Create the root node with all the activities and the loop and exclusive choice
root = StrictPartialOrder(nodes=[client_consult, spec_analysis, module_select, component_order, parts_inspect, frame_assemble, sensor_install, motor_attach, wiring_connect, software_upload, calibration_test, flight_simulate, quality_review, xor, support_schedule])
root.order.add_edge(client_consult, spec_analysis)
root.order.add_edge(spec_analysis, module_select)
root.order.add_edge(module_select, component_order)
root.order.add_edge(component_order, parts_inspect)
root.order.add_edge(parts_inspect, frame_assemble)
root.order.add_edge(frame_assemble, sensor_install)
root.order.add_edge(sensor_install, motor_attach)
root.order.add_edge(motor_attach, wiring_connect)
root.order.add_edge(wiring_connect, software_upload)
root.order.add_edge(software_upload, calibration_test)
root.order.add_edge(calibration_test, flight_simulate)
root.order.add_edge(flight_simulate, quality_review)
root.order.add_edge(quality_review, xor)
root.order.add_edge(xor, support_schedule)