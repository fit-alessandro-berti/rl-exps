import pm4py
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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[client_consult, spec_analysis, module_select, component_order, parts_inspect, frame_assemble, sensor_install, motor_attach, wiring_connect, software_upload, calibration_test, flight_simulate, quality_review, user_train, remote_setup, feedback_collect, support_schedule])

# Define the order of transitions
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
root.order.add_edge(quality_review, user_train)
root.order.add_edge(user_train, remote_setup)
root.order.add_edge(remote_setup, feedback_collect)
root.order.add_edge(feedback_collect, support_schedule)

print(root)