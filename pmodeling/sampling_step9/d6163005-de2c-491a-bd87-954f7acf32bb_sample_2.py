import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
req_analysis = Transition(label='Requirement Analysis')
comp_sourcing = Transition(label='Component Sourcing')
quality_check = Transition(label='Quality Check')
frame_assembly = Transition(label='Frame Assembly')
motor_install = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
control_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
system_calibrate = Transition(label='System Calibration')
flight_testing = Transition(label='Flight Testing')
error_correction = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_training = Transition(label='Client Training')
support_scheduling = Transition(label='Support Scheduling')

# Define the silent transitions
skip = SilentTransition()

# Define the loop for flight testing
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, error_correction])

# Define the XOR for firmware upload and system calibration
xor = OperatorPOWL(operator=Operator.XOR, children=[firmware_upload, system_calibrate])

# Define the POWL model
root = StrictPartialOrder(nodes=[req_analysis, comp_sourcing, quality_check, frame_assembly, motor_install, sensor_setup, control_unit, xor, flight_loop, cosmetic_finish, packaging_prep, user_manual, client_training, support_scheduling])
root.order.add_edge(req_analysis, comp_sourcing)
root.order.add_edge(comp_sourcing, quality_check)
root.order.add_edge(quality_check, frame_assembly)
root.order.add_edge(frame_assembly, motor_install)
root.order.add_edge(motor_install, sensor_setup)
root.order.add_edge(sensor_setup, control_unit)
root.order.add_edge(control_unit, xor)
root.order.add_edge(xor, flight_loop)
root.order.add_edge(flight_loop, error_correction)
root.order.add_edge(error_correction, cosmetic_finish)
root.order.add_edge(cosmetic_finish, packaging_prep)
root.order.add_edge(packaging_prep, user_manual)
root.order.add_edge(user_manual, client_training)
root.order.add_edge(client_training, support_scheduling)