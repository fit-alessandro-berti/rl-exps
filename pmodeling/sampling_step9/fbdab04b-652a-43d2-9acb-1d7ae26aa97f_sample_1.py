import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[client_consult, spec_analysis, module_select, component_order, parts_inspect])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[frame_assemble, sensor_install, motor_attach, wiring_connect, software_upload])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[calibration_test, flight_simulate, quality_review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[user_train, remote_setup, feedback_collect, support_schedule])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])

root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, xor2)

print(root)