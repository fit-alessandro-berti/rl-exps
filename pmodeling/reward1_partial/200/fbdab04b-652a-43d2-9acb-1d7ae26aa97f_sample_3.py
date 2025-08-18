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

# Define the loop for the assembly phase
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    client_consult, spec_analysis, module_select, component_order, parts_inspect, frame_assemble, sensor_install, motor_attach, wiring_connect, software_upload, calibration_test, flight_simulate, quality_review
])

# Define the XOR for the user training and remote setup
xor = OperatorPOWL(operator=Operator.XOR, children=[
    user_train, remote_setup
])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root for verification
print(root)