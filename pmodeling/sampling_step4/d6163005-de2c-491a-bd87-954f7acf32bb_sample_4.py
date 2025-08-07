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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    requirement_analysis,
    component_sourcing,
    quality_check,
    frame_assembly,
    motor_installation,
    sensor_setup,
    control_unit,
    firmware_upload,
    system_calibration,
    flight_testing,
    error_correction,
    cosmetic_finish,
    packaging_prep,
    user_manual,
    client_training,
    support_scheduling
])

# Define the order dependencies
root.order.add_edge(requirement_analysis, component_sourcing)
root.order.add_edge(component_sourcing, quality_check)
root.order.add_edge(quality_check, frame_assembly)
root.order.add_edge(frame_assembly, motor_installation)
root.order.add_edge(motor_installation, sensor_setup)
root.order.add_edge(sensor_setup, control_unit)
root.order.add_edge(control_unit, firmware_upload)
root.order.add_edge(firmware_upload, system_calibration)
root.order.add_edge(system_calibration, flight_testing)
root.order.add_edge(flight_testing, error_correction)
root.order.add_edge(error_correction, cosmetic_finish)
root.order.add_edge(cosmetic_finish, packaging_prep)
root.order.add_edge(packaging_prep, user_manual)
root.order.add_edge(user_manual, client_training)
root.order.add_edge(client_training, support_scheduling)

print(root)