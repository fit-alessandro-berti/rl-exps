import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
req_analysis = Transition(label='Requirement Analysis')
comp_sourcing = Transition(label='Component Sourcing')
quality_check = Transition(label='Quality Check')
frame_assembly = Transition(label='Frame Assembly')
motor_install = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
control_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
calibration = Transition(label='System Calibration')
flight_testing = Transition(label='Flight Testing')
error_correction = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_training = Transition(label='Client Training')
support_scheduling = Transition(label='Support Scheduling')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    req_analysis,
    comp_sourcing,
    quality_check,
    frame_assembly,
    motor_install,
    sensor_setup,
    control_unit,
    firmware_upload,
    calibration,
    flight_testing,
    error_correction,
    cosmetic_finish,
    packaging_prep,
    user_manual,
    client_training,
    support_scheduling
])

# Define the dependencies between the nodes
root.order.add_edge(req_analysis, comp_sourcing)
root.order.add_edge(comp_sourcing, quality_check)
root.order.add_edge(quality_check, frame_assembly)
root.order.add_edge(frame_assembly, motor_install)
root.order.add_edge(motor_install, sensor_setup)
root.order.add_edge(sensor_setup, control_unit)
root.order.add_edge(control_unit, firmware_upload)
root.order.add_edge(firmware_upload, calibration)
root.order.add_edge(calibration, flight_testing)
root.order.add_edge(flight_testing, error_correction)
root.order.add_edge(error_correction, cosmetic_finish)
root.order.add_edge(cosmetic_finish, packaging_prep)
root.order.add_edge(packaging_prep, user_manual)
root.order.add_edge(user_manual, client_training)
root.order.add_edge(client_training, support_scheduling)

# Print the POWL model
print(root)