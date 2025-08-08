import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define process structure
client_consult_to_spec_analysis = OperatorPOWL(operator=Operator.XOR, children=[client_consult, spec_analysis])
spec_analysis_to_module_select = OperatorPOWL(operator=Operator.XOR, children=[spec_analysis, module_select])
module_select_to_component_order = OperatorPOWL(operator=Operator.XOR, children=[module_select, component_order])
component_order_to_parts_inspect = OperatorPOWL(operator=Operator.XOR, children=[component_order, parts_inspect])
parts_inspect_to_frame_assemble = OperatorPOWL(operator=Operator.XOR, children=[parts_inspect, frame_assemble])
frame_assemble_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[frame_assemble, sensor_install])
sensor_install_to_motor_attach = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, motor_attach])
motor_attach_to_wiring_connect = OperatorPOWL(operator=Operator.XOR, children=[motor_attach, wiring_connect])
wiring_connect_to_software_upload = OperatorPOWL(operator=Operator.XOR, children=[wiring_connect, software_upload])
software_upload_to_calibration_test = OperatorPOWL(operator=Operator.XOR, children=[software_upload, calibration_test])
calibration_test_to_flight_simulate = OperatorPOWL(operator=Operator.XOR, children=[calibration_test, flight_simulate])
flight_simulate_to_quality_review = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, quality_review])
quality_review_to_user_train = OperatorPOWL(operator=Operator.XOR, children=[quality_review, user_train])
user_train_to_remote_setup = OperatorPOWL(operator=Operator.XOR, children=[user_train, remote_setup])
remote_setup_to_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[remote_setup, feedback_collect])
feedback_collect_to_support_schedule = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, support_schedule])

# Define partial order
root = StrictPartialOrder(nodes=[
    client_consult_to_spec_analysis,
    spec_analysis_to_module_select,
    module_select_to_component_order,
    component_order_to_parts_inspect,
    parts_inspect_to_frame_assemble,
    frame_assemble_to_sensor_install,
    sensor_install_to_motor_attach,
    motor_attach_to_wiring_connect,
    wiring_connect_to_software_upload,
    software_upload_to_calibration_test,
    calibration_test_to_flight_simulate,
    flight_simulate_to_quality_review,
    quality_review_to_user_train,
    user_train_to_remote_setup,
    remote_setup_to_feedback_collect,
    feedback_collect_to_support_schedule
])

# Define dependencies
root.order.add_edge(client_consult_to_spec_analysis, spec_analysis_to_module_select)
root.order.add_edge(spec_analysis_to_module_select, module_select_to_component_order)
root.order.add_edge(module_select_to_component_order, component_order_to_parts_inspect)
root.order.add_edge(component_order_to_parts_inspect, parts_inspect_to_frame_assemble)
root.order.add_edge(parts_inspect_to_frame_assemble, frame_assemble_to_sensor_install)
root.order.add_edge(frame_assemble_to_sensor_install, sensor_install_to_motor_attach)
root.order.add_edge(sensor_install_to_motor_attach, motor_attach_to_wiring_connect)
root.order.add_edge(motor_attach_to_wiring_connect, wiring_connect_to_software_upload)
root.order.add_edge(wiring_connect_to_software_upload, software_upload_to_calibration_test)
root.order.add_edge(software_upload_to_calibration_test, calibration_test_to_flight_simulate)
root.order.add_edge(calibration_test_to_flight_simulate, flight_simulate_to_quality_review)
root.order.add_edge(flight_simulate_to_quality_review, quality_review_to_user_train)
root.order.add_edge(quality_review_to_user_train, user_train_to_remote_setup)
root.order.add_edge(user_train_to_remote_setup, remote_setup_to_feedback_collect)
root.order.add_edge(remote_setup_to_feedback_collect, feedback_collect_to_support_schedule)

print(root)