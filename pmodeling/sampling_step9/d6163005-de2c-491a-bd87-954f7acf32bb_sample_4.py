import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop for flight testing
loop_flight_testing = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, error_correction])

# Define the choice for firmware upload and system calibration
choice_firmware_calibration = OperatorPOWL(operator=Operator.XOR, children=[firmware_upload, system_calibration])

# Define the choice for cosmetic finish and packaging preparation
choice_finish_packaging = OperatorPOWL(operator=Operator.XOR, children=[cosmetic_finish, packaging_prep])

# Define the loop for client training and support scheduling
loop_client_support = OperatorPOWL(operator=Operator.LOOP, children=[client_training, support_scheduling])

# Define the root POWL model
root = StrictPartialOrder(nodes=[requirement_analysis, component_sourcing, quality_check, frame_assembly, motor_installation, sensor_setup, control_unit, choice_firmware_calibration, loop_flight_testing, choice_finish_packaging, loop_client_support])
root.order.add_edge(requirement_analysis, component_sourcing)
root.order.add_edge(component_sourcing, quality_check)
root.order.add_edge(quality_check, frame_assembly)
root.order.add_edge(frame_assembly, motor_installation)
root.order.add_edge(motor_installation, sensor_setup)
root.order.add_edge(sensor_setup, control_unit)
root.order.add_edge(control_unit, choice_firmware_calibration)
root.order.add_edge(choice_firmware_calibration, loop_flight_testing)
root.order.add_edge(loop_flight_testing, choice_finish_packaging)
root.order.add_edge(choice_finish_packaging, loop_client_support)
root.order.add_edge(loop_client_support, client_training)
root.order.add_edge(client_training, support_scheduling)

# Print the root POWL model
print(root)