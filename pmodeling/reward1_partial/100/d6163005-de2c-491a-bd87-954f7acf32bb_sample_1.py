import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
requirement_analysis = Transition(label='Requirement Analysis')
component_sourcing = Transition(label='Component Sourcing')
quality_check = Transition(label='Quality Check')
frame_assembly = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
control_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
system_calibration = Transition(label='System Calibration')
flight_testing = Transition(label='Flight Testing')
error_correction = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_training = Transition(label='Client Training')
support_scheduling = Transition(label='Support Scheduling')

# Define the workflow model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, error_correction])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, error_correction])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[system_calibration, firmware_upload])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, control_unit])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[motor_installation, quality_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, client_training])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[user_manual, support_scheduling])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[requirement_analysis, component_sourcing])

root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop1)
root.order.add_edge(xor6, loop2)