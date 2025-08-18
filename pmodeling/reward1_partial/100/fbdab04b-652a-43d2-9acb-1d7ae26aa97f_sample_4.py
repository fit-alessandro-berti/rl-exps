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

# Define exclusive choices for sequential steps
spec_analysis_and_module_select = OperatorPOWL(operator=Operator.XOR, children=[spec_analysis, module_select])
component_order_and_parts_inspect = OperatorPOWL(operator=Operator.XOR, children=[component_order, parts_inspect])
frame_assemble_and_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[frame_assemble, sensor_install])
motor_attach_and_wiring_connect = OperatorPOWL(operator=Operator.XOR, children=[motor_attach, wiring_connect])
software_upload_and_calibration_test = OperatorPOWL(operator=Operator.XOR, children=[software_upload, calibration_test])
flight_simulate_and_quality_review = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, quality_review])
user_train_and_remote_setup = OperatorPOWL(operator=Operator.XOR, children=[user_train, remote_setup])

# Define loop for iterative testing
calibration_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibration_test])

# Define root as a strict partial order with the defined transitions and exclusive choices
root = StrictPartialOrder(nodes=[
    client_consult,
    spec_analysis_and_module_select,
    component_order_and_parts_inspect,
    frame_assemble_and_sensor_install,
    motor_attach_and_wiring_connect,
    software_upload_and_calibration_test,
    flight_simulate_and_quality_review,
    user_train_and_remote_setup
])

# Add dependencies between nodes
root.order.add_edge(client_consult, spec_analysis_and_module_select)
root.order.add_edge(client_consult, component_order_and_parts_inspect)
root.order.add_edge(spec_analysis_and_module_select, component_order_and_parts_inspect)
root.order.add_edge(component_order_and_parts_inspect, frame_assemble_and_sensor_install)
root.order.add_edge(frame_assemble_and_sensor_install, motor_attach_and_wiring_connect)
root.order.add_edge(motor_attach_and_wiring_connect, software_upload_and_calibration_test)
root.order.add_edge(software_upload_and_calibration_test, flight_simulate_and_quality_review)
root.order.add_edge(flight_simulate_and_quality_review, user_train_and_remote_setup)

# Add loop dependency
root.order.add_edge(software_upload_and_calibration_test, calibration_test_loop)
root.order.add_edge(calibration_test_loop, calibration_test)