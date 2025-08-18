import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process flow
client_consult_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[client_consult, spec_analysis, module_select, component_order])
component_order_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[parts_inspect, frame_assemble, sensor_install, motor_attach, wiring_connect, software_upload])
software_upload_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[calibration_test, flight_simulate, quality_review])
user_train_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[user_train, remote_setup])
remote_setup_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[feedback_collect, support_schedule])

# Define the partial order
root = StrictPartialOrder(nodes=[client_consult_process, component_order_process, software_upload_process, user_train_process, remote_setup_process])

# Add edges to the partial order
root.order.add_edge(client_consult_process, component_order_process)
root.order.add_edge(component_order_process, software_upload_process)
root.order.add_edge(software_upload_process, user_train_process)
root.order.add_edge(user_train_process, remote_setup_process)

print(root)